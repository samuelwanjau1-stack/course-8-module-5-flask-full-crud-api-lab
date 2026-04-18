from flask import Flask, jsonify, request

app = Flask(__name__)

class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

events = [Event(1, "Tech Meetup"), Event(2, "Python Workshop")]

@app.route("/events", methods=["POST"])
def create_event():
    # Task 1: Accept incoming JSON for a new event
    data = request.get_json()
    # Task 2: Design ID logic
    new_id = events[-1].id + 1 if events else 1
    # Task 3: Create and add new object to list
    new_event = Event(new_id, data['title'])
    events.append(new_event)
    # Task 4: Return 201 status with the new object
    return jsonify(new_event.to_dict()), 201

@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # Task 1: Locate event by ID
    event = next((e for e in events if e.id == event_id), None)
    # Task 2: Handle missing event
    if not event: return jsonify({"error": "Event not found"}), 404
    # Task 3: Process update from JSON
    event.title = request.get_json()['title']
    # Task 4: Return updated object
    return jsonify(event.to_dict()), 200

@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # Task 1: Identify index of event
    global events
    # Task 2: Check existence
    if not any(e.id == event_id for e in events):
        return jsonify({"error": "Event not found"}), 404
    # Task 3: Remove element from list
    events = [e for e in events if e.id != event_id]
    # Task 4: Return success code
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)