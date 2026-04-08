from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

events = [
    {"id": 1, "title": "Sample Event 1"},
    {"id": 2, "title": "Sample Event 2"}
]

next_id = 3

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Event API!"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

@app.route("/events", methods=["POST"])
def create_event():
    global next_id

    data = request.get_json()
    if not data or "title" not in data or not data["title"]:
        return jsonify({"error": "Title is required"}), 400
    
    new_event = {
        "id": next_id,
        "title": data["title"]
    }

    events.append(new_event)
    next_id += 1

    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)
