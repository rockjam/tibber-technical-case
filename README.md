# Tibber Technical case

Assumptions:
* Coordinate 0,0 is at the top left

## Prerequisites

* Docker
* make
* poetry(only for local development)

## Run locally

The following command will build the server Docker image and run  
```shell
make run
```

Once running, try making a request:
```shell
curl localhost:5000/tibber-developer-test/enter-path --data '{
  "start": {
    "x": 10,
    "y": 22
  },
  "commmands": [
    {
      "direction": "east",
      "steps": 2
    },
    {
      "direction": "north",
      "steps": 1
    }
  ]
}'
```

it should respond with:
```json
{}
```


To check the data in the database run:
```shell
docker exec tibber-technical-case-db-1 psql cleaning_robot postgres -c 'select * from executions;'
```

In case you have port 5000 busy - https://medium.com/@inspiremeashish/port-5000-already-in-use-macos-sonama-issue-69d0adc09157


## Run tests

Run unit tests:
```shell
make test
```

Run unit test:
```shell
make e2e-test
```

## Run in development mode
