from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_response
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    reply = get_response(user_input)
    return jsonify({"reply": reply})

@app.route("/history")
def history():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_message, bot_reply FROM chats")
    chats = cursor.fetchall()
    conn.close()
    return jsonify(chats)

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
