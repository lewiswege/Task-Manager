<h1> Task Manager Web-App </h1>
<h2>A simple task manager application as my final project</h2>
    <p>This is a research project to improve my problem-solving and time-management skills</p>

<h3>Technologies Used</h3>
    <ol>
        FastAPI for the Back-End
        Fetch API for HTTP Requests
        HTML, CSS and JavaScript for the Front-End
        JSON for data storage
        Hash Table Data Structure
    </ol>

<p>The application allows users to add tasks to a task queue and delete them when they need to</p>

<p>The app uses API routes to perform CRUD operations, making the entire application work.</p>

<p>JavaScript is also incorporated in the app to handle the frontend logic using fetch API, which sends requests to localhost:8000; the port on which unicorn runs. This handles the request of the task queue and updates the UI dynamically whenever the user refreshes the Tasks or adds new ones to the queue</p>

<p>FastAPI is the technology that does all the magic, it handles the API endpoint and also handles the rendering of the application's UI</p>

<p>The application has limited features but does the basic job a Task Manager application does but its a fully fleded app with a front end UI, a database in json format, API calls and dynamic content</p>

<p>Clone the repo from your terminal move into the root of the repo and run the application through the following command</p>

<strong>uvicorn app.main:app --reload</strong>
