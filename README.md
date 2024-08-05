# Flask Chat App

## Overview

The **Flask Chat App** is a real-time chat application built using Flask. It supports user authentication, chat room creation, message posting, and file uploads. The app utilizes Flask-Login for user management, SQLAlchemy for database operations, and Jinja2 for templating.

## Features

- **User Authentication:** Sign up, log in, and manage user profiles.
- **Chat Rooms:** Create, view, and delete chat rooms.
- **Messaging:** Post text messages and upload files in chat rooms.
- **User Management:** Update user information and profile pictures.

## Requirements

- Python 3.11
- Flask
- Flask-Login
- SQLAlchemy
- Gunicorn (for production)

## Installation

### Setting Up the Environment

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/flask-chat-app.git
   cd flask-chat-app
   ```

2. **Run the setup script to create a virtual environment and install dependencies:**

   ```bash
   ./setup.sh
   ```

### Configuration

Update the `config.py` file with your database and application settings.

## Running the Application

### Development

1. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

2. **Run the Flask development server:**

   ```bash
   flask run
   ```

### Production

1. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

2. **Run the Gunicorn server:**

   ```bash
   ./run.sh
   ```

   **For background execution:**

   ```bash
   ./run.sh -d
   ```

## Project Structure

```
flask-chat-app/
├── website/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── chat.py
│   ├── api.py
│   ├── config.py
│   ├── database.py
│   ├── functions.py
│   └── wsgi.py
├── setup.sh
├── run.sh
└── requirements.txt
```

- **`website/static/`**: Static files (CSS, JavaScript, images).
- **`website/templates/`**: HTML templates.
- **`website/__init__.py`**: Initializes the Flask application.
- **`website/chat.py`**: Chat-related routes.
- **`website/api.py`**: API endpoints.
- **`website/config.py`**: Configuration settings.
- **`website/database.py`**: Database models and manager.
- **`website/functions.py`**: Utility functions.
- **`website/wsgi.py`**: WSGI entry point for Gunicorn.
- **`setup.sh`**: Script to set up the environment.
- **`run.sh`**: Script to run the application.
- **`requirements.txt`**: Python dependencies.

## Routes

### Chat

- **`GET /`**: Redirects to the home page.
- **`GET /home`**: Displays chat rooms.
- **`GET /room/<room_id>`**: Displays a specific chat room.
- **`GET /room-detailed/<room_id>`**: Displays detailed information about a chat room.

### API

- **`POST /submit-chat-message/<room_id>`**: Submits a chat message.
- **`POST /create-chat-room`**: Creates a new chat room.
- **`POST /delete-chat-room/<room_id>`**: Deletes a chat room.
- **`POST /alter-user-information/<user_id>`**: Updates user information.
- **`POST /alter-user-profile-picture/<user_id>`**: Updates user profile picture.
- **`POST /login-user`**: Logs in a user.
- **`POST /signup-user`**: Signs up a new user.
- **`POST /alter-user-password/<user_id>`**: Changes user password.
- **`POST /delete-file/<file_name>`**: Deletes a file from the server.

## Usage

1. **Sign Up**: Create a new account.
2. **Log In**: Log into your account.
3. **Create Chat Room**: Navigate to the home page and create a new chat room.
4. **Post Messages**: Enter a chat room and post messages or upload files.
5. **Manage Profile**: Update your user information and profile picture.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License.

---

## Scripts Explanation

### setup.sh

This script sets up the project environment by creating a virtual environment, installing required packages, and configuring the project for development.

```bash
#!/bin/bash

cd ..

python3.11 -m venv venv
source venv/bin/activate
python -m pip install -U pip

cd website

python -m pip install -r requirements.txt
```

### run.sh

This script runs the application using Gunicorn. It can start the server either in the foreground or as a background process.

```bash
#!/bin/bash

cd ..
source venv/bin/activate
export FLASK_APP=website
export FLASK_DEBUG=1
cd website

if [[ "$#" -eq 0 ]]; then
    gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
elif [[ "$1" == "-d" ]]; then
    gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app &
else
    echo "Invalid option: $1"
    echo "Usage: ./run.sh [-d]"
fi
```

By following this README, you should be able to set up, configure, and run the Flask Chat App both in development and production environments. For any issues or further assistance, feel free to contact the project maintainers.


## Credits

Created By: Tre Brown  
LinkedIn: [www.linkedin.com/in/trebrown100](https://www.linkedin.com/in/trebrown100)  
Contact: [trebrown2238@gmail.com](mailto:trebrown2238@gmail.com)
