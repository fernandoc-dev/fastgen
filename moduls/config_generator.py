import os

class ConfigGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate_config(self):
        config_path = f"{self.settings.project_name}/config"
        os.makedirs(config_path, exist_ok=True)
        with open(f"{config_path}/settings.py", "w") as f:
            f.write(self._generate_base_config())

    def _generate_base_config(self):
        return """
# Base config for the project

class Settings:
    ENVIRONMENT = 'development'
    DEBUG = True

    # Database configurations
    DATABASE_URL = "sqlite:///./test.db"
"""