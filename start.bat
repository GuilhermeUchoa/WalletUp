@ECHO

start cmd /k  "cd backEndApiFinanceApp && venv\Scripts\activate && python manage.py runserver"
start cmd /k  "cd frontEnd && ng serve --o"

