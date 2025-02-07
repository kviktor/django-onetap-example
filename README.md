Run the following commands
- `docker-compose build`
- `cp .env.example .env` and set your client id
- `docker-compose up`
- `docker-compose exec django python manage.py migrate`
- clone the repo into the project directory and check out the changes
- `docker-compose exec django pip install -e "social-core[google-onetap]"`
- go to http://localhost:54321/
