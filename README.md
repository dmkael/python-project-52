### Hexlet tests and linter status:
[![Actions Status](https://github.com/dmkael/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dmkael/python-project-52/actions)
[![django-tests](https://github.com/dmkael/python-project-52/actions/workflows/my_workflow.yaml/badge.svg)](https://github.com/dmkael/python-project-52/actions/workflows/my_workflow.yaml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/30a8e8070441ff48b263/test_coverage)](https://codeclimate.com/github/dmkael/python-project-52/test_coverage)



---

### Task Manager
##### (Course project 4)
This web service provides a task management system. The service includes authentication and authorization mechanisms. Support for task statuses and labels has been implemented, as well as task assignment to executors. The service distinguishes between task authors with full permissions and other users with editing rights only. Task filtering capabilities are implemented within the task list. The service supports three localization languages: English, Russian, and Spanish. Manual language switching functionality is also implemented.

You can check its functionality and test it via the following link: [Task Manager](https://python-project-52-4ipl.onrender.com).

\
Installation and running instructions for the service:

<details>
<summary>1. System requirements</summary>

- Python 3.10 or above ([скачать](https://www.python.org/downloads/))
- GIT-client ([скачать](https://git-scm.com/downloads/))
- PostgreSQL server with database ([скачать](https://www.postgresql.org/download/))
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

  _NOTE: If the gendiff command are not available in your shell after installation for user, you’ll need to add the directory to your PATH. More info here:_
  _[Installing to the user documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-to-the-user-site)_

For the service to function, three environment variables are required:

- SECRET_KEY - for the application to operate (you can generate any value yourself)
- DATABASE_URL - The path to your prepared database as a Uniform Resource Identifier (URI): _postgres://{user}:{password}@{hostname}:{port}/{database-name}_
- ROLLBAR_ACCESS_TOKEN - with "access_token" value from Rollbar service.


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
  python3 $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/django_manage/manage.py migrate && python3 $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/django_manage/manage.py collectstatic
  
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
<summary>3. Запуск веб-сервиса</summary>

После установки веб-сервис готов к запуску. Вы можете опционально добавить переменную окружения __PORT__ для указания порта веб-сервиса.
В случае отсутствия переменной, используется значение по умолчанию __8000__. Запустить можно следующими командами:

- __Linux:__

  запуск c использованием __Django__ с отладкой:
  ```
  export DEBUG=True; python3 $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/django_manage/manage.py runserver localhost:8000
  ```
  запуск c использованием __gunicorn__:
  ```
  export PORT=${PORT:-8000}; gunicorn -w 4 -b 0.0.0.0:${PORT} task_manager.asgi:application -k uvicorn.workers.UvicornWorker
  ```

- __Windows:__

  запуск через __PowerShell__ c использованием __Django__ с отладкой:
  ```
  if (-not $env:DEBUG) {$env:DEBUG = "True"} $location = (pip show hexlet-code | Select-String -Pattern 'Location: (.*)' | ForEach-Object {
      if ($_.Matches.Count -gt 0) {
          $_.Matches[0].Groups[1].Value
      }
  }); $manager = "$location\task_manager\django_manage\manage.py"; py $manager runserver localhost:8000
  ```
  ОС Windows не поддерживает __gunicorn__, поэтому для запуска можно использовать __uvicorn__:
  Запуск через __PowerShell__ c использованием __uvicorn__:
  ```
  if (-not $env:PORT) {$env:PORT = "8000"} uvicorn --port=$env:PORT --workers=4 task_manager.asgi:application
  ```

Для остановки сервиса, запущенного через __guvicorn__ в Windows, небходимо сперва нажать сочетание клавиш __CTRL + BREAK__, а затем нажать сочетание клавиш __CTRL + C__. В остальных случаях остановить сервис можно сочетанием клавиш __CTRL + C__, либо закрытием окна терминала.
</details>

<details>
  <summary>4. Удаление</summary>
  
Для удаления сервиса введите в командной строке: 

- __Linux__:

    ```
  python3 -m pip uninstall hexlet-code
    ```

- __Windows__:

    ```
  py -m pip uninstall hexlet-code
    ```

</details>

Вы можете клонировать репозиторий себе и в дальнейшем развернуть его на хостинге. Имеющиеся команды в __Makefile__ могут быть вам полезны в отладке и в сборке. 


[Test version](https://python-project-52-4ipl.onrender.com/)
