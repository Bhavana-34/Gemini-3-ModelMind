import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "your-api-key-here":
    raise ValueError("❌ GEMINI_API_KEY not set in .env file!")

genai.configure(api_key=API_KEY)


class Reviewer:
    """Review and validate analysis"""
    
    @staticmethod
    def review_analysis(analysis_text):
        """Review analysis quality"""
        try:
            prompt = f"""
Review this ML analysis and rate its quality:

ANALYSIS:
{analysis_text}

Provide:
1. Quality score (1-10)
2. Key strengths
3. Missing information
4. Recommendations for improvement
"""
            
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            
            return {
                "status": "success",
                "review": response.text
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    @staticmethod
    def validate_fixes(fixes_text):
        """Validate proposed fixes"""
        try:
            prompt = f"""
Review these proposed model fixes:

FIXES:
{fixes_text}

For each fix, check if it:
- Makes technical sense
- Is implementable
- Will likely improve the model

Provide feedback on each fix.
"""
            
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            
            return {
                "status": "success",
                "validation": response.text
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
