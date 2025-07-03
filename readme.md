# 🎬 Marvel Movie Explorer – Backend & Frontend

This project provides a full-stack interface to explore data about Marvel actors, movies, and characters.  
It includes a **FastAPI** backend and a **React** frontend.
---

## 🚀 Tech Stack

### Backend (Python):
- **Python 3.11**
- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **PostgreSQL** – Database
- **Pydantic** – Validation
- **Uvicorn** – ASGI server
- **Pytest** – Testing framework

### Frontend (JavaScript):
- **React**
- **Axios** – HTTP client
- **Vite** – Development server

---
## DOCS 
docs/marvel_tests.png  
docs/mervel_app_logs.png
docs/swagger.png

## 📁 Project Structure

MOVIES
├── backend/
│ ├── app/
│ │ ├── controllers/ # Business logic layer
│ │ ├── services/ # Data transformation / filtering
│ │ ├── dal/ # Data access layer (raw SQL + ORM)
│ │ ├── routes/ # API route definitions
│ │ ├── models/ # SQLAlchemy models
│ │ ├── schemas/ # Pydantic response schemas
│ │ └── main.py # App entrypoint
│ ├── tests/ # Pytest test cases
│ ├── requirements.txt # Backend dependencies
│ └── .env # Environment variables
├── frontend/ # React app
└── README.md # You're here


---

## ▶️ How to Run – Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```


🗃️ Populate the Database

After setting up the backend and installing the requirements, you can populate the PostgreSQL database with Marvel movie data by running the following script:
```
cd backend
python -m app.scripts.fetch_and_store
```


## 📘 API Overview

API available at: http://localhost:8000

Interactive docs: http://localhost:8000/docs

| Method | Endpoint                               | Description                                  |
| ------ | -------------------------------------- | -------------------------------------------- |
| GET    | `/api/movies-per-actor`                | Paginated list of actors with movies & roles |
| GET    | `/api/actors-with-multiple-characters` | Actors who played more than one character    |
| GET    | `/api/characters-with-multiple-actors` | Characters played by more than one actor     |


## ▶️ How to Run – Frontend (React)
cd frontend
npm install
npm run dev

App runs on: http://localhost:3000




## 📌 Assumptions & Notes
Pagination is only supported for /movies-per-actor
→ Because it's the only endpoint that returns potentially large datasets, and it's a limited project just an MVP.
This decision fits the limited scope of the assignment.

The .env file must include valid PostgreSQL credentials.

Logging uses Python’s built-in logging module. No external log collector was connected.

Semantic HTTP status codes are used across all endpoints for clarity (e.g., 422, 404, 201, 200).

Focus was given to clean architecture, code separation by responsibility, and readability.

Testing is done using Pytest under the /backend/tests/ folder.

The frontend was built to serve basic presentation needs only – focused on displaying data, without advanced UI/UX features.
The system is **read-only** by design – no Create/Update/Delete (CRUD) operations were implemented, as they were not required in the assignment and since it's a limited project.
No indexing was added to the PostgreSQL database – further optimization would be needed for larger-scale datasets.

## ✅ Run Backend Tests
cd backend
pytest tests

