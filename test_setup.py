"""
Test script to verify ModelMind setup
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("ModelMind Setup Verification")
print("=" * 60)

# 1. Check Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")
if api_key and api_key != "your-api-key-here":
    print(f"✅ Gemini API Key found: {api_key[:10]}...{api_key[-4:]}")
else:
    print("❌ Gemini API Key missing or invalid in .env file")
    print("   Get your key from: https://makersuite.google.com/app/apikey")

# 2. Check required packages
print("\n" + "=" * 60)
print("Checking Required Packages")
print("=" * 60)

packages = {
    "google-genai": "google.genai",
    "streamlit": "streamlit",
    "fastapi": "fastapi",
    "uvicorn": "uvicorn",
    "tensorflow": "tensorflow",
    "torch": "torch",
    "pandas": "pandas",
    "numpy": "numpy",
    "plotly": "plotly",
    "python-dotenv": "dotenv",
    "pydantic": "pydantic"
}

missing_packages = []
for package_name, import_name in packages.items():
    try:
        __import__(import_name)
        print(f"✅ {package_name}")
    except ImportError:
        print(f"❌ {package_name} - Missing")
        missing_packages.append(package_name)

# 3. Test Gemini API
if api_key and api_key != "your-api-key-here":
    print("\n" + "=" * 60)
    print("Testing Gemini API Connection")
    print("=" * 60)
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents='Say hello in one word'
        )
        print(f"✅ Gemini API working! Response: {response.text[:50]}")
    except Exception as e:
        print(f"❌ Gemini API test failed: {str(e)}")
        if "API_KEY_INVALID" in str(e) or "invalid" in str(e).lower():
            print("   Your API key appears to be invalid")
            print("   Get a new key from: https://makersuite.google.com/app/apikey")

# 4. Check directories
print("\n" + "=" * 60)
print("Checking Directories")
print("=" * 60)

from pathlib import Path
dirs = ["storage/uploads", "storage/outputs", "storage/reports"]
for dir_path in dirs:
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    if Path(dir_path).exists():
        print(f"✅ {dir_path}")
    else:
        print(f"❌ {dir_path} - Could not create")

# Summary
print("\n" + "=" * 60)
print("Summary")
print("=" * 60)

if missing_packages:
    print(f"❌ Missing {len(missing_packages)} packages")
    print(f"   Run: pip install {' '.join(missing_packages)}")
else:
    print("✅ All packages installed")

if api_key and api_key != "your-api-key-here":
    print("✅ API key configured")
else:
    print("❌ API key needs to be set in .env file")

print("\n" + "=" * 60)
print("To run the application:")
print("  1. Terminal 1: python api.py")
print("  2. Terminal 2: streamlit run app.py")
print("=" * 60)
