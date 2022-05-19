# Engineered

Engineered is my personal blog made with Django, where I will be sharing my journey as a software engineer.

![Imgur](https://i.imgur.com/0BtkooL.png)

## Run the application

### Clone the repo
```bash
git clone https://github.com/francofgp/Engineered.git
cd Engineered/
```

### Install dependencies with [Poetry](https://python-poetry.org/).

```bash
poetry install
poetry shell
```

If you do not have poetry just use

```bash
pip install -r requirements.txt
```
### Run django
```bash
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser # Optional if you want to create posts
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


## [License](#license)

Closures is provided under the [MIT License](https://github.com/vhesener/Closures/blob/master/LICENSE).

```text
MIT License

Copyright (c) 2021 Pértile Franco Giuliano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


[MIT](https://choosealicense.com/licenses/mit/)


