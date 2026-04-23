post_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "userId": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["id", "userId", "title"]
}