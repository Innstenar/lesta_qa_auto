# Lesta Games
## Тестовое задание на позицию Trainee QA Automation Specialist в проект Мир Кораблей
**Задание 1. [pytest](https://github.com/Innstenar/lesta_qa_auto/tree/main/task_1)**</br>
**Задание 2. [ООП](https://github.com/Innstenar/lesta_qa_auto/tree/main/task_2)**

**[Подробное описание заданий](https://github.com/Innstenar/lesta_qa_auto/blob/main/tasks.md)**
## Инструкция по запуску

### Подготовка окружения
1. **Python**: Скачайте и установите [Python версии не ниже 3.9.8](https://www.python.org/downloads/).
2. **Добавление Python в переменную PATH**: Добавьте путь к папке с установленным Python в список значений переменной PATH. Это необходимо для того, чтобы можно было запускать Python из командной строки.
3. **Git**: Скачайте и установите [Git](https://git-scm.com/downloads).
4. **Добавление Git в переменную PATH**: Аналогично Python, добавьте путь к папке с установленным Git в список значений переменной PATH.

### Клонирование репозитория
5. Склонируйте данный репозиторий на свое устройство, выполнив следующую команду в командной строке (терминале):

   ```
   git clone https://github.com/Innstenar/lesta_qa_auto
   ```

### Установка зависимостей
6. Перейдите в корневую папку проекта <code>lesta_qa_auto</code>

   ```
   cd lesta_qa_auto
   ```

7. Установите необходимые зависимости, выполнив команду:

   ```
   pip install -r requirements.txt
   ```

<h2>Задание 1: Parser</h2>
<table>
    <thead>
        <tr>
            <th>Задача</th>
            <th>Команда</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Запуск скрипта parser.py</td>
            <td><code>python task_1/src/parser.py</code></td>
        </tr>
        <tr>
            <td>Запуск тестов test_parser.py</td>
            <td><code>cd task_1</code></br><code>pytest</code></td>
        </tr>
    </tbody>
</table>

<h2>Задание 2: 2D-движок (Engine2D)</h2>
<table>
    <thead>
        <tr>
            <th>Задача</th>
            <th>Команда</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Запуск скрипта engine2d.py</td>
            <td><code>python task_2/src/engine2d.py</code></td>
        </tr>
        <tr>
            <td>Запуск тестов test_engine2d.py</td>
            <td><code>cd task_2</code></br><code>pytest</code></td>
        </tr>
    </tbody>
</table>
