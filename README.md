# Blog Api Application - Django Blog API

## Overview
Django Blog API is a robust web application developed using Django and Django REST Framework, designed to provide users with seamless management and publication of blog content through an intuitive API interface.


## Demo
1. **AuthUserApi published documentation**
https://documenter.getpostman.com/view/29592036/2sA3JDhkM4

2. **BlogApi published documentation**
https://documenter.getpostman.com/view/29592036/2sA3JDimFH


## Features

1. **Token-Based Authentication:**
   - Ensures secure access to API endpoints with token authentication.
   - Includes forgot password and reset password functionalities via email for enhanced security.

2. **Category Management:**
   - Admin users can create and manage blog categories for efficient content organization.

3. **Blog Management**
   - Enables users to create, edit, list, and delete blog posts effortlessly.
   - Automatically assigns authors to blog posts, simplifying content management.

4. **Comment Functionality**
   - Allows users to engage with blog posts by commenting on them..

5. **Advanced Features::**
   - Implements throttling, filtering, and pagination for improved performance and user experience.
   - Tested endpoints using Postman for seamless integration and functionality verification.

## Getting Started

### Prerequisites
- Docker installed on your machine. You can download and install Docker from [here](https://www.docker.com/get-started).


### Using Postman for API Testing:

1. **Install Postman:** If you haven't already, download and install Postman from [https://www.postman.com/downloads/](https://www.postman.com/downloads/).

2. **Download API Collection:**
   - Download the API collection file provided in this repository: [API Collection](path/to/your/api/collection.json).

3. **Import API Collection:**
   - Open Postman and click on the "Import" button in the top-left corner.
   - Select the downloaded collection file to import it into Postman.

### Installation with Docker
To run the application using Docker, follow these steps:

1. Clone the repository:
   - git clone https://github.com/Kajal-Yadav31/BlogAPIapplication.git
2. Navigate to the project directory:
   - cd BlogAPIapplication
3. Build the Docker image:
   - docker build -t  BlogApp.
4. Run the Docker container:
   - docker run -d -p 8000:8000 BlogApp

### Usage
- Access the application at `http://localhost:8000/` in your web browser.
- Register an account, verify your email, and start creating your posts.
- Explore the features such as blog create, updating and delete.

## License
This project is licensed under the [MIT License]


## Contact
For inquiries or issues, contact [kajalyadav3107@gmail.com].


