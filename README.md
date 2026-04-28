A lightweight Python-based backend service built with **Flask** that integrates with **Google Cloud Dialogflow** to provide conversational AI capabilities.

## 🚀 Overview

This project serves as a bridge between a frontend interface and a Dialogflow NLP agent. It handles incoming user messages, processes them through Google’s AI engine, and returns structured responses.

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Flask
* **AI Engine:** Google Cloud Dialogflow (v2beta1)
* **Authentication:** Google Application Credentials

## 📋 Prerequisites

Before running this project, ensure you have:

1.  **Python 3.x** installed.
2.  A **Google Cloud Project** with the Dialogflow API enabled.
3.  A **Service Account Key** (JSON) from your Google Cloud Console.

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Karlis00/ai-nova-chatbot.git](https://github.com/Karlis00/ai-nova-chatbot.git)
    cd ai-nova-chatbot
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    .\\\\venv\\\\Scripts\\\\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install flask google-cloud-dialogflow
    ```

4.  **Configure Authentication:**
    The application expects a Google credentials file named exactly `.env` in the root directory.
    * Download your Google Service Account JSON key.
    * Rename it to `.env` and place it in the project root.

## 🏃 Running the App

Start the Flask server:
```bash
python app.py
