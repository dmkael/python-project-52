dev:
	python manage.py runserver
PORT ?= 8000
gunicorn:
	poetry run gunicorn -w 4 -b 0.0.0.0:$(PORT) task_manager.asgi:application -k uvicorn.workers.UvicornWorker
install:
	poetry install