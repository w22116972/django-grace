
## Requirement packages

```
brew install postgresql
pip install gunicorn
pip install whitenoise
pip install psycopg2
pip install dj-database-url
```

## Modified file

#### requirements.txt @ top level of directory
- gunicorn: 高效能的http server
- whitenoise: 在heroku上hosting CSS/JS的
- psycopg2: python跟postgresql溝通的
- dj-database-url: 在heroku上取得資料庫設定

```
Django==1.10.4
gunicorn==19.6.0
whitenoise==3.2.2
psycopg2==2.6.2
dj-database-url==0.4.1
```

#### settings.py 
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
import dj_database_url
DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = False
try:
    from .local_settings import * 
except ImportError:
    pass
```
#### wsgi.py
```python
from whitenoise.django import DjangoWhiteNoise
# after application = get_wsgi_application()
application = DjangoWhiteNoise(application)
```

#### local_settings.py
- 保存local 開發的設定(e.g. sqlite, remote用postgresql)
- 不會commit to repository

```python
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DEBUG = True
```

#### Procfile @ top level of directory
- heroku根據procfile來決定怎麼執行程式

```
web: gunicorn PROJECT_NAME.wsgi --pythonpath APP_NAME
```

#### runtime.txt @ top level of directory
- heroku透過此檔案決定用哪個版本的python

```
python-3.5.2
```
--

*heroku run*: do remote instruction

- Migrate 

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