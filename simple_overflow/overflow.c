#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

void dont_execute_this(void){
    exit(1);
}

void shell(void) {
    execl("/bin/sh", "sh", NULL);
}

void vuln(char *str) {
    char buf[32];
    strcpy(buf, str);
}

int main(int argc, char **argv){
    char vbuf[64];
    memset(vbuf, 0, 64);
    read(0, vbuf, 64);
    vuln(vbuf);
    return 0;
}
