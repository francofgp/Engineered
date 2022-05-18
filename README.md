# Engineered


## Run the application

```bash
poetry install
poetry shell

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser #Optional if you want to create posts
python manage.py tailwind install
python manage.py runserver

```

In a seperate  console, if you want to edit the css with tailwind, run the following command:

```bash
python manage.py tailwind start
```

If you don't run the command above, the css assets of tailwind will not be updated, thus you wont see any changes in your browser



## Build

```bash
poetry export -f requirements.txt -o requirements.txt
python manage.py tailwind build


```
in python anywhere open bash console and
```bash
git clone https://github.com/francofgp/Engineered.git

mkvirtualenv --python=/usr/bin/python3.9 engineered # engineered is the name of your env
cd Engineered/
pip install -r requirements.txt

# Go to web in pythonanywhere, create new webapp, with manual configuration
# Add you virtualenv name, in my case engineered

```

## Acknowledgment

- Default post photo: 📷 by Jessica Lewis Creative from Pexels