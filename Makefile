serv:
	uv run backend/manage.py runserver 0.0.0.0:8000
static:
	uv run backend/manage.py collectstatic