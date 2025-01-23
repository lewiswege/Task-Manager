async function fetchTasks() {
    const response = await fetch('/tasks');
    const tasks = await response.json();
    renderTasks(tasks);
}

async function addTask(title, due_date) {
    await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, due_date })
    });
    fetchTasks();
}

async function deleteTask(taskId) {
    await fetch(`/tasks/${taskId}`, { method: 'DELETE' });
    fetchTasks();
}

function renderTasks(tasks) {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';
    for (const [id, task] of Object.entries(tasks)) {
        const taskDiv = document.createElement('div');
        taskDiv.className = 'task';
        taskDiv.innerHTML = `${task.title} (Due: ${task.due_date}) <button onclick="deleteTask('${id}')">Delete</button>`;
        taskList.appendChild(taskDiv);
    }
}

document.getElementById('task-form').addEventListener('submit', (event) => {
    event.preventDefault();
    const title = document.getElementById('task-title').value;
    const due_date = document.getElementById('task-due-date').value;
    addTask(title, due_date);
    event.target.reset();
});

fetchTasks();