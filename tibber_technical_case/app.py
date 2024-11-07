from datetime import datetime

from flask import Flask
from flask import request

from tibber_technical_case.path_calculation import count_unique_positions

app = Flask(__name__)


@app.route("/tibber-developer-test/enter-path", methods=["POST"])
def enter_path():
    request_body = request.json

    commands = request_body["commands"]
    start_x = request_body["start"]["x"]
    start_y = request_body["start"]["y"]
    result = count_unique_positions(start_x, start_y, commands)
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
