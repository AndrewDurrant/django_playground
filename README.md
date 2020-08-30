**Initial Setup for Django Project**
1. create a new virtual environment - `python3 -m venv ~/.virtualenvs/<virtual_env_name>`
   - it's a good idea to keep all virtual environments in one place, ex. ./virtualenvs/ in home directory. The path is where the new environment will be saved
2. activate your virtual environment - `source ~/.virtualenvs/<virtual_env_name>/bin/activate`
   - if source doesn't work, try using a dot instead `. ~/.virtualenvs/djangodev/bin/activate`
3. after you've created and activated a virtual environment, install Django `python -m pip install Django`
4. cd into a directory where you'd like to store your code, run command `django-admin startproject <project_name>`
   - this creates a <project_name> directory in your current directory
5. git init
6. Start the server `python manage.py runserver`

__Creating a new app__
`django-admin startapp <app_name>`

__Setting Up PostgreSQL__
`pip install psycopg2-binary`

__migrate table data__
`python manage.py migrate`


