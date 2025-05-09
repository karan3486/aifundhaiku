import os
import datetime
from pymongo import MongoClient
from openai import OpenAI
from dotenv import load_dotenv
import httpx
# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), http_client=httpx.Client())
class HaikuService:
    def __init__(self):
        """
        Initialize the HaikuService with MongoDB and OpenAI connections
        """
        # Set up MongoDB connection
        mongo_uri = os.getenv('MONGO_URI')
        self.client = MongoClient(mongo_uri)
        self.db = self.client.haiku_db
        self.haiku_collection = self.db.haikus
        
    
    def generate_haiku(self, prompt):
        """
        Generate a haiku using the OpenAI API based on the given prompt
        """
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a haiku poet. Create a beautiful three-line haiku following the traditional 5-7-5 syllable pattern."},
                    {"role": "user", "content": f"Write a haiku about {prompt}"}
                ],
                max_tokens=100,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating haiku: {e}")
            return "Could not generate haiku.\nPlease try again later.\nError occurred."
    
    def save_haiku(self, prompt, text):
        """
        Save a haiku to the MongoDB database
        """
        haiku_data = {
            'prompt': prompt,
            'text': text,
            'created': datetime.datetime.now()
        }
        
        try:
            self.haiku_collection.insert_one(haiku_data)
            return True
        except Exception as e:
            print(f"Error saving haiku: {e}")
            return False
    
    def get_recent_haikus(self, limit=20):
        """
        Get the most recent haikus from the database
        """
        try:
            haikus = list(self.haiku_collection.find().sort('created', -1).limit(limit))
            return haikus
        except Exception as e:
            print(f"Error retrieving haikus: {e}")
            return []
