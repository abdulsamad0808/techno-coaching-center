from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---------------- AI LOGIC ----------------
def ai_agent(user_msg):
    msg = user_msg.lower()

    if "course" in msg or "courses" in msg:
        return "We offer Python, Java, SQL, Excel and CSC computer coaching."

    elif "time" in msg or "timing" in msg:
        return "Classes run from 6:00 PM to 8:00 PM."

    elif "fee" in msg or "fees" in msg:
        return "Please visit our center for fee details."

    elif "location" in msg or "area" in msg or "where" in msg or "saidapet" in msg:
        return "Our Techno Coaching Center is in Saidapet, near your local CSC."

    elif "duration" in msg or "how long" in msg:
        return "Each course duration is 3 months."

    elif "contact" in msg or "phone" in msg or "number" in msg or "call" in msg:
        return "Contact us at: 885881274."

    else:
        return "Please visit our center for more details."

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    reply = ai_agent(user_msg)
    return jsonify({"reply": reply})

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

