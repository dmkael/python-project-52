### Hexlet tests and linter status:
[![Actions Status](https://github.com/dmkael/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dmkael/python-project-52/actions)
[![django-tests](https://github.com/dmkael/python-project-52/actions/workflows/my_workflow.yaml/badge.svg)](https://github.com/dmkael/python-project-52/actions/workflows/my_workflow.yaml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/30a8e8070441ff48b263/test_coverage)](https://codeclimate.com/github/dmkael/python-project-52/test_coverage)



---

### Task Manager
##### (Course project 4)
This Django web service provides a task management system. The service includes authentication and authorization mechanisms. Support for task statuses and labels has been implemented, as well as task assignment to executors. The service distinguishes between task authors with full permissions and other users with editing permissions only. Task filtering capabilities are implemented within the task list. The service supports three localization languages: English, Russian, and Spanish. Manual language switching functionality is also implemented.

You can check its functionality and test it via the following link: [Task Manager](https://python-project-52-4ipl.onrender.com).

\
Installation and running instructions for the service:

<details>
<summary>1. System requirements</summary>

- Python 3.10 or above ([download](https://www.python.org/downloads/))
- GIT-client ([download](https://git-scm.com/downloads/))
- PostgreSQL server with database ([download](https://www.postgresql.org/download/))
- Account and active API-key for the error collector service [Rollbar](https://rollbar.com/)

</details>

<details>
<summary>2. Installation steps</summary>

- __Linux__:
  - for current user:

      ```
    python3 -m pip install --user git+https://github.com/dmkael/python-project-52.git
      ```

  - to the system (using the built-in Python version) or to a virtual environment:

      ```
    python3 -m pip install git+https://github.com/dmkael/python-project-52.git
      ```

- __Windows__:
  - for current user:

      ```
    py -m pip install --user git+https://github.com/dmkael/python-project-52.git
      ```

  - to the system (using the built-in Python version) or to a virtual environment:

      ```
    py -m pip install git+https://github.com/dmkael/python-project-52.git
      ```

  _NOTE: During installation of the package "for user," it's necessary for the user-specific package directory to be accessible in the PATH variable. Detailed information:_
  _[Installing to the user documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-to-the-user-site)_

For the service to function, three environment variables are required:

1. __SECRET_KEY__ - for the application to operate (you can generate any value yourself)
2. __DATABASE_URL__ - The path to your prepared database as a Unified Resource Identifier (URI): _postgres://{user}:{password}@{hostname}:{port}/{database-name}_
3. __ROLLBAR_ACCESS_TOKEN__ - with "access_token" value from Rollbar service.


  You can use the `python-dotenv` package and specify variables in a `.env` file located in the root of the package.
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

  - run command:
    ```
    python3 $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/django_manage/manage.py migrate && python3 $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/django_manage/manage.py collectstatic --no-input
  
    ```

- __Windows:__
  
  - run command in __PowerShell__:
    ```
    <# apply migrations and collect static files #>
    $location = (pip show hexlet-code | Select-String -Pattern 'Location: (.*)' | ForEach-Object {
        if ($_.Matches.Count -gt 0) {
            $_.Matches[0].Groups[1].Value
        }
    }); $manager = "$location\task_manager\django_manage\manage.py"; Write-Output $manager; py "$manager" migrate; py "$manager" collectstatic --no-input

    ```

You also need to specify allowed hosts in the `ALLOWED_HOSTS` section of the `settings.py` file for the service to function correctly.:

- __Linux:__

  - run command:
    ```
    nano $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/settings.py

    ```

- __Windows:__

  - run command in __PowerShell__:
    ```
    $location = (pip show hexlet-code | Select-String -Pattern 'Location: (.*)' | ForEach-Object {
         if ($_.Matches.Count -gt 0) {
             $_.Matches[0].Groups[1].Value
         }
    }); notepad.exe $location\task_manager\settings.py;

    ```
Installation is now complete!
</details>

<details>
<summary>3. Start the web service</summary>

After installation, the web service is ready to be started. Optionally, you can set the environment variable __PORT__ to specify the port for the web service. If the variable is not set, the default value of __8000__ will be used. You can start it with the following commands:

- __Linux:__

  - run using __Django__ using debugging:
    ```
    export DEBUG=True; python3 $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/django_manage/manage.py runserver localhost:8000
    ```
  - run using __gunicorn__:
    ```
    export PORT=${PORT:-8000}; gunicorn -w 4 -b 0.0.0.0:${PORT} task_manager.asgi:application -k uvicorn.workers.UvicornWorker
    ```

- __Windows:__

  - run using __PowerShell__ with __Django__ using debugging:
    ```
    if (-not $env:DEBUG) {$env:DEBUG = "True"} $location = (pip show hexlet-code | Select-String -Pattern 'Location: (.*)' | ForEach-Object {
        if ($_.Matches.Count -gt 0) {
            $_.Matches[0].Groups[1].Value
        }
    }); $manager = "$location\task_manager\django_manage\manage.py"; py $manager runserver localhost:8000
    ```
  Since Windows does not support __gunicorn__, you can use __uvicorn__ for running the service.
  - run using __PowerShell__ with __uvicorn__:
    ```
    if (-not $env:PORT) {$env:PORT = "8000"} uvicorn --port=$env:PORT --workers=4 task_manager.asgi:application
    ```

To stop a service running via __uvicorn__ on Windows, you need to first press __CTRL + BREAK__, and then press __CTRL + C__. In other cases, you can stop the service by pressing __CTRL + C__, or by closing the terminal window..
</details>

<details>
  <summary>4. Uninstall</summary>
  
To uninstall the service, use in the command line: 

- __Linux__:

    ```
    python3 -m pip uninstall hexlet-code
    ```

- __Windows__:

    ```
    py -m pip uninstall hexlet-code
    ```

</details>

You can clone the repository and subsequently deploy it on a hosting service. The existing commands in the __Makefile__ may be useful to you for debugging and building.
