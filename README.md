
# Simple Blogging Platform

This is a simple blogging platform built using Django. It allows users to register, log in, and create, edit, and delete blog posts. The platform also allows users to view a list of all blog posts and read individual posts.

## Features

- **User Authentication**
  - Users can register, log in, and log out.
  - Django’s built-in authentication system is used for handling user authentication.
  
- **Blog Post Management**
  - Users can create, edit, and delete their own blog posts.
  - Each blog post has a title, content, timestamp, and author (user).
  
- **View Blog Posts**
  - All users (including non-authenticated users) can view a list of all blog posts.
  - Users can view individual blog posts.

## Requirements

- Python 3.8 or higher
- Django 3.x
- MongoDB or MySQL (depending on your choice)

## Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/Ajith-te/blog.git
```

### 2. Navigate to the project directory

```bash
cd blog
```

### 3. Set up a virtual environment

It is recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install dependencies

Install the required packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 5. Configure Database

- If you are using **MongoDB**, make sure it is running on your machine or configure it in the `settings.py` file.
- If you are using **MySQL**, configure your database in the `settings.py` file.

### 6. Apply database migrations

Run the following command to apply all migrations and set up the database:

```bash
python manage.py migrate
```

### 7. Create a superuser

To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

### 8. Start the development server

Now, you can start the Django development server:

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.


## Usage

### Authentication:
- Users can **register**, **login**, and **logout** from the platform.
  
### Blog Post Management:
- Users can **create**, **edit**, and **delete** their own blog posts after logging in.
  
### View Blog Posts:
- All users can view a list of blog posts, and non-authenticated users can read individual posts.

## Folder Structure

- `blog/`: The main project directory.
  - `app/`: The app for managing blog posts.
    - `migrations/`: Database migrations.
    - `models.py`: Defines the database models.
    - `views.py`: Handles the logic for displaying blog posts.
    - `templates/`: Contains HTML files for the frontend.
  - `isolve_task/settings.py`: Main Django project settings.
  - `isolve_task/urls.py`: URL routing for the project.
  - `manage.py`: Django's command-line utility for managing the project.

## Technologies Used

- **Django**: The web framework for building the platform.
- **HTML/CSS**: For rendering and styling the pages.
- **MongoDB or MySQL**: Database for storing users and blog posts.
- **Bootstrap** (optional): For better styling and UI.

## Contributing

1. Fork the repository.
2. Create your branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
