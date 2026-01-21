import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY =", api_key)
print("TIPO =", type(api_key))
print("LONGITUD =", None if api_key is None else len(api_key))

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
r = requests.get(url)

print("STATUS =", r.status_code)
print("RESPUESTA =", r.text)
