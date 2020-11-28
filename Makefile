migrate:
	docker-compose exec portal python -m manage makemigrations
	docker-compose exec portal python -m manage migrate

static:
	docker-compose exec portal python -m manage collectstatic --noinput

admin:
	docker-compose exec portal python -m manage createsuperuser 

boot: migrate admin static