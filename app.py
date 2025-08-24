#app.py

import os
import json
import requests
from flask import Flask, request, render_template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("IBM_API_KEY")
DEPLOYMENT_ID = os.getenv("DEPLOYMENT_ID")
REGION = os.getenv("REGION", "us-south")

TOKEN_URL = "https://iam.cloud.ibm.com/identity/token"
PREDICT_URL = f"https://{REGION}.ml.cloud.ibm.com/ml/v1/deployments/{DEPLOYMENT_ID}/predictions"

def get_iam_token(api_key):
    """Get IBM Cloud IAM token"""
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"apikey={api_key}&grant_type=urn:ibm:params:oauth:grant-type:apikey"
    response = requests.post(TOKEN_URL, headers=headers, data=data)
    return response.json().get("access_token", "")

@app.route("/", methods=["GET", "POST"])
def home():
    result_text = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input.strip():
            iam_token = get_iam_token(API_KEY)
            headers = {
                "Authorization": f"Bearer {iam_token}",
                "Content-Type": "application/json"
            }
            payload = {
                "input": [
                    {"role": "user", "content": user_input}
                ]
            }
            response = requests.post(PREDICT_URL, headers=headers, json=payload)
            try:
                result_text = json.dumps(response.json(), indent=2)
            except:
                result_text = "Error processing response"
        else:
            result_text = "Please enter a question."
    return render_template("index.html", result=result_text)

if __name__ == "__main__":
    app.run(debug=True)