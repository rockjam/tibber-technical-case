# Tibber Technical case

Tibber Technical case, Python implementation.
Flask used for API routing, psycopg2 for the database access, gunicorn as the WSGI server.
The server is containerized with Docker, and has Docker Compose setup for simplified end to end testing.

## Prerequisites

* Docker
* GNU make
* poetry(for local development)

## How to run the server

Run the following command to build the Docker image and run the server, alongside with prepared Postgres database:

```shell
make run
```

Once ready, try calling the API:

```shell
curl -XPOST localhost:5000/tibber-developer-test/enter-path -H "Content-Type: application/json" --data '{
  "start": { "x": 10, "y": 22 },
  "commands": [
    {"direction": "east", "steps": 2},
    {"direction": "north", "steps": 1},
    {"direction": "west", "steps": 100}
  ]
}'
```

It should respond with something like:

```json
{
  "commands": 3,
  "duration": 0.000045,
  "id": 317,
  "result": 104,
  "timestamp": "Fri, 08 Nov 2024 03:16:55 GMT"
}
```

> [!NOTE]  
> If you're on MacOS, you might need to [disable Airplay Receiver](https://medium.com/@inspiremeashish/port-5000-already-in-use-macos-sonama-issue-69d0adc09157) to run the API on port 5000  

Last, confirm that execution is written to the database:

```shell
docker exec tibber-technical-case-db-1 psql cleaning_robot postgres -c 'select * from executions;'
```

## How to run tests

Before running tests, run `make dev-setup` to set up the development environment.

To run unit tests:

```shell
make test
```

To run end-to-end tests:

```shell
make e2e-test
```

## How to run server locally in dev-mode

This assumes that you have a running Postgres server on localhost:5432 and
`cleaning_robot` database with schema from `db/createdb.sql`.

Run `docker compose up -d db` to create a pre-configured Postgres instance in Docker.
Once ready, run:

```shell
make run-dev
```

