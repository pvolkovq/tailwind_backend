serv:
	uv run backend/manage.py runserver 0.0.0.0:8000
static:
	uv run backend/manage.py collectstatic
migrate:
	uv run backend/manage.py makemigrations
	uv run backend/manage.py migrate
su:
	uv run backend/manage.py createsuperuser
test:
	uv run backend/manage.py test $(appname).tests