import os

import psycopg2
from flask import Flask, request

from tibber_technical_case.database import save_execution
from tibber_technical_case.measure_utils import measure_execution_time
from tibber_technical_case.path_calculation import count_unique_positions

app = Flask(__name__)

conn = psycopg2.connect(host=os.environ["DB_HOST"],
                        port=os.environ["DB_PORT"],
                        dbname=os.environ["DB_NAME"],
                        user=os.environ["DB_USER"],
                        password=os.environ["DB_PASSWORD"])


@app.route("/tibber-developer-test/enter-path", methods=["POST"])
def enter_path():
    request_body = request.json

    commands = request_body["commands"]
    start_x = request_body["start"]["x"]
    start_y = request_body["start"]["y"]

    result, duration = measure_execution_time(lambda: count_unique_positions(start_x, start_y, commands))
    execution = save_execution(len(commands), result, duration, conn)

    return {
        "id": execution["id"],
        "timestamp": execution["timestamp"],
        "commands": execution["commands"],
        "result": execution["result"],
        "duration": execution["duration"]
    }


if __name__ == '__main__':
    app.run()
