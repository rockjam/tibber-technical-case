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
    response = requests.post(
        "http://localhost:5000/tibber-developer-test/enter-path",
        json.dumps(request_body),
        headers={
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200

    response_body = response.json()
    assert response_body["id"] > 0
    assert response_body["duration"] > 0
    assert response_body["commands"] == 2
    assert response_body["result"] == 4
    assert len(response_body["ts"]) > 0
