import os
import shutil
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py folder_path")
    sys.exit(1)

folder_path = sys.argv[1]
subfolder_names = ['Binaries', 'Build', 'DerivedDataCache', 'Intermediate', 'Saved', '.idea', '.vs', '.vscode']
plugin_subdir_name = 'Plugins'
file_extension = ['.sln', '.code-workspace']


for name in os.listdir(folder_path):
    fullname = os.path.join(folder_path, name)
    if name in subfolder_names and os.path.isdir(fullname):
        print(f"Deleting {fullname}")
        shutil.rmtree(fullname)
    
    if name == plugin_subdir_name and os.path.isdir(fullname):
        print(f"Checking {fullname}")
        for plugin_name in os.listdir(fullname):
            plugin_path = os.path.join(fullname, plugin_name)
            for plugin_folder in os.listdir(plugin_path):
                full_plugin_folder = os.path.join(plugin_path, plugin_folder)
                if plugin_folder in subfolder_names and os.path.isdir(full_plugin_folder):
                    print(f"Deleting {plugin_path}")
                    shutil.rmtree(full_plugin_folder)

    if os.path.splitext(name)[-1] in file_extension:
        print(f"Deleting {fullname}")
        os.remove(fullname)
