# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

Сайт позволяет просматривать посещения, совершаемые в хранилище. По имени владельца пропуска просматривается история всех его посещений с указанием их продолжительностей. Каждый пропуск имеет уникальный код доступа. Каждое посещение продолжительностью от 1 часа и более является подозрительным, и на него ставится  метка UNDER SUSPICION. 

### Как установить

Запросите доступ к БД у менеджера вашего банка. Для доступа вам понадобятся хост, порт, имя БД, имя пользователя, пароль, а также секретный ключ и бэкэнд ДБ для использования.
Создайте файл `.env` в директории файла `settings.py`. Для отключения отладочного режима добавьте в файл `.env` запись `DEBUG=False` (для включения режима отладки замените `False` на `True`), а также полученные у менеджера необходимые данные в следующем формате:
```
DATABASE_URL=postgres://имя_пользователя:пароль@хост:порт/имя_БД
SECRET_KEY=секретный_ключ
DEBUG=False
```
Не используйте кавычки, скобки или пробелы.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить
Для того, чтобы сайт работал, необходимо открыть интерпретатор командной строки и ввести следующую команду:
```
$ python3 manage.py runserver 0.0.0.0:8000
```
Пример успешного запуска :
```
$ python3 manage.py runserver 0.0.0.0:8000
Performing system checks...

System check identified no issues (0 silenced).
January 18, 2020 - 19:59:53
Django version 1.11.2, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.
```
Для открытия сайта в браузере в качестве адреса введите [localhost:8000](http://localhost:8000/).
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
