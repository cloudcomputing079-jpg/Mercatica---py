import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load your Gemini API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyArNoYwRiCUxgz-VKA8FcMVwRbHojJ3VfI"))

def extract_section(text, keyword):
    lines = text.split('\n')
    for line in lines:
        if keyword.lower() in line.lower():
            return line.split(':', 1)[-1].strip()
    return "Not found"

def generate_branding_kit(store_name, Domain):
    prompt = f"""
    Create branding for a store named '{store_name}' in the '{Domain}' domain.
    Include:
    - Tagline
    - Color palette
    - Logo ideas
    """

    try:
       model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
       response = model.generate_content(prompt)
       text = response.text
       return {
            'tagline': extract_section(text, "Tagline"),
            'colors': extract_section(text, "Color"),
            'logo_ideas': extract_section(text, "Logo")
        }

    except Exception as e:
        return {
            'tagline': f'Error: {str(e)}',
            'colors': 'Please check your Gemini API key or usage.',
            'logo_ideas': 'Visit https://ai.google.dev for details.'
        }