# Fastgen
FastAPI Project Generator

## Description

The **FastAPI Project Generator** simplifies the process of creating fully structured FastAPI projects with flexible configurations. This generator lets you choose:
- Relational databases (MySQL, MariaDB, PostgreSQL)
- ORM integration (SQLAlchemy or SQLModel)
- Docker setup with `Dockerfile` and `docker-compose.yml`
- API versioning and modular project structure

This tool is designed to speed up the development of FastAPI applications by automating the creation of project scaffolding, configuration files, and dependencies.

## Features

- **Customizable database support**: Choose between popular relational databases (MySQL, MariaDB, PostgreSQL).
- **ORM Integration**: Select SQLAlchemy or SQLModel for handling your database models.
- **Docker integration**: Automatically generate a `Dockerfile` and `docker-compose.yml` to containerize your application.
- **API Versioning**: Option to scaffold your FastAPI project with versioned APIs.
- **Modular project structure**: Organized into clearly defined modules using object-oriented programming (OOP) principles for scalability and maintainability.

## Requirements

- Python 3.8+
- Docker (optional, if you want to use Docker)

## Installation

Clone this repository and navigate to the project folder:
<pre>git clone https://github.com/yourusername/fastapi-project-generator.git
cd fastapi-project-generator</pre>

## Usage

Run the project generator script:
<pre>py main.py</pre>

The script will interactively guide you through setting up your FastAPI project by asking the following questions:

1. Project Name: Enter the name of your FastAPI project.
2. Relational Database: Choose between MySQL, MariaDB, or PostgreSQL. If you don't want a database, simply skip this step.
3. ORM: Select SQLAlchemy or SQLModel to manage your database models.
4. API Versioning: Decide whether you want versioned APIs.
5. Model Placement: Choose whether models should reside inside or outside the versioned folders.

Example

<pre>$ python project_generator.py
Enter the project name: my_fastapi_project
Are you going to use a relational database? (y/n): y
Which relational database are you going to use?
1: MySQL
2: MariaDB
3: PostgreSQL
Enter the number of the relational database: 3
Are you going to use an ORM? (y/n): y
Which ORM are you going to use?
1: SQLAlchemy
2: SQLModel
Enter the number of the ORM: 1
Would you like to use API versioning? (y/n): y
Would you like to place models inside the versioned folder? (y/n): n
</pre>

Once you complete the input, the generator will automatically create a FastAPI project with the chosen configuration.

## Generated Structure

Here’s an example of the generated project structure based on the inputs provided:

<pre>my_fastapi_project/
├── app/
│   ├── main.py
│   ├── v1/
│       └── routers/
├── config/
│   ├── settings.py
│   └── database.py (if ORM is used)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
</pre>

## Running the Generated Project

After the project is generated, you can install the dependencies and run the FastAPI application.

1. Install dependencies:
<pre>pip install -r requirements.txt
</pre>

2. Run the FastAPI app:
<pre>uvicorn app.main:app --reload
</pre>

3. Run with Docker:
<pre>docker-compose up --build
</pre>

This will start the FastAPI application and the database (if chosen) in separate containers.

## Contributing

Contributions are welcome! If you have any suggestions or want to report a bug, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
