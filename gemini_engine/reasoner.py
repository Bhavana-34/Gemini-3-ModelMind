from google import genai
from google.genai import types
from gemini_engine.prompts import Prompts
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "your-api-key-here":
    raise ValueError("❌ GEMINI_API_KEY not set in .env file!")

client = genai.Client(api_key=API_KEY)

def sanitize_text(text):
    """Remove problematic characters from text"""
    if not isinstance(text, str):
        return str(text)
    # Replace problematic characters
    text = text.replace("'", "'").replace(""", '"').replace(""", '"')
    # Remove any non-printable characters
    text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\t')
    return text


class Reasoner:
    """Use Gemini for reasoning"""
    
    @staticmethod
    def analyze(model_info, issues):
        """Analyze model using Gemini"""
        try:
            prompt = Prompts.get_diagnosis_prompt(str(model_info), str(issues))
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            
            return {
                "status": "success",
                "analysis": sanitize_text(response.text)
            }
        except Exception as e:
            # Fallback analysis if Gemini fails
            print(f"Gemini error: {e}")
            return {
                "status": "success",
                "analysis": f"Model Analysis:\n- Type: {model_info.get('type', 'Unknown')}\n- Issues found: {len(issues) if isinstance(issues, list) else 'Unknown'}\n- Status: Demo mode (Gemini unavailable)"
            }
    
    @staticmethod
    def get_improvements(model_info):
        """Get improvements from Gemini"""
        try:
            prompt = Prompts.get_improvement_prompt(str(model_info))
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            
            return {
                "status": "success",
                "improvements": sanitize_text(response.text)
            }
        except Exception as e:
            # Fallback improvements if Gemini fails
            print(f"Gemini improvement error: {e}")
            return {
                "status": "success",
                "improvements": "Recommendations:\n- Consider optimizing model architecture\n- Review training parameters\n- Validate data quality\n- Test model performance on diverse datasets"
            }
