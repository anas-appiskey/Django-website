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
8. Shell
   ```
   py manage.py shell
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
13. now we are separating the django files from html file create a file name index.html
     ```
      django-website
            |___mysite
            |___polls
               |__migrations
               |___templates
                  |___polls 
                     |___index.html            
     ```
     and the rest of files will also be there , it is only to show you where to place the index.html file. Note the templates folder name is **case sensitive**

     shift+cntl+V 
14. The above template displays a radio button for each question choice. The value of each radio button is the associated question choice’s ID. The name of each radio button is "choice". That means, when somebody selects one of the radio buttons and submits the form, it’ll send the POST data choice=# where # is the ID of the selected choice. This is the basic concept of HTML forms.
15. forloop.counter indicates how many times the for tag has gone through its loop
16. Since we’re creating a POST form (which can have the effect of modifying data), we need to worry about Cross Site Request Forgeries. Thankfully, you don’t have to worry too hard, because Django comes with a helpful system for protecting against it. In short, all POST forms that are targeted at internal URLs should use the {% csrf_token %} template tag.
17. The vote in Views.py use to give us the total votes for a single option 
18. After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse. HttpResponseRedirect takes a single argument: the URL to which the user will be redirected (see the following point for how we construct the URL in this case).

19. As the Python comment above points out, you should always return an HttpResponseRedirect after successfully dealing with POST data. This tip isn’t specific to Django; it’s good Web development practice in general.

20. We are using the reverse() function in the HttpResponseRedirect constructor in this example. This function helps avoid having to hardcode a URL in the view function. It is given the name of the view that we want to pass control to and the variable portion of the URL pattern that points to that view. In this case, using the URLconf we set up in Tutorial 3, this reverse() call will return a string like




