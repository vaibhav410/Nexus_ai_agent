import google.generativeai as genai
import os
from dotenv import load_dotenv

print("--- Starting Verification ---")

# 1. Check if app.env exists
if os.path.exists("app.env"):
    print("SUCCESS: app.env file found.")
else:
    print("ERROR: app.env file NOT found in current directory.")
    print(f"Current Directory: {os.getcwd()}")

# 1.1 Check for static files
if os.path.exists("static/style.css"):
    print("SUCCESS: static/style.css found.")
else:
    print("ERROR: static/style.css NOT found.")

if os.path.exists("static/script.js"):
    print("SUCCESS: static/script.js found.")
else:
    print("ERROR: static/script.js NOT found.")

# 2. Load environment
load_dotenv("app.env")
api_key = os.getenv("GEMINI_KEY")

if api_key:
    print(f"SUCCESS: API Key found: {api_key[:5]}...{api_key[-4:]}")
else:
    print("ERROR: GEMINI_KEY not found in environment variables.")
    exit(1)

# 3. Configure Gemini
try:
    genai.configure(api_key=api_key)
    print("SUCCESS: Gemini configured.")
except Exception as e:
    print(f"ERROR: Failed to configure Gemini: {e}")
    exit(1)

# 4. List Models
print("Listing available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"ERROR: Failed to list models: {e}")

# 5. Test Generation with a fallback
print("\nAttempting to generate content with 'gemini-2.5-flash'...")
try:
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content("Hello")
    print(f"SUCCESS: Model responded: {response.text.strip()}")
except Exception as e:
    print(f"ERROR: Generation failed: {e}")
