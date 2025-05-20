This is a dummy test for easy deplyment testing. Clone the repo and follow the steps:-

Step 1:-

Create virtual enviornment and initialize it

    python3 -m venv myenv

    source myenv/bin/activate --linux
    ./myenv/Scripts/activate  --windows

Step 2:-

Install the requirements

    pip install -r requirement.txt

Step 3:- 

  Configure DB
  Navigate to test project and edit settings:-

        DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'username',
        'PASSWORD': 'pswd',
        'HOST': 'localhost/ip',
        'PORT': 'port',
    }
}

  alternativley you can use sqllite for easier integration -- recommended for local testing, for deployment/docker use postgres

   For sqllite:-

     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }

Step 4:-
  
  Naviage to folder conatining manage.py. Make migrations and Run the server.

    python3 manage.py migrate
    python3 manage.py makemigrations
    python3 manage.py runserver 

   You should see the app running in localhost. 

Step 5:- 

  Creating dokcer image

  Install docker
  Pull posgres 14 image

    docker pull postgres:14

  Create docker image via Dockerfile. Navigate to folder containing Dockerfile and run

    docker build -t test-app:1.0 .  

  Check present images, you should both postgres:14 and test-app:-
    
    docker images  
  
Step 6:-

  In settings.py make the following change. 

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': os.environ.get('DATABASE_NAME'),
          'USER': os.environ.get('DATABASE_USER'),
          'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
          'HOST': os.environ.get('DATABASE_HOST'),
          'PORT': os.environ.get('DATABASE_PORT'),
      }
  }

Step 7:- 

  Create a docker network and compose docker using docker-compose file and start it. 

     docker network create docker_stuffs_default
     docker-compose -f test_app_db_compose.yaml create
     docker start django-app postgres-db 

  Test using curl


!! Check for typos !!
    
     

    





  
  
