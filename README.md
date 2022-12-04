### troo-task
<br/>  

### Features
* All operation category api with nested list view with depth of n elements.
* All operation products api
* Async mailing
* Scheduled async mailing
* Cache Implementation for instant product list page load

<br/>

## Getting Started

### Prerequisites
You should have Python3x and redis installed on your machine.

### Installation
Just make a virtual environment in the project directory and activate it.
Then install all the dependencies given in requirements.txt using
#### `pip install -r requirements.txt` 

Then make the migrations.
####  `python manage.py makemigrations`

Let's sync your database with the models.
#### `python manage.py migrate`

Then start all three servers.
#### `python manage.py runserver`
#### `celery -A core.celery worker --pool=solo -l info`
#### `celery -A core beat -l info`

<br/>

##APIs.
#### `api/products/` (get, put, post, delete, patch)
#### `api/categories/` (get, put, post, delete, patch)
#### `api/send-mail/` (args: email)
#### `api/send-mail-later/` (args: email)



## Contact
Shivam Maithil - shivammaithil1008@gmail.com


