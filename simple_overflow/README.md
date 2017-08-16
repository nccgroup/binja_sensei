## Showcase
Consider the following C snippet:

```c
void shell(void) {
    execl("/bin/sh", "sh", NULL);
}

void vuln(char *str) {
    char buffer[32];
    // Doesn't check whether str is less than 32 bytes long
    strcpy(buffer, str);
}

int main(int argc, char **argv){
    char vulnerable_buffer[64];
    memset(vulnerable_buffer, 0, 64);

    // read up to 64 bytes from stdin
    read(0, vulnerable_buffer, 64);
    vuln(vulnerable_buffer);

    return 0;
}
```

There are two important things to notice about this snippet:
* It exhibits a buffer overflow vulnerability. The buffer in the `vuln` function can only hold 32 bytes, but the `main` function may pass it as many as 64 bytes. When `strcpy` is called in the `vuln` function, it may overwrite the contents of the stack.
* The function `shell` executes `/bin/sh`, but it is never called.

As an attacker, I want to craft an exploit that tricks this program into executing the `shell` function so I can take control of the computer running it. Let's look at how I can use the tools created for this project to develop such an exploit.

First, I'll open the [overflow](overflow) binary in Binary Ninja and enable `binja_dynamics` (Tools --> Enable Dynamic Analysis Tools). I'll step through the first few instructions of `main`. The important highlights are marked in the image below.

![Screenshot](images/1.png)

I'll step down to the call to `read`, which makes the interaction panel pop up. I'll enter 16 A's, which should be fairly easy to spot in the memory viewer. Note how the memory viewer highlights the updated bytes in orange once the call to `read` completes.

![Screenshot](images/2.gif)

I'll step for a few more instructions until I get into the `vuln` function and its stack frame is set up. The sequence of A's I entered is still visible on the stack frame below the current one. I've highlighted the relevant bytes in green to make them easy to spot.

![Screenshot](images/3.png)

I'll step over the call to `strcpy`. Afterwards, I can see that the 16 A's have been copied into the buffer in the current stack frame. Since I have the source code for the binary, this doesn't come as a surprise.

![Screenshot](images/4.png)

While the return address is automatically highlighted in red, I've manually highlighted the bytes I'll try to overwrite in green. According to the traceback viewer, the return address of `vuln` is `0x4006dd`.

![Screenshot](images/5.png)

To confirm this, I'll double check the endianness in the architecture reference. The reference confirms that x86 is little-endian. Going back to the highlighted green bytes in the previous image, I can see that they contain `dd` `06` `40` `00`, which, when converted from little-endian form, become 0x004006dd.

![Screenshot](images/8.png)

![Screenshot](images/6.png)

![Screenshot](images/7.png)

![Screenshot](images/9.png)

![Screenshot](images/10.png)

![Screenshot](images/11.png)

![Screenshot](images/12.png)

```python
buffer_length = 32
saved_rbp_width = 8

print 'A'*(buffer_length + saved_rbp_width) # + ???

```

Helpfully, Binary Ninja will show me the address of each instruction. The address of the first instruction in `shell` is `0x400654`.

![Screenshot](images/13.png)

```python
import struct

buffer_length = 32
saved_rbp_width = 8

desired_return_address = 0x400654
packed_return_address = struct.pack('<I', desired_return_address)


print 'A'*(buffer_length + saved_rbp_width) + packed_return_address

```

I'm now ready to test the exploit. I'll run the solution script, and at first pipe the output into a hexdump to make sure that everything looks correct. Since it does, I'll pipe it into the `base64` utility to get an easily copy-and-paste-able version.

![Screenshot](images/14.png)

After starting the program over and stepping over the `read` call, I'l change the mode of the input panel to base 64, and paste in the output of the exploit script.

![Screenshot](images/15.png)

After the call completes, I can see that the memory now contains the exploit bytes, which have been properly base 64 decoded. Since I'm still in the `vuln` function, they haven't overwritten anything yet.
![Screenshot](images/16.png)

Now I'll step through into the `vuln` function, where the gif below shows the before and after of stepping over the call to `strcpy`. The buffer in `vuln` turns orange as `strcpy` overwrites the bytes there with the exploit. Since there are more bytes in the exploit than there is space in the buffer, `strcpy` keeps overwriting memory, and by following the orange highlights, I can see that the return address is overwritten as well. In the traceback viewer, I click on the button showing the new return address, and I get taken to the first instruction of `shell`. The exploit worked.

![Screenshot](images/17.gif)

Next, I'll step through the `leave` and `retn` instructions. Since I successfully overwrote the return address with the address of `shell`, the instruction pointer now points to the first instruction there. As you can see in the traceback viewer, overwriting the saved base pointer did some horrible things to the stack. Fortunately, I don't need to be concerned about this, since I only care whether `shell` drops a shell as expected, not whether it exits without throwing a segmentation fault.

![Screenshot](images/18.png)

Before I go any further, I need to delete the breakpoints set in GDB. If I don't do this, the exploit will still work, but GDB will attempt to set breakpoints in `/bin/sh` after we execute it, which will cause problems because `/bin/sh` has a different address layout than the current binary.

![Screenshot](images/19.png)

Since I deleted the breakpoints at the GDB console instead of via the Binja UI, binjatron will complain that the existing breakpoints have suddenly disappeared. I'll click "No" at the prompt so that it doesn't undo what I just did.

![Screenshot](images/20.png)

Next, I'll click the "Continue" button, which will tell GDB to continue executing until it hits another breakpoint (all of which we just deleted). The shell function executes `/bin/sh`, and a prompt appears in the interaction console.

![Screenshot](images/21.png)

Just to prove that everything works, I'll run the `whoami` command at the console, which prints out my username.

![Screenshot](images/22.png)

Exploiting a program in GDB is one thing, but I want to double check that my exploit works in an actual environment. I'll pipe the output of the python solution into `pbcopy` to put it on my clipboard, verify that it worked as expected by piping `pbpaste` into a hexdump, then run the program and paste in the exploit. Just as in GDB, the exploit gets us a shell. Note that my VM has ASLR turned off so that the address space in bash will match the address space in GDB.

![Screenshot](images/23.png)

### Further Reading
This writeup focused on showcasing how the tools bundled with this plugin can aid a beginner in exploiting a program via a buffer overflow, not on how buffer overflows work. For more information on buffer overflows, consider reading the seminal work on the subject: [Smashing the Stack for Fun and Profit](https://www.eecs.umich.edu/courses/eecs588/static/stack_smashing.pdf).
