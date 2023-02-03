# Task-Manager
 Task-Manager is a Web App developed using Python Django framwork.
 
This Web App demonstrates CRUD functionality and User Authentification system of the Django framwork with function-based views.

Its main functions are :
1. Creating Your Own account by registering and filling up the form provided by the register template.
2. Logging In if you already have an account and also Logging Out of your account.
3.If you happen to make any error a warning message will pop off to notify you that you've made an error.
3. You can access your tasks through the list tasks window and you can operate these functions on them : Create , Read, Update, Delete any task.
4. You can use the search bar the search for any term you provide and it will give you your search results based on wether the term has occured in any of your tasks.
5. The database used for this project is SQLite3.

### This is the Login page:

![Capture1](https://user-images.githubusercontent.com/116681645/216663799-cee5ce08-76d6-4dda-95e3-93960d746c6a.PNG)

### This is the Registration page:

![Capture2](https://user-images.githubusercontent.com/116681645/216663818-74725be4-7d35-448d-8f9b-0af247b309cb.PNG)

### This is The Main View of the user:

![Capture3](https://user-images.githubusercontent.com/116681645/216663840-f57d0a2e-5f79-419d-aa7a-3be0afe9c6bd.PNG)

### This is the Add task view:

![Capture4](https://user-images.githubusercontent.com/116681645/216663850-ba085ae1-1550-4857-a262-94ca86bc6dcb.PNG)

### This is the Update task view:

![Capture5](https://user-images.githubusercontent.com/116681645/216663866-613e637b-7d2f-4310-b8bc-be3c9d5476ec.PNG)

### This is how your search results will be demonstrated:

![Capture6](https://user-images.githubusercontent.com/116681645/216663778-2eff81ef-741a-4cec-a7c0-e8a43699a163.PNG)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Chouaib-Djerdi/Task-Manager.git
$ cd task_manager
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd task_manager
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/members/register_user/`.

