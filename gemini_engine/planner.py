import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "your-api-key-here":
    raise ValueError("❌ GEMINI_API_KEY not set in .env file!")

genai.configure(api_key=API_KEY)


class Planner:
    
    
    @staticmethod
    def plan_experiments(model_info, current_performance):
        """Plan next experiments"""
        try:
            prompt = f"""
You are an ML researcher. Plan experiments to improve this model:

MODEL: {model_info}
CURRENT PERFORMANCE: {current_performance}

Suggest 3 experiments to try next:
1. Experiment name
2. What to change
3. Expected result

Be practical and prioritize by impact.
"""
            
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            
            return {
                "status": "success",
                "plan": response.text
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
