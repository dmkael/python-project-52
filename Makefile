dev:
	python manage.py runserver 0.0.0.0:8000
PORT ?= 8000
gunicorn:
	poetry run gunicorn -w 4 -b 0.0.0.0:$(PORT) task_manager.asgi:application -k uvicorn.workers.UvicornWorker
install:
	poetry install
migrate:
	poetry run python manage.py migrate
create-migrations:
	poetry run python manage.py makemigrations
lint:
	poetry run flake8 task_manager
console:
	poetry run python manage.py shell_plus --ipython
prebuild-translation:
	poetry run python manage.py makemessages --all
translate:
	poetry run django-admin compilemessages