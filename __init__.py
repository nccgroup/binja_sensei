from binaryninja import RepositoryManager, user_plugin_path, log_error, log_info
import json
import pip
import traceback

plugin_list = ['Annotator', 'Explain Instruction', 'Syscaller', 'Binary Ninja Dynamic Analysis Tools', 'Binja Architecture Reference']

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
                        pip.main(['install', '-q', package])
                    except IOError:
                        print("Unable to install {}. Permissions?".format(package))
                        traceback.print_exc()
    except IOError:
        log_error("Unable to install dependencies for {}".format(plugin.name))
        traceback.print_exc()

manager = RepositoryManager()
manager.check_for_updates()
for plugin in manager.plugins['default']:
    if plugin.name in plugin_list:
        if not plugin.installed:
            log_info("Installing {}".format(plugin.name))
            succ = manager.enable_plugin(plugin, install=True)
            if not succ:
                log_error("{} installation failed".format(plugin.name))
                traceback.print_exc()
            handle_dependencies(plugin)
        else:
            log_info("Updating {}".format(plugin.name))
            manager.update_plugin(plugin)
            handle_dependencies(plugin)

# import writeups
