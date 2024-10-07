from moduls.project_settings import ProjectSettings
from moduls.scaffolding_generator import ScaffoldingGenerator
from moduls.config_generator import ConfigGenerator
from moduls.orm_config_generator import ORMConfigGenerator
from moduls.docker_generator import DockerGenerator
from moduls.requirements_generator import RequirementsGenerator
from moduls.user_input_collector import UserInputCollector

class ProjectGenerator:
    def __init__(self):
        self.settings = ProjectSettings()

    def run(self):
        # Collect user inputs
        input_collector = UserInputCollector(self.settings)
        input_collector.collect_user_inputs()

        # Generate project scaffolding
        scaffold_generator = ScaffoldingGenerator(self.settings)
        scaffold_generator.generate_structure()

        # Generate Dockerfile and docker-compose.yml
        docker_generator = DockerGenerator(self.settings)
        docker_generator.generate_dockerfile()
        docker_generator.generate_docker_compose()

        # Generate configuration
        config_generator = self._create_config_generator()
        config_generator.generate_config()

        # Generate requirements.txt
        requirements_generator = RequirementsGenerator(self.settings)
        requirements_generator.generate_requirements()

        print("Project scaffolding, Docker configuration, and requirements generated successfully!")

    def _create_config_generator(self):
        if self.settings.orm_choice:
            return ORMConfigGenerator(self.settings)
        else:
            return ConfigGenerator(self.settings)

if __name__ == "__main__":
    generator = ProjectGenerator()
    generator.run()
