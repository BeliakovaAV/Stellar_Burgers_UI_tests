## Дипломный проект. Задание 3: UI-тесты
<hr>

## Студент: Алевтина Белякова

## <h>Когорта: #18</h>
<hr>

## <h>Project: Stellar Burgers</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла          | Содержание файла               |
|-------------------------|--------------------------------|
| Tests dir               | Директория с тестами           |
| test_create_bookings.py | Тесты на создание бронирования |
| test_delete_booking.py  | Тесты на удаление бронирования |
| conftest.py             | Фикстуры                       |
| helpers.py              | Хэлпер для тела запросов       |
| data.py                 | Файл с URL и body запросов     |
| auth_methods.py         | http клиент к auth методам     |
| booking_methods.py      | http клиент к booking методам  |
| generators.py           | Генератор данных               |
| requirements.txt        | Файл с зависимостями           |
| allure_results.dir      | Папка с отчетами Allure        |

