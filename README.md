### Hexlet tests and linter status:
[![Actions Status](https://github.com/dmkael/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dmkael/python-project-52/actions)
[![django-tests](https://github.com/dmkael/python-project-52/actions/workflows/my_workflow.yaml/badge.svg)](https://github.com/dmkael/python-project-52/actions/workflows/my_workflow.yaml)
[![Maintainability](https://api.codeclimate.com/v1/badges/30a8e8070441ff48b263/maintainability)](https://codeclimate.com/github/dmkael/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/30a8e8070441ff48b263/test_coverage)](https://codeclimate.com/github/dmkael/python-project-52/test_coverage)



---

### Task Manager
##### (Course project 4)
This Django web service provides a task management system. The service includes authentication and authorization mechanisms. Support for task statuses and labels has been implemented, as well as task assignment to executors. The service distinguishes between task authors with full permissions and other users with editing permissions only. Task filtering capabilities are implemented within the task list. The service supports three localization languages: English, Russian, and Spanish. Manual language switching functionality is also implemented.

You can check its functionality and test it via the following link: [Task Manager](https://python-project-52-4ipl.onrender.com).

\
Installation and running instructions for the service:

_You can copy and paste step by step all commands to execute them in command line interface_

<details>
<summary>1. System requirements</summary>

- Python 3.10 or above ([download](https://www.python.org/downloads/))
- GIT-client ([download](https://git-scm.com/downloads/))
- PostgreSQL server with database ([download](https://www.postgresql.org/download/))
- Account and active API-key for the error collector service ([Rollbar](https://rollbar.com/))
- Poetry ([Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer))

</details>

<details>
<summary>2. Installation steps</summary>
<br/>

Create folder where you want to install, navigate to that folder through __bash__ / __PowerShell__ and execute:
    
  ```
  git clone https://github.com/dmkael/python-project-52.git
  cd python-project-52
  
  ```

For the service to function, three environment variables are required:

1. __SECRET_KEY__ - for the application to operate (you can generate any value by yourself)
2. __DATABASE_URL__ - The path to your prepared database as a Unified Resource Identifier (URI): _postgres://{user}:{password}@{hostname}:{port}/{database-name}_
3. __ROLLBAR_ACCESS_TOKEN__ - "access_token" value from Rollbar service. You can provide any random value if this service is not necessary.


  You can use the `python-dotenv` package and specify variables in a `.env` file. Just create it in the root of the package and define variables in that file.
  Alternatively, you can set the variables directly in the operating system environment:
- __Linux (Ubuntu):__

  - Show available:
    ```
    printenv
    
    ```
  - Set for the user by specifying a value of MY_VAR=VALUE:
    ```
    echo MY_VAR=VALUE >> $HOME/.bashrc
    
    ```
  - Set for the system by specifying a value of MY_VAR=VALUE:
    ```
    sudo echo MY_VAR=VALUE >> /etc/environment
    
    ```
    _Alternatively, you can manually edit the specified files using a text editor like nano._


- __Windows:__
  - To run in the command line __cmd__ or __PowerShell__ as an administrator, or in the __Run__ menu, which opens with the __WIN + R__ keystroke combination (_Launching from the Run menu may start without administrator privileges, which prevents changing system variables_):
    ```
    rundll32.exe sysdm.cpl,EditEnvironmentVariables
    
    ```

After adding environment variables, you need to perform database migrations and collect static files in Django.:

- __Linux:__

  - execute in __bash__ (install performs in venv):
    ```
    source .venv/bin/activate
    make setup
    
    ```

- __Windows:__
  
  - execurte in __PowerShell__:
    ```
    poetry install
    poetry run py manage.py migrate
    poetry run py manage.py collectstatic --no-input
    
    ```

You optionally can specify allowed hosts and add some external hostnames/IP's in the `ALLOWED_HOSTS` section of the `settings.py` file for the service to function correctly besides the localhost:

- __Linux:__

  - execute in __bash__:
    ```
    nano task_manager/settings.py

    ```

- __Windows:__

  - execurte in __PowerShell__:
    ```
    notepad.exe task_manager/settings.py

    ```
Installation is now complete!
</details>

<details>
<summary>3. Start the web service</summary>

After installation, the web service is ready to be started. You can start it with the following commands:

- __Linux:__

  - run by __bash__ using __Django__:
    ```
    make dev
    
    ```
  - run by __bash__ using __gunicorn__:
    ```
    make gunicorn
    
    ```

- __Windows:__

  - run by __PowerShell__ using __Django__:
    ```
    poetry run py manage.py runserver 8000
    
    ```
  Since Windows does not support __gunicorn__, you can use __uvicorn__ for running the service.
  - run by __PowerShell__ usnig __uvicorn__:
    ```
    poetry run uvicorn --port=8000 --workers=4 task_manager.asgi:application
    
    ```

To stop a service running via __uvicorn__ on Windows, you need to first press __CTRL + BREAK__, and then press __CTRL + C__. In other cases, you can stop the service by pressing __CTRL + C__, or by closing the terminal window..
</details>

<details>
  <summary>4. Uninstall</summary>
  
To uninstall the service, use in the command line: 

```
poetry run pip uninstall hexlet-code -y

```

_THIS ONE ONLY FOR WINDOWS:_ Also, to clean created by Poetry virtual env folder in Windows you need to determine venv-name to delete. To figure it out just execute this command in project folder through __PowerShell__:
```
poetry env list

```
and find one which starts with __'hexlet-code-'__, copy that name and execute:
```
poetry env remove <venv_name>
```


To clean the rest just delete folder __python-project-52__

</details>

You can clone the repository and subsequently deploy it on a hosting service. The existing commands in the __Makefile__ may be useful to you for debugging and building.
