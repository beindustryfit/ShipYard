.PHONY: up test
up:
	docker compose up --build

test:
	pytest -q
