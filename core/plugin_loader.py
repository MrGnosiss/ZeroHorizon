import importlib.util
import os

def load_plugins(path="plugins"):
    plugins = []
    for file in os.listdir(path):
        if file.endswith(".py"):
            spec = importlib.util.spec_from_file_location(file[:-3], os.path.join(path, file))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            plugins.append(mod)
    return plugins
