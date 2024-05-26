dev:
	python manage.py runserver
gunicorn:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker