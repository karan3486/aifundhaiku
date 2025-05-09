from flask import Blueprint, render_template, request, redirect, url_for
from services.haiku_service import HaikuService

# Create blueprint
haiku_blueprint = Blueprint('haiku', __name__)

# Initialize service
haiku_service = HaikuService()

@haiku_blueprint.route('/', methods=['GET'])
def index():
    """
    Display the homepage with the haiku form and past haikus
    """
    # Get the 20 most recent haikus
    recent_haikus = haiku_service.get_recent_haikus(20)
    return render_template('index.html', haikus=recent_haikus)

@haiku_blueprint.route('/generate', methods=['POST'])
def generate():
    """
    Generate a new haiku based on the provided prompt
    """
    prompt = request.form.get('prompt', '')
    
    if not prompt:
        return redirect(url_for('haiku.index'))
    
    # Generate haiku and save to database
    haiku_text = haiku_service.generate_haiku(prompt)
    haiku_service.save_haiku(prompt, haiku_text)
    
    # Redirect back to homepage to see the new haiku
    return redirect(url_for('haiku.index'))
