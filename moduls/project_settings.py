class ProjectSettings:
    """
    Singleton class to hold the project settings across the app.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ProjectSettings, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.project_name = None
        self.db_choice = None
        self.orm_choice = None
        self.versioning = False
        self.models_inside_versioning = False