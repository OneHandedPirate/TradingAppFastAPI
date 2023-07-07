up:
	docker compose -f docker-compose-dev.yaml up -d
down:
	docker compose -f docker-compose-dev.yaml down

up_prod:
	docker compose -f docker-compose-prod.yaml up -d --build
down_prod:
	docker compose -f docker-compose-prod.yaml down