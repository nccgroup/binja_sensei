from binaryninja import RepositoryManager

plugin_list = ['Annotator', 'binja_explain_instruction', 'Syscaller']

manager = RepositoryManager()
manager.check_for_updates()
for plugin in manager.plugins['default']:
    if plugin.name in plugin_list:
        if not plugin.installed:
            manager.enable_plugin(plugin.name)
        else:
            manager.update_plugin(plugin)

import writeups
