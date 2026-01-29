import google.generativeai as genai
from gemini_engine.prompts import Prompts
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "your-api-key-here":
    raise ValueError("❌ GEMINI_API_KEY not set in .env file!")

genai.configure(api_key=API_KEY)


class Reasoner:
    """Use Gemini for reasoning"""
    
    @staticmethod
    def analyze(model_info, issues):
        """Analyze model using Gemini"""
        try:
            prompt = Prompts.get_diagnosis_prompt(str(model_info), str(issues))
            
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            
            return {
                "status": "success",
                "analysis": response.text
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    @staticmethod
    def get_improvements(model_info):
        """Get improvements from Gemini"""
        try:
            prompt = Prompts.get_improvement_prompt(str(model_info))
            
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            
            return {
                "status": "success",
                "improvements": response.text
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
