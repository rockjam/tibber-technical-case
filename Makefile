.PHONY: run-dev
run-dev:
	poetry run flask --app tibber_technical_case/app run

.PHONY: run
run:
	docker compose up --build --wait -d

.PHONY: stop
stop:
	docker compose down

.PHONY: test
test:
	poetry run pytest tibber_technical_case

.PHONY: e2e-test
e2e-test: run
	poetry run pytest e2e_tests



