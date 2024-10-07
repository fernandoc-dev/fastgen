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

        # Create Alembic structure if Alembic is enabled
        if self.settings.use_alembic:
            self._create_alembic_structure()

    def _create_main_file(self):
        content = "from fastapi import FastAPI\n\napp = FastAPI()\n\n"
        if self.settings.versioning:
            content += "from app.v1.routers import example_router\napp.include_router(example_router)\n"
        else:
            content += "@app.get('/')\ndef read_root():\n    return {'message': 'Hello World'}\n"
        with open(f"{self.settings.project_name}/app/main.py", "w") as f:
            f.write(content)

    def _create_alembic_structure(self):
        project_name = self.settings.project_name
        os.makedirs(f"{project_name}/migrations", exist_ok=True)

        # Get the correct database URL based on the user's choice
        db_url = self._generate_db_url()

        # alembic.ini file with dynamic sqlalchemy.url
        alembic_ini_content = f"""
[alembic]
script_location = {project_name}/migrations

# IMPORTANT: Set the database URL here
sqlalchemy.url = {db_url}

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers = console
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers = console
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stdout,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
"""
        with open(f"{project_name}/alembic.ini", "w") as f:
            f.write(alembic_ini_content)

        # Placeholder migration script
        with open(f"{project_name}/migrations/env.py", "w") as f:
            f.write("# Alembic environment script (to be completed)\n")

        print(f"Alembic structure and alembic.ini file created in {project_name}/migrations")

    def _generate_db_url(self):
        """
        Generates the SQLAlchemy database URL based on the user's database choice.
        """
        db_type = self.settings.db_choice
        if db_type == "PostgreSQL":
            return "postgresql://user:password@localhost:5432/mydatabase"
        elif db_type == "MySQL":
            return "mysql://user:password@localhost:3306/mydatabase"
        elif db_type == "MariaDB":
            return "mariadb://user:password@localhost:3306/mydatabase"
        else:
            return "sqlite:///./test.db"  # Default SQLite configuration
