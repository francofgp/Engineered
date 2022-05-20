# Engineered

Engineered is my personal blog made with Django, where I will be sharing my journey as a software engineer.

<p align="center">
  <img src="https://i.imgur.com/0BtkooL.png" alt="Sublime's custom image"/>

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

</p>

|   Vocabulary  | Flashcards    | Export    |
| :----:        | :----:        | :----:    |
| Each user can save words in their own vocabulary. | Vocabulary review through flashcards. | Possibility to export the vocabulary to PDF.| 



## Table of contents
- [Engineered](#engineered)
  - [Table of contents](#table-of-contents)
  - [Run the application](#run-the-application)
  - [Showcase](#showcase)
  - [Acknowledgment](#acknowledgment)
  - [License](#license)



## Run the application


1. Clone the repo
```bash
git clone https://github.com/francofgp/Engineered.git
cd Engineered/
```

2. Install dependencies with [Poetry](https://python-poetry.org/).

```bash
poetry install
poetry shell
```

If you do not have poetry just use

```bash
pip install -r requirements.txt
```
3. Run django
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

If you don't run the command above, the css assets of tailwind will not be updated when you edit the files, thus you will not see any changes in your browser, and you will not have hot reload either.



## Showcase

**Home**
![Home image](https://i.imgur.com/KMqBu40.png)

## Acknowledgment
- [Django](https://www.djangoproject.com/) The web framework for perfectionists with deadlines.
- [tailwindcss](https://github.com/python-pillow/Pillow) A utility-first CSS framework for rapid UI development.
- [Pillow](https://github.com/python-pillow/Pillow) The friendly PIL fork (Python Imaging Library)
- [django-tailwind](https://github.com/timonweb/django-tailwind) Django + Tailwind CSS = 💚
- [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) Django admin CKEditor integration.
- [django-taggit](https://github.com/jazzband/django-taggit) Simple tagging for django
- [Django](https://www.djangoproject.com/) The web framework for perfectionists with deadlines.
- [python-dotenv](https://github.com/theskumar/python-dotenv) Reads key-value pairs from a .env file and can set them as environment variables. It helps in developing applications following the 12-factor principles.
- Default post photo 📷 by [Jessica Lewis Creative](https://www.pexels.com/es-es/@thepaintedsquare/) from Pexels

## [License](#license)

Closures is provided under the [MIT License](https://github.com/vhesener/Closures/blob/master/LICENSE).

```text
MIT License

Copyright (c) 2022 Pértile Franco Giuliano

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





<!-- ## Build

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

``` -->