### Hexlet tests and linter status:
[![Actions Status](https://github.com/dmkael/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dmkael/python-project-52/actions)
[![django-tests](https://github.com/dmkael/python-project-52/actions/workflows/my_workflow.yaml/badge.svg)](https://github.com/dmkael/python-project-52/actions/workflows/my_workflow.yaml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/30a8e8070441ff48b263/test_coverage)](https://codeclimate.com/github/dmkael/python-project-52/test_coverage)



---

### Task Manager
##### (Course project 4)
Данный веб-сервис предоставляет систему управления задачами. В сервисе используется аутентификация и авторизация. Реализована поддержка статусов и меток для задач, а так же назначение исполнителя. Сервис имеет разграничение прав между авторами задач с полными правами и остальными пользователями с правами только на редактирование. В списке задач реализован инструмент филтрации задач по условиям. 

Проверить работу и протестировать можно по ссылке: [Task Manager](https://python-project-52-4ipl.onrender.com).

\
Инструкция по установке и запуску сервиса у себя:

<details>
<summary>1. Системные требования</summary>

- Python 3.10 или выше ([скачать](https://www.python.org/downloads/))
- GIT-клиент ([скачать](https://git-scm.com/downloads/))
- Сервер с базой данных PostgreSQL ([скачать](https://www.postgresql.org/download/))
- Учётная запись и действующий API-key в сервисе коллектора ошибок [Rollbar](https://rollbar.com/)

</details>

<details>
<summary>2. Порядок установки</summary>

- __Linux__:
  - для текущего пользователя:

      ```
    python3 -m pip install --user git+https://github.com/dmkael/python-project-52.git
      ```

  - в систему (использует встроенную версию Python) или в виртуальное окружение:

      ```
    python3 -m pip install git+https://github.com/dmkael/python-project-52.git
      ```

- __Windows__:
  - для текущего пользователя:

      ```
    py -m pip install --user git+https://github.com/dmkael/python-project-52.git
      ```

  - в систему или в виртуальное окружение:

      ```
    py -m pip install git+https://github.com/dmkael/python-project-52.git
      ```

  _ВНИМАНИЕ: При установке пакета "для пользователя" необходимо, чтобы каталог пользовательских пакетов был доступен в переменной PATH. Детальная информация здесь:_
  _[Installing to the user documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-to-the-user-site)_

Для работы сервиса необходимы две переменные окружения:

- SECRET_KEY - со значением секрета для работы приложения (можете любое значение сгенерировать сами)
- DATABASE_URL - путь к вашей подготовленной базе данных в виде унифицированного идентификатора ресурса (URI): _postgres://{user}:{password}@{hostname}:{port}/{database-name}_
- ROLLBAR_ACCESS_TOKEN - со значением "access_token" сервиса Rollbar


  Можно использовать пакет python-dotenv и указать переменные в файле .env в корне пакета.
  Либо прописать переменные в окружение ОС:
- __Linux (Ubuntu):__

  - Вывести имеющиеся
    ```
    printenv
    ```
  - задать для пользователя, указав значение вида MY_VAR=VALUE:
    ```
    echo MY_VAR=VALUE >> $HOME/.bashrc
    ```
  - задать для системы, указав значение вида MY_VAR=VALUE:
    ```
    sudo echo MY_VAR=VALUE >> /etc/environment
    ```
    _Либо можете прописать текстовым редактором, например, nano в указанные файлы вручную._


- __Windows:__
  - запустить в командной строке __cmd__ или __PowerShell__ от имени администратора, либо в меню __Выполнить__, которое открывается сочетанием клавиш __WIN + R__ (_При запуске через меню "Выполнить" может запуститься без прав администратора, что не позволит менять системные переменные_):
    ```
    rundll32.exe sysdm.cpl,EditEnvironmentVariables
    ```

После добавления переменных окружения нужно выполнить миграции в базу данных и собрать статические файлы Django:

- __Linux:__

  - запустить команду:
  ```
  python3 $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/django_manage/manage.py migrate && python3 $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/django_manage/manage.py collectstatic
  
  ```

- __Windows:__
  
  - запустить команду в __PowerShell__:
  ```
  <# apply migrations and collect static files #>
  $location = (pip show hexlet-code | Select-String -Pattern 'Location: (.*)' | ForEach-Object {
      if ($_.Matches.Count -gt 0) {
          $_.Matches[0].Groups[1].Value
      }
  }); $manager = "$location\task_manager\django_manage\manage.py"; Write-Output $manager; py "$manager" migrate; py "$manager" collectstatic --no-input

  ```

Так же необходимо прописать разрешённые хосты в разделе ALLOWED_HOSTS файла settings.py для работы сервиса:

- __Linux:__

  - запустить команду:
  ```
  nano $(pip show hexlet-code | grep -oP 'Location: \K.*')/task_manager/settings.py

  ```

- __Windows:__

  - запустить команду в __PowerShell__:
  ```
  $location = (pip show hexlet-code | Select-String -Pattern 'Location: (.*)' | ForEach-Object {
       if ($_.Matches.Count -gt 0) {
           $_.Matches[0].Groups[1].Value
       }
  }); notepad.exe $location\task_manager\settings.py;

  ```
На этом установка завершена!
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
  Запуск через __PowerShell__ c использованием __waitress__:
  ```
  if (-not $env:PORT) {$env:PORT = "8000"} uvicorn --port=$env:PORT --workers=4 task_manager.asgi:application
  ```

Остановить сервис можно сочетанием клавиш __CTRL + C__, либо закрытием окна терминала. Для остановки сервиса, запущенного через __guvicorn__ в Windows, небходимо сперва нажать сочетание клавиш __CTRL + BREAK__, а затем нажать сочетание клавиш __CTRL + C__
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
