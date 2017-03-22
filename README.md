# Artbud

Web App Development Group Project
A web application developed to help any artistic soul share their art with the world.

Lab Thursday Group 3 Team C

Python Anywhere link: http://artbud.pythonanywhere.com/

***
##Project Members (github account - name, student matriculation number)

zixk -Dominik Bladek - 2144751b

Giles Munn - 2227780m

Charlie Parker - 2144176p

Andreas Klitis - 2141487k


***
##Steps to run:

1. Download files: 
```
git clone https://github.com/GilesGlasgow/Artbud
```

2. Setup virtual environment: 
```
mkvirtualenv artbud
```

3. Work on new virtual environment:
```
workon artbud
```

4. Install requirements:
```
pip install -r requirements.txt
```

5. Setup database:
```
python manage.py makemigrations artbud
python manage.py migrate
```

6. Run project:
```
python manage.py runserver
```

7. Find server on http://127.0.0.1:8000/artbud/



