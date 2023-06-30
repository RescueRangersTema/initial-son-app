# initial-son-app
Initial son project app

docker-compose build <-- Run on project startup or every time when add new module in requirements.txt

docker-compose up <-- Starts an application on 127.0.0.1:8000
docker-compose down <-- Stop all application containers

To use django via docker:

docker-compose run --rm app sh -c "python manage.py createsuperuser"

docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

!!! Migrations applied automaticly via docker-compose.yml
Database available on ports 5434:5432
