import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "your-api-key-here":
    raise ValueError("❌ GEMINI_API_KEY not set in .env file!")


class Prompts:
    """Store Gemini prompts"""
    
    @staticmethod
    def get_diagnosis_prompt(model_info, issues):
        """Get diagnosis prompt"""
        return f"""
You are an ML expert. Analyze this model and its issues:

MODEL: {model_info}
ISSUES FOUND: {issues}

Provide:
1. Root cause analysis
2. Specific fixes
3. Expected improvements

Keep response concise and actionable.
"""
    
    @staticmethod
    def get_improvement_prompt(model_info):
        """Get improvement prompt"""
        return f"""
You are an ML optimization expert. Suggest improvements for:

MODEL: {model_info}

Provide top 3 improvements with:
1. What to change
2. Why it helps
3. Expected impact

Be specific and practical.
"""
