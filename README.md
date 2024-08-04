# ISP Monitoring System (Flask)

### Краткое описание проекта:

Данная система построена на веб-фреймворке Flask,архитектура монолитная.<br/>
Так как БД в данном проекте не сильно нагружаетсязапросами, за основу была взята SQLite.<br/>
Система ICMP-мониторинга была реализована в видеdaemon-потока<br/>
Другие системы и утилиты были реализованы так же, в видеdaemon-потоков


### Цели проекта:

* Упростить для работников (операторов, техников, монтажников, сисадминов) использование ресурсов провайдера
* Централизованно мониторить состояние узлов, серверов
* Превратить не дружелюбные для техников и монтажников CLI интерфейсы в графические интерфесы (JS, HTML, CSS)
* Автоматизация рутинных процессов (например регистрация ONT Gpon терминалов)
* Создание системы поиска по логину из Billing системы, откуда физически клиент работает (порт сетевого коммутатора)
* Центральное хранилище конфигураций, прошивок сетевого оборудования
* Более удобная система helpdesk и дополнитеных заявок в отличии от существующей в провайдере


### Основные библиотеки и фреймворки проекта

![flask](https://img.shields.io/badge/Flask-v3.0.2-blue)
![sqlalchemy](https://img.shields.io/badge/SQLAlchemy-v2.0.25-blue)
![gunicorn](https://img.shields.io/badge/gunicorn-v22.0.0-blue)
![bs4](https://img.shields.io/badge/beautifulsoup4-v4.12.3-blue)
![alembic](https://img.shields.io/badge/alembic-v1.13.1-blue)
![icmplib](https://img.shields.io/badge/icmplib-v3.0.4-blue)
![paramiko](https://img.shields.io/badge/paramiko-v3.4.0-blue)


### Database
 ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### Static files, ssl, proxy
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)


### Простая схема архитектуры проекта
















