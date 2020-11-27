makemigration:
	docker-compose exec portal python -m manage makemigration

migrate:
	docker-compose exec portal python -m manage migrate
