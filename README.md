git clone https://github.com/Hailecw/omega-chatbot.git
cd chatbot


python -m venv env

.\env\Scripts\activate

source env/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

use 127.0.0.1 instead of localhost for google Oauth

http://127.0.0.1:8000/ -------- home page
http://127.0.0.1:8000/oauth/login ----- login page
http://127.0.0.1:8000/oauth/logout ----- logout page


