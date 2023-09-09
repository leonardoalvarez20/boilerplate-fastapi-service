up:
	test -f .env | cp .env.dist .env
	docker-compose up --build --detach

down:
	docker-compose down

create-migration:
	docker-compose run --rm migration dbmate new ${NAME}

run:
	poetry run uvicorn main:app --reload

test:
	poetry run coverage run -m pytest

test-report:
	poetry run coverage report
