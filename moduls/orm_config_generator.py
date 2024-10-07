from moduls.config_generator import ConfigGenerator

class ORMConfigGenerator(ConfigGenerator):
    def _generate_base_config(self):
        db_url = self._get_database_url()
        return f"""
# ORM-specific config

class Settings:
    ENVIRONMENT = 'development'
    DEBUG = True

    # Database configurations
    DATABASE_URL = "{db_url}"

# Explanation of how to adapt the database connection parameters:
# - Replace 'user' with your database username.
# - Replace 'password' with your database password.
# - Replace 'localhost' with your database host.
# - Replace '5432' with your database port (default for PostgreSQL).
# - Replace 'mydatabase' with the name of your database.
"""

    def _get_database_url(self):
        db_type = self.settings.db_choice
        if db_type == "PostgreSQL":
            return "postgresql://user:password@localhost:5432/mydatabase"
        elif db_type == "MySQL":
            return "mysql://user:password@localhost:3306/mydatabase"
        elif db_type == "MariaDB":
            return "mariadb://user:password@localhost:3306/mydatabase"
        else:
            return "sqlite:///./test.db"