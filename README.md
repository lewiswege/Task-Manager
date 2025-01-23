# Task Manager App

## Overview
The Task Manager App is a simple web application for managing tasks, featuring a FastAPI backend and a JavaScript-based frontend. Tasks are stored persistently in a JSON file. Users can add, view, and delete tasks via the web interface.

---

## Features
- **Add Tasks:** Users can add tasks with a title and a due date.
- **View Tasks:** The app displays all saved tasks in a clean, organized layout.
- **Delete Tasks:** Users can remove tasks they no longer need.
- **Persistent Storage:** Tasks are saved in a `tasks.json` file, ensuring data is retained across app restarts.

---

## Project Architecture
```
task-manager-app/
|
├── app/                 # Backend application files
|   ├── __init__.py      # (Optional) Init file for the backend module
|   ├── main.py          # FastAPI backend server file
|   ├── tasks.json       # JSON file to store tasks persistently
|
├── static/              # Static files for the frontend (HTML, CSS, JS)
|   ├── index.html       # Main HTML file for the UI
|   ├── styles.css       # CSS file for styling
|   └── script.js        # JavaScript for frontend logic
|
└── templates/           # (Optional) Templating folder (not used in this app)
```

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd task-manager-app
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

---

## Running the Application
1. Start the FastAPI backend:
   ```bash
   uvicorn app.main:app --reload
   ```
2. Open your web browser and go to:
   ```
   http://127.0.0.1:8000

   ## Usage
1. **Add Tasks:**
   - Fill in the "Task Title" and "Due Date" fields in the web interface.
   - Click the "Add Task" button to save the task.

2. **View Tasks:**
   - All tasks are displayed in the "Task List" section.

3. **Delete Tasks:**
   - Click the "Delete" button next to a task to remove it.

---

## Communication Flow
1. **Frontend (HTML/JS):** Sends HTTP requests (`GET`, `POST`, `DELETE`) to FastAPI endpoints.
2. **Backend (FastAPI):** Processes these requests, interacts with `tasks.json`, and sends JSON responses back.
3. **Data Flow:**
   - User actions trigger JavaScript functions.
   - JavaScript communicates with FastAPI endpoints.
   - FastAPI handles data in `tasks.json` and updates the UI dynamically.

---

## Example API Endpoints
- `GET /tasks`: Retrieve all tasks.
- `POST /tasks`: Add a new task.
- `DELETE /tasks/{task_id}`: Delete a task by ID.

---

## Future Enhancements
- Implement task editing.
- Add user authentication.
- Migrate from JSON storage to a database.
- Improve UI with advanced frameworks like React or Vue.js.