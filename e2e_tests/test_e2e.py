import json

import requests


def test_e2e():
    request_body = {
        "start": {
            "x": 10,
            "y": 22
        },
        "commands": [
            {
                "direction": "east",
                "steps": 2
            },
            {
                "direction": "north",
                "steps": 1
            }
        ]
    }
    response = requests.post("http://localhost:5000/tibber-developer-test/enter-path", json.dumps(request_body))
    response_body = response.json()

    assert response_body["id"] > 0
    assert response_body["duration"] > 0
    assert response_body["commands"] == 3
    assert response_body["result"] == 5
    assert len(response_body["ts"]) > 0
