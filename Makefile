.PHONY: run
run:
	docker compose up --build --wait -d

.PHONY: stop
stop:
	docker compose down

.PHONY: dev-setup
dev-setup:
	poetry install

.PHONY: run-dev
run-dev:
	poetry run flask -e .env.local --debug --app tibber_technical_case/app run

.PHONY: test
test:
	poetry run pytest -s tibber_technical_case

.PHONY: e2e-test
e2e-test: run
	poetry run pytest -s e2e_tests



