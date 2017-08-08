from binaryninja import RepositoryManager, user_plugin_path, log_error, log_info
import json
import pip

plugin_list = ['Annotator', 'Explain Instruction', 'Syscaller', 'binja_dynamics', 'binja_arch_ref']

def handle_dependencies(plugin):
    path = user_plugin_path.replace('plugins', 'repositories/default/plugins')
    plugin_json = '{}/{}/plugin.json'.format(path, plugin.path)
    try:
        with open(plugin_json, 'r') as jsonfile:
            raw_data = json.load(jsonfile)
            dependencies = raw_data["plugin"]["dependencies"]
            if "pip" in dependencies:
                for package in dependencies["pip"]:
                    print("Installing {} depdency: {}".format(plugin.name, package))
                    try:
                        pip.main(['install', package])
                    except IOError:
                        print("Unable to install {}. Permissions?".format(package))
    except IOError:
        log_error("Unable to install dependencies for {}".format(plugin.name))

manager = RepositoryManager()
manager.check_for_updates()
for plugin in manager.plugins['default']:
    if plugin.name in plugin_list:
        if not plugin.installed:
            log_info("Installing {}".format(plugin.name))
            succ = manager.enable_plugin(plugin.name, install=True)
            if not succ:
                log_error("{} installation failed".format(plugin.name))
            handle_dependencies(plugin)
        else:
            log_info("Updating {}".format(plugin.name))
            manager.update_plugin(plugin)

import writeups
