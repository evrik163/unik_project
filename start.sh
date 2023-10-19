#!/bin/bash

#if [ "$DB_HOST" = "unik_db" ]
#then
echo "Ожидание инициализации базы данных"
#  while !</dev/tcp/$DB_HOST/$DB_PORT; do sleep 1; done 2>/dev/null
sleep 5
echo "Готово"
#fi

python cool.py
rm train.csv
python manage.py migrate
python manage.py createsuperuser --no-input
python manage.py loaddata ./fixtures/data.json
python manage.py runserver "0.0.0.0:8000"
