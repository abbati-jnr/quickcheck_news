# QuickCheck News 
Python Developer Case Study by Ahmad Abbati Bako (khalypha360@gmail.com). This is a news web app based on Hacker News public API.
The goal is to make it easier to navigate Hacker news. This application uses Celery and Redis for database syncing.

## Installations
```bash
pip install -r requirements.txt 
```
and
```bash
manage.py migrate
``` 

### Redis is a broker server 
Also you need to install Redis in your machine 
More details about redis [Redis](https://redis.io/)

## Run the broker server 
```bash
redis-server
```

## Next run the Django server
```bash
python manage.py runserver
``` 

## Next step run the Celery worker 
```bash
celery -A quickcheck_news worker -l info
```

## Next run the scheduler 
```bash
celery -A quickcheck_news beat -l info
```
This is all development setup.

Hope my application will be duly considered. :)