# Event Management API

A simple RESTful API for managing events, built with Python and Flask.

## Routes

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/events` | Create a new event |
| `PATCH` | `/events/<id>` | Update an existing event title |
| `DELETE` | `/events/<id>` | Remove an event |

## API Usage Examples

### POST /events
**Request:**
```json
{ "title": "Hackathon" }
