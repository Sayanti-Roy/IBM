# College Admission Agent (IBM Granite + Cloud Lite)

## Overview
The **College Admission Agent** is an AI-powered assistant that helps students retrieve admission-related details like eligibility, policies, fees, and deadlines. It uses **IBM Granite** and **IBM Cloud Lite** for real-time, AI-driven answers through a simple web interface.

---

## Features
- **AI-Powered Q&A** – Get answers about courses, fees, deadlines, and eligibility.
- **Real-Time Information Retrieval** – Uses Retrieval-Augmented Generation (RAG) for accuracy.
- **Simple Web Interface** – Enter queries and get responses instantly.
- **Powered by IBM Granite & Cloud Lite** – Ensures scalable and secure AI model hosting.

---

## Folder Structure
college-admission-agent/
│
├─ app.py # Flask backend
├─ requirements.txt # Dependencies list
├─ .env # Environment variables (use your own API keys)
├─ .gitignore # Ignore .env and cache
│
└─ templates/
└─ index.html # Frontend UI


---

## Environment Setup
Create a `.env` file in the root folder with your own IBM Cloud credentials:
IBM_API_KEY=your_ibm_api_key_here
DEPLOYMENT_ID=your_deployment_id_here
REGION=us-south


> **Important:** Replace `your_ibm_api_key_here` and `your_deployment_id_here` with the credentials from your IBM Cloud Watsonx deployment.

---

## Installation
1. Clone the repository:
   
   git clone https://github.com/your-repo/college-admission-agent.git
   cd college-admission-agent
Install required packages:


pip install -r requirements.txt
Run the application:


python app.py
Usage
Open your browser at http://127.0.0.1:5000/

Enter a query (e.g., "What are the eligibility criteria for MBA admission?")

View AI-generated answers instantly.

Wow Factors
Instant retrieval of college admission information.

AI-powered contextual summarization.

IBM Granite + Cloud Lite ensures reliability and scalability.

Future Scope
Real-time integration with university databases.

Voice-based queries for accessibility.

Comparative analysis of multiple colleges in one chat.

License
MIT License





