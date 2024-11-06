from datetime import datetime

from flask import Flask

from tibber_technical_case.calculate_path import count_unique_positions

app = Flask(__name__)


@app.route("/tibber-developer-test/enter-path", methods=["POST"])
def enter_path():
    request = {
        "start": {
            "x": 10,
            "y": 22
        },
        "commands": [
            {"direction": "east", "steps": 2},
            {"direction": "north", "steps": 1},
            {"direction": "south", "steps": 2},
        ]
    }

    commands = request["commands"]
    result = count_unique_positions(request["start"]["x"], request["start"]["y"], request["commands"])
    now = datetime.now()

    return {
        "id": 123,  # TODO
        "ts": str(now),
        "commands": len(commands),
        "result": result,
        "duration": 33,  # TODO
    }


if __name__ == '__main__':
    app.run()
