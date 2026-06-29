from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    new_id = max((e.id for e in events), default=0) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify({"id": new_id, "title": new_event.title}), 201  


# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json()
    event_to_update = next((event for event in events if event.id == event_id), None)
    if not event_to_update:
        return jsonify({"error": "Event not found"}), 404

    if "title" in data:
        event_to_update.title = data["title"]
        return jsonify({"id": event_to_update.id, "title": event_to_update.title}), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event_to_delete = next((event for event in events if event.id == event_id), None)
    if not event_to_delete:
        return jsonify({"error": "Event not found"}), 404

    events.remove(event_to_delete)

    return jsonify({"message": "Event deleted successfully"}), 204



if __name__ == "__main__":
    app.run(debug=True)
