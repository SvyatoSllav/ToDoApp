# ToDo app
ToDo список дел с возможность добавления новых задач и их описания через веб интерфейс или через API.

### **Стек**
![python version](https://img.shields.io/badge/Python-3.7-green)
![django version](https://img.shields.io/badge/Django-2.2-green)
![pillow version](https://img.shields.io/badge/Pillow-8.3-green)
![pytest version](https://img.shields.io/badge/pytest-6.2-green)
![sorl-thumbnail version](https://img.shields.io/badge/thumbnail-12.7-green)

# Планы:
  * Реализовать систему регистрации и сделать так, чтобы у каждого пользователя был свой личный список.

# Установка
```
git clone https://github.com/evencatt/ToDoApp.git
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

# Документация по API будет доступна по адресу:
`http://127.0.0.1:8000/swagger/`
