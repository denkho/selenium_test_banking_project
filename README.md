# Тестовое задание на позицию SDET

## Для запуска тестов

1. Откройте терминал. Перейдите в папку, куда планируете клонировать репозиторий. Клонируйте репозиторий на локальную машину с помощью команды в терминале:
    ```
    git clone https://github.com/denkho/selenium_test_banking_project.git
    ```

2. Если на локальной машине не установлен Python, то скачайте его с официального сайта https://www.python.org/downloads/ и установите.

3. На локальной машине перейдите в раздел с клонированным репозиторием, установите виртуальное окружение и активируйте его. 
Для Windows команды будут следующие:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```
    Для Linux:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Установите требуемые зависимости из файла requirements.txt командой:
    ```
    pip install -r requirements.txt
    ```
5. Если у вас не скачан Selenium Server, то скачайте файл jar сервера из [последнего релиза](https://github.com/SeleniumHQ/selenium/releases/latest)

6. Запустите Grid командой:
    ```
    java -jar selenium-server-<version>.jar standalone
    ```

6. Запустите все тесты командой (для этого необходимо находиться в корневой папке проекта):
    ```
    pytest --alluredir=reports
    ```

7. После завершения тестов для того, чтобы сгенерировать отчет Allure, выполните команду:
    ```
    allure serve reports
    ```
    Эта команда откроет локальный веб-сервер и покажет сгенерированный отчет в браузере.
