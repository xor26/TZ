# TZ
Тестовое задание

### Task description
```
https://docs.google.com/document/d/1u_CrShWVJQ3i2kugx7w-f9-hBWR_4Ur9lOnN1tXyRpc/edit
```

### How to run
1. Install requirements with
```pip install requirements.txt ```
2. Run mongodb container with 
```docker-compose up```
3. Run celery with 
```celery -A tasks worker --loglevel=info```
4. Run flask with
```python main.py```
