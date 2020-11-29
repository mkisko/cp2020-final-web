migrate:
	docker-compose exec portal python -m manage makemigrations
	docker-compose exec portal python -m manage migrate

static:
	docker-compose exec portal python -m manage collectstatic --noinput

admin:
	docker-compose exec portal python -m manage createsuperuser 

init_db:
	docker-compose exec portal python -m manage loaddata init_db

boot: migrate admin static