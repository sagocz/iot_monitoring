# IoT Monitoring

A modular proof-of-concept application for collecting, processing, and visualizing IoT sensor data using modern cloud-ready technologies. The project is designed for easy deployment, reproducibility, and scalability — using Docker containers and microservice architecture.

## 🚀 Project Overview

**iot_monitoring** is a prototype IoT monitoring platform that simulates data from virtual sensors, forwards it to a backend API, and visualizes it in a user-friendly web interface. It is ideal for demonstrating skills in full-stack development, REST APIs, containerization, and working with time-series sensor data.

## ⚙️ Environment Requirements

To run the project locally, make sure you have the following tools installed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🛠️ Technologies Used

| Layer       | Technology        |
|-------------|-------------------|
| Backend API | FastAPI (Python)  |
| Sensor Sim  | Python (custom simulator) |
| Containerization | Docker, Docker Compose |
| Development | Git, GitHub, VSCode |
| (Planned) Frontend | React.js or lightweight static dashboard |
| (Planned) Database | PostgreSQL / MongoDB |
| (Planned) Cloud | AWS EC2 / ECS / RDS for deployment |

## 📈 Project Development Stages

Work is developed on the `development` branch. Each completed stage will be merged into `main` via Pull Requests.

| Stage | Description |
|-------|-------------|
| ✅ Stage 1 | Initial setup of sensor simulator and FastAPI backend, containerized with Docker |
| ✅ Stage 2 | Add database support (SQL - PostgreSQL) to store time-series sensor data. |
| ✅ Stage 3 | Implement basic frontend dashboard for live data preview |
| ⏳ Stage 4 | Add authentication and user roles (e.g., viewer, admin) |
| ⏳ Stage 5 | Deploy the app to AWS using ECS / EC2 / RDS |
| ⏳ Stage 6 | Add CI/CD (e.g., GitHub Actions) for automated testing and deployment |
| ⏳ Stage 7 | Add support for real industrial sensor inputs (Modbus/TCP or MQTT bridge) |

---

Feel free to clone, contribute, or fork this repository for learning or experimentation purposes.
