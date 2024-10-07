from moduls.examples.models.sqlalchemy import SQLALCHEMY_ITEM_MODEL
from moduls.examples.models.sqlmodel import SQLMODEL_ITEM_MODEL
from moduls.examples.routes_examples import ROUTES_EXAMPLE
from moduls.examples.repositories_examples import SQLALCHEMY_REPOSITORY_EXAMPLE, SQLMODEL_REPOSITORY_EXAMPLE
from moduls.examples.services_examples import SQLALCHEMY_SERVICE_EXAMPLE, SQLMODEL_SERVICE_EXAMPLE
from moduls.examples.alembic import ALEMBIC_INI_TEMPLATE

import os

class ScaffoldingGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate_structure(self):
        project_name = self.settings.project_name
        os.makedirs(f"{project_name}/app", exist_ok=True)

        # Create versioned or non-versioned structure
        if self.settings.versioning:
            os.makedirs(f"{project_name}/app/v1", exist_ok=True)
        os.makedirs(f"{project_name}/config", exist_ok=True)

        # Call the function to create models
        self._create_models()

        # Create repositories and services
        self._create_repositories()
        self._create_services()

        # Create routes
        self._create_routes()

        # Create main file
        self._create_main_file()

        # Create Alembic structure if Alembic is enabled
        if self.settings.use_alembic:
            self._create_alembic_structure()


    def _create_main_file(self):
        content = "from fastapi import FastAPI\n"
        if self.settings.orm_choice == "SQLAlchemy":
            content += "from sqlalchemy.orm import Session\n"
        elif self.settings.orm_choice == "SQLModel":
            content += "from sqlmodel import Session\n"

        if self.settings.versioning:
            content += "from app.v1.routes import items\n"
        else:
            content += "from app.routes import items\n"

        content += "\napp = FastAPI()\n"
        content += "app.include_router(items.router)\n"

        with open(f"{self.settings.project_name}/app/main.py", "w") as f:
            f.write(content)

    def _create_routes(self):
        # Determine the path for the routes directory
        if self.settings.versioning:
            routes_path = f"{self.settings.project_name}/app/v1/routes"
        else:
            routes_path = f"{self.settings.project_name}/app/routes"

        os.makedirs(routes_path, exist_ok=True)

        # Write the routes example to the __init__.py file
        with open(f"{routes_path}/__init__.py", "w") as f:
            f.write(ROUTES_EXAMPLE)            

    def _create_models(self):
        if self.settings.versioning:
            models_path = f"{self.settings.project_name}/app/v1/models"
        else:
            models_path = f"{self.settings.project_name}/app/models"

        os.makedirs(models_path, exist_ok=True)

        # Ensure that the correct model example is written based on the ORM choice
        if self.settings.orm_choice == "SQLAlchemy":
            model_example = SQLALCHEMY_ITEM_MODEL
        elif self.settings.orm_choice == "SQLModel":
            model_example = SQLMODEL_ITEM_MODEL

        # Write the model example to the __init__.py file
        with open(f"{models_path}/__init__.py", "w") as f:
            f.write(model_example)

    def _create_repositories(self):
        if self.settings.versioning:
            repositories_path = f"{self.settings.project_name}/app/v1/repositories"
        else:
            repositories_path = f"{self.settings.project_name}/app/repositories"

        os.makedirs(repositories_path, exist_ok=True)

        # Write the appropriate repository example to the __init__.py file
        if self.settings.orm_choice == "SQLAlchemy":
            repository_example = SQLALCHEMY_REPOSITORY_EXAMPLE
        elif self.settings.orm_choice == "SQLModel":
            repository_example = SQLMODEL_REPOSITORY_EXAMPLE

        with open(f"{repositories_path}/__init__.py", "w") as f:
            f.write(repository_example)

    def _create_services(self):
        if self.settings.versioning:
            services_path = f"{self.settings.project_name}/app/v1/services"
        else:
            services_path = f"{self.settings.project_name}/app/services"

        os.makedirs(services_path, exist_ok=True)

        # Write the appropriate service example to the __init__.py file
        if self.settings.orm_choice == "SQLAlchemy":
            service_example = SQLALCHEMY_SERVICE_EXAMPLE
        elif self.settings.orm_choice == "SQLModel":
            service_example = SQLMODEL_SERVICE_EXAMPLE

        with open(f"{services_path}/__init__.py", "w") as f:
            f.write(service_example)

    def _create_sqlalchemy_model(self, models_path):
        # Create item.py file with SQLAlchemy model
        with open(f"{models_path}/item.py", "w") as f:
            f.write(SQLALCHEMY_ITEM_MODEL)

    def _create_sqlmodel_model(self, models_path):
        # Create item.py file with SQLModel model
        with open(f"{models_path}/item.py", "w") as f:
            f.write(SQLMODEL_ITEM_MODEL)

    def _create_alembic_structure(self):
        project_name = self.settings.project_name
        os.makedirs(f"{project_name}/migrations", exist_ok=True)
    
        # Get the correct database URL based on the user's choice
        db_url = self._generate_db_url()
    
        # Use the string template from moduls/examples/alembic.py
        alembic_ini_content = ALEMBIC_INI_TEMPLATE.format(project_name=project_name, db_url=db_url)
    
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
