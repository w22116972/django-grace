

- Migrate (before Update)
```
heroku run python manage.py migrate
heroku run python manage.py makemigrations
```

- Update 
```bash
git add .
git commit -m ""
git push heroku master
```

- Run server
```
heroku run python manage.py runserver
```

- Open website (after running server)
```
heroku open
```

- Close server on heroku
```
heroku ps:scale web=0
```