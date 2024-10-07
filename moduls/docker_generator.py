class DockerGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate_dockerfile(self):
        content = f"""
# Dockerfile for {self.settings.project_name}
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
        with open(f"{self.settings.project_name}/Dockerfile", "w") as f:
            f.write(content)

    def generate_docker_compose(self):
        db_service = ""
        if self.settings.db_choice == "PostgreSQL":
            db_service = """
  db:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"
"""
        elif self.settings.db_choice == "MySQL":
            db_service = """
  db:
    image: mysql
    environment:
      MYSQL_USER: user
      MYSQL_PASSWORD: password
      MYSQL_DATABASE: mydatabase
    ports:
      - "3306:3306"
"""
        elif self.settings.db_choice == "MariaDB":
            db_service = """
  db:
    image: mariadb
    environment:
      MYSQL_USER: user
      MYSQL_PASSWORD: password
      MYSQL_DATABASE: mydatabase
    ports:
      - "3306:3306"
"""

        content = f"""
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db{db_service}
"""
        with open(f"{self.settings.project_name}/docker-compose.yml", "w") as f:
            f.write(content)