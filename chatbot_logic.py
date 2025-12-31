import sqlite3

def get_response(user_input):
    # Simple NLP rule-based logic
    user_input = user_input.lower()

    if "hello" in user_input:
        reply = "Hello! How can I help you?"
    elif "bye" in user_input:
        reply = "Goodbye! Have a great day!"
    else:
        reply = "I'm still learning. Can you rephrase?"

    # Save conversation to database
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chats (user_message, bot_reply) VALUES (?, ?)",
        (user_input, reply)
    )
    conn.commit()
    conn.close()

    return reply
