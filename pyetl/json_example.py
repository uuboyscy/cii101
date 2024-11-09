import json

sample_dict = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "phone_numbers": [
        {"type": "home", "number": "555-555-5555"},
        {"type": "work", "number": "555-555-5556"}
    ],
    "is_active": True,
    "roles": ["user", "admin"]
}

json_str = json.dumps(sample_dict)
print(type(json_str))
print(json_str)
json_data = json.loads(json_str)
print(type(json_data))
