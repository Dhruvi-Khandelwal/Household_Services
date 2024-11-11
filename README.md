# Household Services

A web application designed to connect customers with professionals offering household services such as AC repairs, cleaning, salon services, and electrical work. This app provides a platform where users can view available service packages, book appointments, and track service history.

## Features

- **User Dashboard**: Customers and professionals have separate dashboards with tailored functionalities.
- **Service Categories**: Browse different service categories like AC Repair, Salon, Cleaning, Electrician, etc.
- **Service Packages**: View available service packages with ratings, prices, and descriptions.
- **Service History**: Customers can view and manage their service history.
- **Login & Registration**: Separate authentication for users and professionals.
- **Admin Panel**: Admins can manage the platform, including user data and service details.

## Technologies Used

- **Flask**: A micro web framework for building web applications.
- **SQLite**: Lightweight database used for storing user and service data.
- **SQLAlchemy**: ORM for interacting with the database.
- **Flask-Migrate**: For handling database migrations.
- **Bootstrap 5**: For styling and responsive layout.
- **JavaScript**: For dynamic content like package listings.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Jinja2
- Gunicorn (for production deployment) #to be decided soon
  
### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Household_Services.git
    cd Household_Services
    ```

2. Create and activate a virtual environment:
    - **macOS/Linux**:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - **Windows**:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. Run the development server:
    ```bash
    flask run
    ```

    The app should be available at `http://127.0.0.1:5000`.

## Usage

- **Customer**:
    - Register an account and log in to access the customer dashboard.
    - Browse available services, view packages, and book appointments.
    - View your service history and track ongoing requests.

- **Professional**:
    - Register as a professional and log in to access the professional dashboard.
    - View your service history, manage requests, and accept appointments.

- **Admin**:
    - Admins can manage the platform, including user data and service listings.

## Project Structure

Household_Services/ │ ├── app/ │ ├── init.py # Application factory │ ├── models.py # Database models │ ├── routes.py # Routes for customer and professional dashboards │ ├── templates/ # HTML templates │ ├── static/ # Static files like CSS, JS, images │ └── ... │ ├── migrations/ # Database migration files ├── config.py # Configuration settings ├── requirements.txt # Project dependencies ├── run.py # Entry point to run the application └── README.md # Project documentation


## Database Setup

- **SQLite**: The app uses SQLite for simplicity, but you can switch to a different database (e.g., PostgreSQL) by modifying the `SQLALCHEMY_DATABASE_URI` in `config.py`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.



