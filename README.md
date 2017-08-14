# binja_sensei
Educational tools for Binary Ninja

This plugin provides resources for beginners to learn reverse engineering using Binary Ninja. It automatically installs several other plugins, and provides examples that showcase the features of these plugins.

## Origins
This project is a product of [NCC Group](https://www.nccgroup.trust/us/)'s 2017 summer internship program.

## Setup

#### Plugin Manager
For the sake of futureproofing, Binja Sensei installs plugins via the yet-incomplete Plugin Manager API. Since the plugin manager does not currently have a GUI, installation must be accomplished by running the following snippet at the Binary Ninja script console (Accessed via Ctrl+\`).
```python
manager = RepositoryManager()

manager.enable_plugin('binja_sensei', install=True)
```
Note: Depending on when you installed Binja, you may need to run `manager.check_for_updates()` and restart Binja for this plugin to show up. I strongly recommend installing on a fresh VM.

If you're running this before August 31st, 2017, you'll need to be using the development version of Binary Ninja, as dependency installation relies on [	b0778fc](https://github.com/Vector35/binaryninja-api/commit/b0778fc4d0271a9ba16e7c81c2c4c67a8273cda6) and [326253a](https://github.com/Vector35/binaryninja-api/commit/326253abc74f7d6b601e03463df6abe8b8929428).

Next, restart Binary Ninja. When loaded, Sensei will update all the bundled plugins to the latest version, and install any python dependencies for each plugin. It *won't* automatically run install scripts, so if you're on Ubuntu and intend to set up `binja_dynamics`, you'll need to navigate to `~/.binaryninja/repositories/default/plugins/binja_dynamics` and run `./install.sh`.

#### Manual Installation
If any of the plugin installations fail, you may have more success performing a manual installation. Pending [Issue #753](https://github.com/Vector35/binaryninja-api/issues/753), some plugins that reply on absolute file paths may not work unless manually installed. To manually install, copy the relevant repository links below, and clone them inside of your [plugins directory](https://github.com/Vector35/binaryninja-api/tree/master/python/examples#loading-plugins).
```
https://github.com/carstein/Annotator.git
https://github.com/ehennenfent/binja_arch_ref.git
https://github.com/ehennenfent/binja_dynamics.git
https://github.com/ehennenfent/binja_explain_instruction.git
https://github.com/carstein/Syscaller.git
```

## Bundled Tools
Please note that the bundled tools remain property of their respective authors. While this plugin is offered under an [MIT License](LICENSE), that license does not extend to any of the plugins below.
* [**Annotator**](#annotator) by Carstein
* [**Architecture Reference**](#architecture-reference)
* [**Binja Dynamic Analysis Tools**](#binja-dynamic-analysis-tools)
* [**Explain Instruction**](#explain-instruction)
* [**Syscaller**](#syscaller) by Carstein

## Writeups
To demonstrate potential use cases for these plugins, solutions for the five overflow challenges from [PicoCTF 2013](https://github.com/picoCTF/2013-Problems) are included. Please note that minor changes in terms of functionality, color scheme, and bugfixes may have been implemented since the creation of the writeups.

* [Overflow 1](writeups/overflow1/writeup.md)
* [Overflow 2](writeups/overflow2/writeup.md)
* [Overflow 3](writeups/overflow3/writeup.md)
* [Overflow 4](writeups/overflow4/writeup.md)
* [Overflow 5](writeups/overflow5/writeup.md)

## Examples

### [Annotator](https://github.com/carstein/Annotator/)
Annotator uses a virtual stack to annotate calls to libc functions with argument prototypes.
![annotator screenshot](screenshots/annotator.png)

### [Architecture Reference](https://github.com/ehennenfent/binja_arch_ref)
This plugin displays a cheat sheet with Binary Ninja's internal information on the architecture.
![arch-ref screenshot](screenshots/arch-ref.png)

### [Binja Dynamic Analysis Tools](https://github.com/ehennenfent/binja_dynamics)
This plugin adds a Qt frontend to [Binjatron](https://github.com/snare/binjatron), including highlights intended to help beginners spot important memory locations.
![binja-dynamics screenshot](screenshots/binja-dynamics.png)

### [Explain Instruction](https://github.com/ehennenfent/binja_explain_instruction/)
Adds a popup window that explains in simple English what an assembly instruction does.
![binja-explain-instruction screenshot](screenshots/binja-explain-instruction.png)

### [Syscaller](https://github.com/carstein/Syscaller)
Annotates system calls with arguments.
![syscaller screenshot](screenshots/syscaller.png)
