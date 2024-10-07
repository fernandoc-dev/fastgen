class RequirementsGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate_requirements(self):
        requirements = [
            "fastapi",
            "uvicorn[standard]",
            "pydantic"
        ]
        if self.settings.orm_choice == "SQLAlchemy":
            requirements.append("SQLAlchemy")
        elif self.settings.orm_choice == "SQLModel":
            requirements.append("SQLModel")

        if self.settings.db_choice == "PostgreSQL":
            requirements.append("psycopg2")
        elif self.settings.db_choice == "MySQL":
            requirements.append("mysql-connector-python")
        elif self.settings.db_choice == "MariaDB":
            requirements.append("mariadb")

        # Add Alembic if the user opted for it
        if self.settings.use_alembic:
            requirements.append("alembic")

        with open(f"{self.settings.project_name}/requirements.txt", "w") as f:
            f.write("\n".join(requirements))
