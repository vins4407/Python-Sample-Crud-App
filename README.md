# FastAPI CRUD App with PyMongo

This repository contains the source code for a CRUD (Create, Read, Update, Delete) application built with FastAPI and PyMongo, connected to a MongoDB database. This application provides a RESTful API that can be used to perform CRUD operations on a collection of notes.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Running the Application Locally](#running-the-application-locally)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running the application, ensure that you have the following prerequisites installed:

- Python 3.7+
- MongoDB server or Docker
- FastAPI and PyMongo dependencies (see `requirements.txt`)
- Frontend app dependencies (if running frontend locally)

## Running the Application Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/wpcodevo/crud-app-pymongo.git
Navigate to the project directory:
bash
Copy code
cd crud-app-pymongo
Set up a virtual environment (optional but recommended):
bash
Copy code
python -m venv venv
# Activate the virtual environment
# Windows
venv\Scripts\activate.bat
# Linux/Mac
source venv/bin/activate
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Start the MongoDB server (if not using Docker):
bash
Copy code
# Start MongoDB server locally or use Docker
Run the FastAPI server:
bash
Copy code
uvicorn app.main:app --reload
(Optional) Run the frontend app locally (if applicable):
bash
Copy code
# Instructions to run frontend app
Project Structure
The project structure is as follows:

bash
Copy code
├── app
│   ├── main.py        # FastAPI application setup
│   ├── database.py    # MongoDB connection setup
│   ├── note.py        # CRUD operations for notes
│   ├── schemas.py     # Pydantic schemas for validation
│   └── note_serializers.py  # Data serialization functions
├── tests              # Test files (if available)
├── .env               # Environment variables
└── README.md          # Project README file
API Endpoints
The application provides the following API endpoints:

GET /api/notes: Retrieve all notes
POST /api/notes: Create a new note
GET /api/notes/{noteId}: Get a single note
PATCH /api/notes/{noteId}: Edit a note
DELETE /api/notes/{noteId}: Remove a note
For detailed documentation on each endpoint, refer to the Swagger UI or OpenAPI documentation provided by FastAPI.

Contributing
Contributions to this project are welcome. Please follow the guidelines outlined in the CONTRIBUTING.md file.

License
This project is licensed under the MIT License.

# Python-Sample-Crud-App
# Python-Sample-Crud-App