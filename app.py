from flask import Flask
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Import routes after app is created to avoid circular imports
from controllers.haiku_controller import haiku_blueprint

# Register blueprints
app.register_blueprint(haiku_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
