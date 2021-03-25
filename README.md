# MSDavid - Sun Asterisk Coding Exam 
Sun Asterisk Coding Exam by Michael Steven N. David

**In order to install a fresh copy of this, you should meet the requirements stated below**
- Python _**3.7**_/_**3.8**_
- PostGresSQL
- A database on PostGresSQL named "sunAsterisk"
- Virtual Env (Guide for Virtual Envs https://docs.djangoproject.com/en/3.1/howto/windows/)
- Git

#For Development

**If all requirements are made, follow the instructions below to have a fresh copy of the project**
1. Clone the project's repository to your desired folder location 
(**Do take note you should be inside your created virtual environment**)
2. Make a virtual environment using the CLI or thru your preferred IDE

    CLI: (Be in the project root folder from CLI)
    ```
    C:\Projects\sunAsterisk> py -m venv venv
   ```
3. Let's install the packages required by the project thru CLI or thru your preferred IDE
    
    Go inside the virtual environment
   ```
   C:\Projects\sunAsterisk> call venv\Scripts\activate
   (venv) C:\Projects\sunAsterisk> python -m pip install --force-reinstall pip
   ```
   Lets upgrade also setuptools to have no complications on installing the other packages
   ```
   (venv) C:\Projects\sunAsterisk> easy_install --upgrade setuptools
   ```
   Let's check the pip version and it must be the latest around v21.0.1
   ```
   (venv) C:\Projects\sunAsterisk> pip --version
   ```
   Make sure to check, if it's not updated then update pip with "pip install --force-reinstall pip"
   
   Let's install the packages now
   ```
   (venv) C:\Projects\sunAsterisk> pip install -r requirements.txt
   ```
   
   If error occurred, then go back to step 3 and make sure everything's correct
4. In **DATABASES** part in _settings.py_ change to whatever you have the User and Password of your PostGresSQL
5. Type in console `python manage.py migrate`
    
    If ever an error occurred, please refer back to the steps above and do it again
6. Check in database if the models were successfully migrated
7. Run the project either by pycharm on the right top corner play button or by typing `python manage.py runserver` on the CLI
