# что используем за сборку языка 
FROM python:3.12-slim 

WORKDIR /app

# устанавливаем системные зависимости
RUN apt-get update && apg-get install -y \
    gcc \
    postgresql-client \ 
    && rm -rf /var/lib/apt/list/*

# копируем все зависимости проекта 
COPY requiremets.txt

# устанавливаем зависимости python 
RUN pip install --no-cashe-dir -r requiremets.txt 

#копируем сам проект 
COPY src/app/src 

# порт на котором разворачиваем 

EXPOSE 8000

# команды запуска 

CMD ['python','manage.py','runserver','0.0.0.0:8000']