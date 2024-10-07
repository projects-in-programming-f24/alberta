# Alberta API

This is a simple FastAPI application that provides a RESTful API for managing courses the Alberta database. It uses MongoDB as the database backend, but you could adapt this for SQL too.

## Features

- List all courses
- Get a specific course by ID
- Create a new course
- Update an existing course
- Delete a course

## Prerequisites

- Python 3.11
- MongoDB

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/nyu-course-api.git
   cd nyu-course-api
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your MongoDB URI:
   ```
   MONGODB_URI=your_mongodb_uri_here
   ```

## Running the Application

To run the application, use the following command:

```
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

- `GET /courses/`: List all courses
- `GET /courses/{course_id}`: Get a specific course
- `POST /courses/`: Create a new course
- `PUT /courses/{course_id}`: Update an existing course
- `DELETE /courses/{course_id}`: Delete a course

## API Documentation

Once the application is running, you can view the interactive API documentation by visiting:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`


## Testing with Postman
Postman is a popular tool for testing APIs. Here's how you can use it to test the NYU Course API:

Install Postman: If you haven't already, download and install Postman from https://www.postman.com/downloads/
Launch Postman: Open the Postman application.
Set up a new request:

1. Click on the "+" tab to create a new request.
2. Set the request type (GET, POST, PUT, DELETE) according to the endpoint you're testing.
3. Enter the request URL (e.g., http://localhost:8000/courses/)

### Testing endpoints:
a. GET all courses:

```
Method: GET
URL: http://localhost:8000/courses/
Click "Send"
```

b. GET a specific course:

```
Method: GET
URL: http://localhost:8000/courses/{course_id} (replace {course_id} with an actual ID)
Click "Send"
```

c. Create a new course:

```
Method: POST
URL: http://localhost:8000/courses/
Go to the "Body" tab, select "raw" and "JSON"
Enter the course data, e.g.:
jsonCopy{
    "code": "CS101",
    "title": "Introduction to Computer Science",
    "section_count": 3,
    "section_type": "lecture"
}

Click "Send"
```

d. Update a course:

```
Method: PUT
URL: http://localhost:8000/courses/{course_id} (replace {course_id} with an actual ID)
Go to the "Body" tab, select "raw" and "JSON"
Enter the updated course data
Click "Send"
```

e. Delete a course:
```
Method: DELETE
URL: http://localhost:8000/courses/{course_id} (replace {course_id} with an actual ID)
Click "Send"
```

Remember to start your FastAPI server before testing with Postman. If you encounter any issues, make sure your server is running and that you're using the correct URL and port.