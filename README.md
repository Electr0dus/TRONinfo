# TRON info

Микросервис для получения информации по адрессу в сети трон

## Информация получаемая при запросе

- Bandwidth
- Energy
- Баланс TRX

## Установка

1. Скопируйте все файлы проекта в рабочую директорию

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env с необходимыми переменными:
```env
API_KEY=ВАШ КЛЮЧ ДЛЯ РАБОТЫ С СЕТЬЮ TRON
```

5. Запустите работу сервера:
```bash
python main.py
```
