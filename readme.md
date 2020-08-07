# User Activity Module

### Installation Steps:
``` sh
 $ Clone the project 'git clone URL'
 $ Create Virtual Environment  `virtualenv -p /usr/bin/python3 venv`
 $ Activate Virtual Enviornment `source venv/bin/activate`
 $ Install Requirements `pip install -r requirements.txt`
 $ Create new file .env and copy contents of .env.example to it and control setting of project from env
 $ Create Tables: `python manage.py migrate`
 $ Run project `python manage.py runserver 127.0.0.1:8000`
```

### Custom Commands
```sh
$ Activate virtual Environment
$ Run python manage.py generate_user (Returns User Id and API key)
```
![](https://github.com/manavchawla2012/images/blob/master/Screenshot%20from%202020-08-07%2006-34-13.png?raw=true)

### API Documentation
#### Get Methods (http://project_url/api/v1/url?api-key={api_key})
```shell script
$ get_user_activity: Return User and User Activity
```
![](https://github.com/manavchawla2012/images/blob/master/Screenshot%20from%202020-08-07%2006-35-19.png?raw=true)



# Project Created and Hosted Using

* [Django](https://docs.djangoproject.com/en/3.0/) - 3.0.2
* [Django Rest Framework](https://www.django-rest-framework.org/) - 3.11.1
* [SqlLite](https://www.sqlite.org/docs.html)
* [AmazonAWS](https://aws.amazon.com/)
* [Nginx](https://www.nginx.com/)

### Contact
* [Linkedin](https://www.linkedin.com/in/manav-chawla-9b1147120/)
* [Email](mailto:manavchawla2012@gmail.com)
