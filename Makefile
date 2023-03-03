up-backend:
	docker-compose --file infra/docker-compose.yml run --service-ports --rm backend /bin/sh || true
up-frontend:
	docker-compose --file infra/docker-compose.yml run --service-ports --rm frontend /bin/sh || true
test:
	python -m pytest --discover
clean:
	docker ps -aq | xargs docker stop | xargs docker rm
build:
	docker-compose -f ./infra/docker-compose.yml build --no-cache
