# Тамагочи
____
## Описание проекта
Я создаю виртуальных питомцев и вы можете выбирать одного из них, 
заботиться о нем, кормить, следить за его состоянием.
____
## Функционал
1. **Выбор питомца**: вы сможете выбрать одного из нескольких питомцев.
2. **Кормление**: у вас будет возможность кормить питомца рахной едой, 
каждая из которых имеет свои характеристики.
3. **Мониторинг состояния**: у вас будет возможность следить за состоянием 
питомца (уровень голода, счастья и здоровья).
4. **Таймер бездействия**: если питомец не получает должного ухода, то он 
начинает терять здоровье.

____
### Классы
- **Атрибуты**:
#### 1. `User`
  - `username`: строка — имя пользователя.
  - `pet`: объект класса `Pet`, выбранный питомец.
#### 2. `Pet`

  - `name`: строка — имя питомца
  - `type`: строка — вид питомца
  - `hunger`: целое число — уровень голода питомца
  - `happiness`: целое число — уровень счастья питомца
  - `health`: целое число — уровень здоровья питомца

- **Методы**:
  - `feed(food)`: уменьшает уровень голода в зависимости от вида еды
  - `play()`: увеличивает уровень счастья питомца
  - `update_status()`: обновляет состояние питомца

#### 3. `Food`
  - `nutrition_value`: целое число — питательная ценность
#### 4. `Fun`
- `fun_value`: уровень счастья, которое получает питомец от игр
### Функции
- `create_pet()`: создания нового питомца
- `pet_status(pet_id)`: информация о текущем состоянии питомца
- `feed_pet(user, food_id)`: кормления питомца
- `update_pet_timer()`: отслеживания времени бездействия 
