from enum import Enum

class DatabaseOption(Enum):
    MySQL = 1
    MariaDB = 2
    PostgreSQL = 3

class ORMOption(Enum):
    SQLAlchemy = 1
    SQLModel = 2

class UserInputCollector:
    def __init__(self, settings):
        self.settings = settings

    def collect_user_inputs(self):
        self.settings.project_name = input("Enter the project name: ")

        # Ask if the user wants to use a relational database
        use_db = input("Are you going to use a relational database? (y/n): ").lower() == 'y'
        if use_db:
            self._collect_database_inputs()

            # Ask if the user wants to use an ORM only if a relational database is selected
            use_orm = input("Are you going to use an ORM? (y/n): ").lower() == 'y'
            if use_orm:
                self._collect_orm_inputs()

            # Ask if the user wants to use Alembic for database migrations
            use_alembic = input("Would you like to add Alembic for database migrations? (y/n): ").lower() == 'y'
            self.settings.use_alembic = use_alembic

        # Ask if the user wants API versioning
        self.settings.versioning = input("Would you like to use API versioning? (y/n): ").lower() == 'y'

        # Only ask if the models will be inside the versioning folder if versioning is enabled
        if self.settings.versioning:
            self.settings.models_inside_versioning = input("Would you like to place models inside the versioned folder? (y/n): ").lower() == 'y'

    def _collect_database_inputs(self):
        print("Which relational database are you going to use?")
        for db in DatabaseOption:
            print(f"{db.value}: {db.name}")
        db_choice = int(input("Enter the number of the relational database: "))

        if db_choice in [db.value for db in DatabaseOption]:
            self.settings.db_choice = DatabaseOption(db_choice).name
        else:
            print("Invalid choice, please select a valid number.")
            self._collect_database_inputs()

    def _collect_orm_inputs(self):
        print("Which ORM are you going to use?")
        for orm in ORMOption:
            print(f"{orm.value}: {orm.name}")
        orm_choice = int(input("Enter the number of the ORM: "))

        if orm_choice in [orm.value for orm in ORMOption]:
            self.settings.orm_choice = ORMOption(orm_choice).name
        else:
            print("Invalid choice, please select a valid number.")
            self._collect_orm_inputs()
