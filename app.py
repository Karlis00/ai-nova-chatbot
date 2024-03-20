from flask import Flask, jsonify, request
from google.cloud import dialogflow_v2beta1 as dialogflow
import os
GOOGLE_AUTHENTICATION_FILE_NAME = "env/key.json"
current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
app = Flask(__name__)

@app.route('/getId', methods=['GET'])
def getId():
    # Create a simple JSON response
    response = {'message': 'Kam Hung Chan (200601463)'}
    return jsonify(response)

@app.route('/webhook', methods=['POST'])
def webhook():
    request_data = request.get_json()
    message_text = request_data['message']
    response_text = process_message(message_text)
    response = {'message': response_text}
    return jsonify(response)

def process_message(message_text):
    project_id = 'ai-nova-addl'
    session_id = '200601463'
    language_code = 'en-US'

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=message_text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    return response.query_result.fulfillment_text

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)