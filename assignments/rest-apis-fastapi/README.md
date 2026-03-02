# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, production-ready REST APIs using the FastAPI framework. You'll create a web service with multiple endpoints, request/response validation, and proper HTTP status codes. This assignment teaches you web development fundamentals, API design principles, and how to structure backend applications that can be consumed by frontend clients.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project and Create Basic Endpoints

#### Description
Initialize a FastAPI project with proper project structure and create foundational endpoints to handle HTTP requests.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn dependencies
- Create a main application file with FastAPI instance initialization
- Implement a GET endpoint that returns a welcome message
- Implement a simple GET endpoint with a path parameter
- Create a GET endpoint that returns a list of items in JSON format
- Run the server successfully using uvicorn


### 🛠️ Add Request Validation and POST Endpoints

#### Description
Implement endpoints that accept request data, validate input using Pydantic models, and perform create operations.

#### Requirements
Completed program should:

- Define a Pydantic model for request/response data structure
- Create a POST endpoint that accepts JSON data
- Validate incoming data types and required fields
- Return proper HTTP status codes (201 for creation, 400 for bad requests)
- Store or process submitted data appropriately
- Return the created resource with all necessary details


### 🛠️ Implement Full CRUD Operations and Error Handling

#### Description
Add remaining CRUD operations (Read, Update, Delete) with proper error handling and realistic data management.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve a specific item by ID
- Implement PUT/PATCH endpoint to update existing resources
- Implement DELETE endpoint to remove resources
- Return 404 status code when requested resource doesn't exist
- Include meaningful error messages in responses
- Handle edge cases like invalid IDs or missing data
- Store data in a simple data structure (list or dictionary) for persistence during runtime
