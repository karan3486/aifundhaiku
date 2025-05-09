from flask import Flask
# from dotenv import load_dotenv
import os
# Load environment variables
# load_dotenv()

# Create Flask app
app = Flask(__name__)

# Import routes after app is created to avoid circular imports
from controllers.haiku_controller import haiku_blueprint

# Register blueprints
app.register_blueprint(haiku_blueprint)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
