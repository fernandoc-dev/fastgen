import os

class ScaffoldingGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate_structure(self):
        project_name = self.settings.project_name
        os.makedirs(f"{project_name}/app", exist_ok=True)
        if self.settings.versioning:
            os.makedirs(f"{project_name}/app/v1", exist_ok=True)
        os.makedirs(f"{project_name}/config", exist_ok=True)
        self._create_main_file()

    def _create_main_file(self):
        content = "from fastapi import FastAPI\n\napp = FastAPI()\n\n"
        if self.settings.versioning:
            content += "from app.v1.routers import example_router\napp.include_router(example_router)\n"
        else:
            content += "@app.get('/')\ndef read_root():\n    return {'message': 'Hello World'}\n"
        with open(f"{self.settings.project_name}/app/main.py", "w") as f:
            f.write(content)