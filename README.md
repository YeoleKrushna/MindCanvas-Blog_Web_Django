**Created Basic Blog App with CRUD functionality along with Signup, Login, Logout for Authentication.**

How to install and run this web application on your system ?

1. You need to have Python installed on your machine, you can get it installed by following way

   https://phoenixnap.com/kb/how-to-install-python-3-windows

2. Install Django using command line

   python -m pip install Django

3. Clone this repository on your machine using this command

   git clone https://github.com/amol410/DataGrid.git
   
4. If required go to the directory
   cd datagrid
   
5. Open VsCode or Any other code editor and run these commands for creating files and executing them into database
   (if sqlite database shown in directory following commands not required)

   python manage.py makemigrations

   python manage.py migrate

6. Runserver using following command

   python manage.py runserver

7. While Signup, Your username must be different from password and in password use Capital letter, Small letters and one Special Charecter and a Number
   
   


Functionality --

1. Implemented basic CRUD (Create, Read, Update, Delete) operations for blog posts where each blog have Title and Body.

2. Created basic user authentication where users can sign up, log in, and log out (links created will take you to respective pages), it has shown on frontpage itself.

3. Home page has listed with all blog posts in reverse chronological order (descending order), new post will be shown at top.

4. Admin functionality given to superuser so that he/she can Users or Blog Posts  



  
