# PYTHON DJANGO FRAMEWORK
 
- [PYTHON DJANGO FRAMEWORK](#python-django-framework)
  - [Commands](#commands)
  - [Flow of Project](#flow-of-project)
  
## Commands

1. Create Project 
   
   ```
   django-admin startproject foldername
   ```
2. Run Server
   
   ```
   python manage.py runserver
   ```
   with this command you will start the django development server, a light weight server written purely in python 

 **Note** 
```
The difference between a project and app? 
Answer)A project can contain multiple app and an app can be in multiple projects  
 ```
3. Create App 
    ```
    python manage.py startapp polls(app-name)
    ```

4. migrate 
   The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py 

   ```
   py manage.py migrate
   ```

   By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
 
   ```
   python manage.py makemigrations polls
   ```

5. sqlmigrate
   The sqlmigrate command takes migration names and returns their SQL:
   ```
   python manage.py sqlmigrate polls 0001
   ```
6. Admin

   ```
   py manage.py createsuperuser
   ```
7. Server 
   ```
   py manage.py runserver
   ```


## Flow of Project

1. we create a project and then make an poll app in it.
2. we then create urls.py file in polls folder 
3. to display urls.py, we import django.http in views file 
4. In views we make a function to show the content 
5. we use urls.py file in polls , to display the index function in views
6. Include the polls app in mysite (urls.py) file  
7. Use the migrate command cCreate models of question and choice .
8. add this line in settings 'polls.apps.PollsConfig' to make the app visible for project , 
9. Now, run migrate again to create those model tables in your database: 
10. create the superuser and start the development server
11. register the models in admin.py file to add these in panel
12. add three new views in views.py file and add urlpatterns in urls.py file in polls






