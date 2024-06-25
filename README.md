# Airflow DAGs and Data Pipelines

This repository contains various Data Pipelines and DAGs that I have developed and worked with using Apache Airflow. The setup also leverages Docker for containerized deployment.

## Overview

This repository showcases various data pipelines implemented using Apache Airflow. The pipelines are containerized using Docker for ease of deployment and management.

## Directory Structure

```plaintext
├── dags
│   ├── my_dag.py
│   └── podcast_summary.py
├── logs
├── plugins
├── docker-compose.yml
├── Dockerfile
└── README.md
```
# Getting Started
## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

    Docker
    Docker Compose

## Installation

    ### Clone the repository:

    sh

git clone https://github.com/tharrun-source/data-pipelines
cd your-repo-name

Build the Docker image and start the Airflow services using Docker Compose:

sh

    docker-compose up --build

## Running Airflow

After running the docker-compose up --build command, Airflow services should start, and you can access the Airflow web interface by navigating to http://localhost:8080 in your web browser.

    Username: airflow
    Password: airflow

### DAGs

This repository includes the following DAGs:

    [] my_dag.py: A sample DAG to demonstrate the structure and components of an Airflow DAG.
    [] podcast_summary.py: Podcast summary automates the retrieval and analysis of podcast episodes, leveraging Airflow and Docker for efficient data processing and management.

Each DAG is defined in a separate Python file within the dags/ directory.
Tools and Technologies

    Apache Airflow: An open-source tool for orchestrating complex data workflows.
    Docker: A platform for developing, shipping, and running applications in containers.
    Docker Compose: A tool for defining and running multi-container Docker applications.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

    Fork the repository.
    Create your feature branch (git checkout -b feature/your-feature-name).
    Commit your changes (git commit -m 'Add some feature').
    Push to the branch (git push origin feature/your-feature-name).
    Open a pull request.

# License

This project is licensed under the GNU LESSER License - see the LICENSE file for details.
Acknowledgements

    Thanks to the Apache Airflow community for their continuous development and support.
    Inspired by numerous open-source contributions and examples.
