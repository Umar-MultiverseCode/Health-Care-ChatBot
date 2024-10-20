import os
import json
import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Database setup function
def create_table():
    conn = sqlite3.connect('chatbot_conversations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Create table when the application starts
create_table()

# Function to save conversation to the database
def save_conversation(user_message, bot_response):
    conn = sqlite3.connect('chatbot_conversations.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO conversations (user_message, bot_response)
        VALUES (?, ?)
    ''', (user_message, bot_response))
    conn.commit()
    conn.close()

user_data = {}
current_question_index = 0
current_illness = None

problem_to_dawai = {
    "cough": ("Marzanjosh", "https://aetmaad.co.in/product/al-marzanjosh", 300),
    "malaria": ("Sanna Makki", "https://aetmaad.co.in/product/sanna-makki", 70),
    "constipation": ("Sanna Makki", "https://aetmaad.co.in/product/sanna-makki", 70),
    "blood pressure": ("Qalbi Nuska", "https://aetmaad.co.in/product/qalbi-nuska", 600),
    "joint pain": ("Rumabil", "https://aetmaad.co.in/product/rumabil", 300),
    "ulcers": ("Al-Rehan", "https://aetmaad.co.in/product/al-rehan", 300),
    "sore throats": ("Multi Flora Honey", "https://aetmaad.co.in/product/multi-flora-honey", 600),
    "skin irritations": ("Multi Flora Honey", "https://aetmaad.co.in/product/multi-flora-honey", 600),
    "hair loss": ("Tulsi Honey", "https://aetmaad.co.in/product/tulsi-honey", 600),
    "infections": ("Tulsi Honey", "https://aetmaad.co.in/product/tulsi-honey", 600),
    "fever": ("Tulsi Honey", "https://aetmaad.co.in/product/tulsi-honey", 600)
}

questions = {
    "fever": [
        "How long have you been experiencing this issue?",
        "Are you currently taking any medication? (Yes/No)",
        "Do you have any allergies? (Yes/No)",
        "What is your lifestyle like? Do you eat junk food? (Yes/No)",
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    greeting_message = "Hi! How can I assist you today?"
    return render_template('chatbot.html', greeting=greeting_message)

@app.route('/get_response', methods=['POST'])
def get_response():
    global current_question_index, current_illness
    user_message = request.json['message'].lower().strip()

    # Save user message before processing it
    save_conversation(user_message, "")

    if "thank you" in user_message or "thanks" in user_message:
        response = "You're welcome! If you need further assistance, feel free to ask!"
        save_conversation(user_message, response)
        return jsonify({'response': response})

    if user_message in ["hi", "hello", "hey"]:
        response = "Hi! How can I assist you today?"
        save_conversation(user_message, response)
        return jsonify({'response': response})

    detected_illness = next((illness for illness in questions.keys() if illness in user_message), None)

    if detected_illness:
        current_illness = detected_illness
        current_question_index = 0
        response = questions[current_illness][current_question_index]
        save_conversation(user_message, response)
        return jsonify({'response': response})

    if current_illness:
        return handle_existing_case(user_message)

    response = "I'm sorry, but I don't have information about that illness."
    save_conversation(user_message, response)
    return jsonify({'response': response})

def handle_existing_case(user_message):
    global current_question_index, current_illness

    if current_question_index == 0:
        current_question_index += 1
    elif current_question_index == 1:
        if "yes" in user_message:
            current_question_index += 1
        elif "no" in user_message:
            current_question_index += 1  # Skip to the next question
        else:
            return jsonify({'response': questions[current_illness][current_question_index]})
    elif current_question_index == 2:
        if "yes" in user_message:
            current_question_index += 1
        elif "no" in user_message:
            current_question_index += 1  # Skip to the next question
        else:
            return jsonify({'response': questions[current_illness][current_question_index]})
    elif current_question_index == 3:
        if "yes" in user_message:
            response = "It's good to eat healthy!"
        else:
            response = "You should try to avoid junk food."
        current_question_index += 1
        return jsonify({'response': response})

    if current_question_index < len(questions[current_illness]):
        response = questions[current_illness][current_question_index]
        return jsonify({'response': response})
    else:
        return jsonify({'response': generate_recommendation(current_illness)})

def generate_recommendation(illness):
    global current_question_index, current_illness
    product_name, link, price = problem_to_dawai[illness]
    response = (
        f"For relief from your problem, you might consider trying {product_name}. "
        f"It is known to help reduce {illness} and improve overall health. "
        f"You can purchase it at a price of ₹{price} from here: {link}."
        " **How to use:**\n"
        "1. Follow the instructions provided on the product page.\n"
        "2. Ensure to consult a healthcare professional if needed.\n\n"
        "Take care and feel better soon!"
    )

    current_question_index = 0
    current_illness = None
    return response

# New endpoint to handle form submissions
@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.json
    # Process the data here as needed (save to database, etc.)
    # For demonstration, just return a success message
    return jsonify({'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
