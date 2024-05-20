import json


def serialize_messages(messages, request):
    # Serialize messages to JSON
    serialized_messages = []
    for message in messages.get_messages(request):
        serialized_messages.append({
            'message': message.message,
            'tags': message.tags,
        })
    context = {
        'messages': json.dumps(serialized_messages),
    }
    return context
