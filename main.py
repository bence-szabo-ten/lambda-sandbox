import json
import requests


def handler(event, context):
    response = requests.get("https://reqres.in/api/users")
    print(json.dumps(response.json(), indent=2))
