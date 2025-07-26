# LEENS
## Описание
Микросервисное приложение, моделирующее закупку рекламы.

Проект для мини курса "Микросервисное взаимодействие" в рамках летней технологической практики ВШЭ, 2 курс.

## Требования
- docker
- docker-compose

## Запуск
### Клонирование репозитория (URL)
```
git clone https://github.com/Andromeddda/leens/ && cd leens/
```

### Сборка образов
```
docker compose build
```

### Запуск контейнеров
```
docker compose up
```

### Запуск в фоновом режиме
```
docker compose up -d
```

### Остановка приложения, запущенного в фоновом режиме
```
docker compose stop
```

## Примеры взаимодействия (cURL)
### Создание пользователя
```
curl -X POST http://localhost:8082/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "Daniel",
    "role": "advertiser"
}'
```

### Получение всех пользователей-рекламодателей
```
curl "http://localhost:8082/users/?user_role=advertiser"
```

### Получение всех каналов
```
curl http://localhost:8081/channels/
```

### Получение всех заказов
```
curl http://localhost:8081/orders/
```
