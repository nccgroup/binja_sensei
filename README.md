# binja_sensei
Educational tools for Binary Ninja

This plugin provides resources for beginners to learn reverse engineering using Binary Ninja. It acts as a wrapper around several other plugins, and provides examples that showcase the features of these plugins.

## Setup
Due to a [bug](https://github.com/Vector35/binaryninja-api/issues/740) (as of dev-1.0.794) in the way Binary Ninja handles repository management, all the plugins installed by Binja Sensei will be disabled. To fix this, after first installing Sensei, simply run the following snippet in the script console, then restart Binja.
``` python
import binja_sensei
manager = RepositoryManager()
for plugin in binja_sensei.plugin_list:
  manager.enable_plugin(plugin)
```

## Bundled Tools
* [Annotator](#annotator)
* [Architecture Reference](#architecture-reference)
* [Binja Dynamic Analysis Tools](#binja-dynamic-analysis-tools)
* [Explain Instruction](#explain-instruction)
* [Syscaller](#syscaller)

## Writeups
To demonstrate potential use cases for these plugins, solutions for the five overflow challenges from [PicoCTF 2013](https://github.com/picoCTF/2013-Problems) are included.

* [Overflow 1](writeups/overflow1/writeup.md)
* [Overflow 2](writeups/overflow2/writeup.md)
* [Overflow 3](writeups/overflow3/writeup.md)
* [Overflow 4](writeups/overflow4/writeup.md)
* [Overflow 5](writeups/overflow5/writeup.md)

### [Annotator](https://github.com/carstein/Annotator/)
### [Architecture Reference](https://github.com/ehennenfent/binja_arch_ref)
### [Binja Dynamic Analysis Tools](https://github.com/ehennenfent/binja_dynamics)
### [Explain Instruction](https://github.com/ehennenfent/binja_explain_instruction/)
### [Syscaller](https://github.com/carstein/Syscaller)
