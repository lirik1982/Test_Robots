# R4C - Robots for consumers

<details>
  <summary>Задание из файла - 1</summary>
  R4C - Robots for consumers
  Небольшая предыстория.
Давным-давно, в далёкой-далёкой галактике, была компания производящая различных 
роботов. 

Каждый робот(**Robot**) имел определенную модель выраженную двух-символьной 
последовательностью(например R2). Одновременно с этим, модель имела различные 
версии(например D2). Напоминает популярный телефон различных моделей(11,12,13...) и его версии
(X,XS,Pro...). Вне компании роботов чаще всего называли по серийному номеру, объединяя модель и версию(например R2-D2).

Также у компании были покупатели(**Customer**) которые периодически заказывали того или иного робота. 

Когда роботов не было в наличии - заказы покупателей(**Order**) попадали в список ожидания.

Что делает данный код?
Это заготовка для сервиса, который ведет учет произведенных роботов,а также 
выполняет некие операции связанные с этим процессом.

Сервис нацелен на удовлетворение потребностей трёх категорий пользователей:
- Технические специалисты компании. Они будут присылать информацию
- Менеджмент компании. Они будут запрашивать информацию
- Клиенты. Им будут отправляться информация

 Как с этим работать?
- Создать для этого проекта репозиторий на GitHub
- Открыть данный проект в редакторе/среде разработки которую вы используете
- Ознакомиться с задачами в файле tasks.md
- Написать понятный и поддерживаемый код для каждой задачи 
- Сделать по 1 отдельному PR с решением для каждой задачи
- Прислать ссылку на своё решение
</details>

<details>
  <summary>Задание из файла - 2</summary>
Task 1. От технического специалиста компании.
Создать API-endpoint, принимающий и обрабатывающий информацию в формате JSON. 
В результате web-запроса на этот endpoint, в базе данных появляется запись 
отражающая информацию о произведенном на заводе роботе. 

_**Примечание от старшего технического специалиста**_: 
Дополнительно предусмотреть валидацию входных данных, на соответствие существующим в системе моделям.
Пример входных данных:
{"model":"R2","version":"D2","created":"2022-12-31 23:59:59"}
{"model":"13","version":"XS","created":"2023-01-01 00:00:00"}
{"model":"X5","version":"LT","created":"2023-01-01 00:00:01"}

Task 2. От директора компании
**User Story**: Я как директор хочу иметь возможность скачать по прямой ссылке Excel-файл со сводкой по суммарным показателям производства роботов за последнюю неделю. 
_**Примечание от менеджера**_. Файл должен включать в себя несколько страниц, на каждой из которых представлена информация об одной модели, но с детализацией по версии. 
Схематично для случая с моделью "R2":
|Модель|Версия|Количество за неделю|
|  R2  |  D2  |       32           |
|  R2  |  A1  |       41           |
|  R2  |  С8  |       99           |
Task 3. От клиента компании.
**Job story**: Если я оставляю заказ на робота, и его нет в наличии, я готов подождать до момента появления робота. После чего, пожалуйста пришлите мне письмо.
_**Примечание от менеджера**_: Письмо должно быть следующего формата
Добрый день!
Недавно вы интересовались нашим роботом модели X, версии Y. 
Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами
где Х и Y это соответственно модель и версия робота.

_**Примечание от старшего технического специалиста**_: 
Постарайтесь не переопределять встроенные методы модели. 
Также стремитесь не смешивать контексты обработки данных и бизнес-логику. 
Рекомендуется использовать механизм сигналов предусмотренный в фреймворке.
</details>

<details>
  <summary><h2>Мои комментарии</h2></summary>
  - валидация реализована с помощью инструмента django forms
  - несмотря на рекомендацию - не менять модели, к order был добавлен атрибут informed, для исключения двойного информирования клиента 
  
</details>

# В результате проделанной работы, реализован сервис бэка компании, производящей роботов.
Менеджер имеет возможность получать статистику о робатах произведенных за прошлую неделю.
Клиенты могут оставлять заказы, в случае отсутствия в наличии робота, в сервисе будет установлена автоматическая напоминалка, и в случае производства востребованного робота, клиенту будет отправлен email с приглашением в офис.

# Команды работы с сервисом:
- Создание новой записи о роботе:
```cmd
  curl "http://127.0.0.1:8000/api/v1/robots/new" --header "Content-Type: application/json" --data "{\"model\":\"O2\",\"version\":\"K2\",\"created\":\"2023-10-03 23:59:59\"}"
```
- Создание записи о новом клиенте:
```cmd
curl "http://127.0.0.1:8000/api/v1/customers/add" --header "Content-Type: application/json" --data-raw "{\"email\":\"IlonMask7@tesla.com\"}"}
```

- Создание записи о новом заказе:
```cmd
curl "http://127.0.0.1:8000/api/v1/orders/add" --header "Content-Type: application/json" --data-raw "{\"customer\":\"5\", \"robot_serial\": \"O2-K2\"}
```

- Получение отчета о готовых роботах за неделю по прямой ссылке:
```cmd
http://127.0.0.1:8000/api/v1/robots/report
```

# Также, можно импортировать файл robots.postman_collection.json в программу postman, и использовать готовые запросы
# Кроме того, для удобства, после клонирования репозитория, можно выполнить команду docker-compose up, и запустить готовый сервис







