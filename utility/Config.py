import os
import json

CONFIG_FILE = "config.json"

class ConfigUtils:
    @staticmethod
    def load_or_create_config():
       
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    print("Invalid config format. Recreating empty config.")
                    return {}
        else:
            return {}

    @staticmethod
    def save_config(config):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)

    @staticmethod
    def get_value(key):
        config = ConfigUtils.load_or_create_config()
        return config.get(key, "")

    @staticmethod
    def set_value(key, value):

        config = ConfigUtils.load_or_create_config()
        config[key] = value
        ConfigUtils.save_config(config)

