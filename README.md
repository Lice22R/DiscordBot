Инструкция для запуска:
1. Загружаем проект из github
2. Создаем витуальное окружение командой "python -m venv venv" или "vertualenv venv"
3. Активируем вируальное окружение. Windows: "venv\Scripts\activate.bat", Linux: "source venv/bin/activate.bat"
4. Устанавливаем зависимости "pip install -r requirements.txt"
5. Создаем файл с названием ".env" с данным содержанием:

APPLICATION_ID=ТВОИ_ДАННЫЕ
PUBLIC_KEY=ТВОИ_ДАННЫЕ
CLIENT_SECRET=ТВОИ_ДАННЫЕ
TOKEN=ТВОИ_ДАННЫЕ

6. Запускаем и радуемся