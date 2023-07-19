# somsagram

![image](https://github.com/mirafzal114/somsagram/assets/136591233/117f4bea-cb53-4cf8-8624-7be4018eda23)


## SomSaGraM

SomsaGram - это приложение, которое позволяет пользователям  добавить посты посишать чужый посты  отрыть профиль редактировать  делитья  с рисунками 


**Пример программы так работает.**

## Особенности
- Создание списков дел с уникальными именами.
- Добавление постов.
- Посищать другие посты.
- Удаление и редактирование текстов.
- Отображение даты и времени постов.
- Редактирование профиля.

## Установка

**Для установки программы, выполните следующие шаги:**

1. Установите Python на вашу систему, если он еще не установлен. Вы можете скачать Python с официального сайта: https://www.python.org/downloads/

2. Клонируйте репозиторий с программой на вашу локальную машину:
 ```bash
$  git clone https://github.com/mirafzal114/somsagram.git
```

3. Перейдите в директорию с программой:
cd Todo_App 

## Использование

**После того, как вы загрузили django, перейдите в каталог клонированного репо и выполните следующую команду**
```bash
$ python manage.py makemigrations
```

**Это создаст все файлы миграции (миграции базы данных), необходимые для запуска этого приложения.**

**Теперь, чтобы применить эту миграцию, выполните следующую команду**
```bash
$ python manage.py migrate
```
**Один последний шаг, и тогда наше приложение todo будет запущено. Нам нужно создать пользователя-администратора для запуска этого приложения. В терминале введите следующую команду и укажите имя пользователя, пароль и адрес электронной почты для пользователя-администратора.**
```bash
$ python manage.py createsuperuser
```
 **Запустите программу с помощью команды:**
```bash
$ python manage.py runserver
```



## Дополнительные ресурсы
- **Документация Django:** https://docs.djangoproject.com/



