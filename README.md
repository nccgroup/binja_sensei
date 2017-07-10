# binja_sensei
Educational tools for Binary Ninja

This plugin provides resources for beginners to learn reverse engineering using Binary Ninja. It acts as a wrapper around several other plugins, and provides sample binaries that showcase the features provided by the plugins.

## Setup
Due to a bug (as of dev-1.0.794) in the way Binary Ninja handles repository management, all the plugins installed by Binja Sensei will be disabled. To fix this, after first installing Sensei, simply run the following snippet in the script console, then restart Binja.
``` python
import binja_sensei
manager = RepositoryManager()
for plugin in binja_sensei.plugin_list:
  manager.enable_plugin(plugin)
```
