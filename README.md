Находясь в папке infra, выполните команду docker-compose up. При выполнении этой команды контейнер frontend, описанный в docker-compose.yml, подготовит файлы, необходимые для работы фронтенд-приложения, а затем прекратит свою работу.

По адресу http://localhost изучите фронтенд веб-приложения, а по адресу http://localhost/api/docs/ — спецификацию API.

# Foodgram
## Описание проекта
«Фудграм» — сайт, на котором пользователи могут публиковать свои рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Зарегистрированным пользователям также доступен сервис «Список покупок». Он позволяет создавать и скачивать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Автор проекта:
*  [Никита Малумашвили](https://github.com/TLS228)

Сайт доступен по адресу: [https://mytastyfoodgram.zapto.org](https://mytastyfoodgram.zapto.org)
## Технологии
* Python 3.9
* Django
* Django Rest Framework
* Docker
* Gunicorn
* Nginx
* PostgreSQL
## Запуск проекта
1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:TLS228/foodgram.git
```

```
cd foodgram
```

2. Создать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. В корне проекта необходимо создать файл .env со следующими данными:
```
POSTGRES_USER      #имя пользователя БД 
POSTGRES_PASSWORD  #пароль пользователя БД 
POSTGRES_DB        #название БД
DB_HOST            #имя контейнера, где запущен сервер БД
DB_PORT            #порт, по которому Django будет обращаться к БД 
DEBUG              #статус режима отладки (default=False)
ALLOWED_HOSTS      #список доступных хостов
```
5. В корне проекта, где лежит файл docker-compose.production.yml, выполнить команды:
```
docker compose -f docker-compose.production.yml exec backend python manage.py migrate
docker compose -f docker-compose.production.yml exec backend python manage.py loaddata recipes/data/ingredients.json
docker compose -f docker-compose.production.yml exec backend python manage.py loaddata recipes/data/tags.json
```
