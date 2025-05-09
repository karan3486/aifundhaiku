# Haiku Generator

A Flask web application that generates haikus based on user prompts using OpenAI's API and stores them in MongoDB.

## Features

- Generate three-line haikus from user prompts using OpenAI's API
- Store generated haikus in MongoDB Atlas
- Display the 20 most recent haikus
- Clean, responsive user interface

## Setup Instructions

### Prerequisites

- Python 3.7+
- MongoDB Atlas account
- OpenAI API key

### Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Rename `.env.example` to `.env`
   - Add your MongoDB connection string and OpenAI API key:
     ```
     MONGO_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net/haiku_db
     OPENAI_API_KEY=your_openai_api_key
     ```

### Running the Application

Run the application with:
```
python app.py
```

The application will be available at http://localhost:5000

## Project Structure

```
haiku/
├── app.py                  # Main application file
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (not committed to version control)
├── controllers/            # Route handlers
│   ├── __init__.py
│   └── haiku_controller.py # Haiku routes
├── services/               # Business logic
│   ├── __init__.py
│   └── haiku_service.py    # Haiku generation and database operations
├── templates/              # HTML templates
│   └── index.html          # Main page template
└── static/                 # Static assets (CSS, JS, images)
```

## Technologies Used

- Flask: Web framework
- OpenAI API: Haiku generation
- MongoDB Atlas: Database for storing haikus
- Python-dotenv: Environment variable management
