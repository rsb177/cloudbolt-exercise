install:
	pipenv install -r requirements.txt --skip-lock

migrate:
	pipenv run python src/manage.py makemigrations
	pipenv run python src/manage.py migrate

seed:
	pipenv run python src/manage.py seed_database

build: install migrate seed

killdb:
	rm -f src/db.sqlite3

wipe: killdb migrate seed

run:
	pipenv run python src/manage.py runserver 0.0.0.0:8080

shell:
	pipenv run python src/manage.py shell

format:
	pipenv run black src

test:
	pipenv run python src/manage.py test messageboard.tests

stats:
	pipenv run python statistics.py
