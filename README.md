# Сервер для генерации ответов на различные задачи с помощью ИИ

## Основные функции

- принимает текстовые задания на русском (естественный язык) и различные параметры, на основании которых составляется запрос к языковой модели;
- возвращает пользователю ответ.

## Технологии:

- Язык программирования — **Python**
- Фреймвор — **Fastapi**
- LLM — **deepseek**

## Переменные окружения

Проект использует файл `.env` для хранения конфиденциальных данных. Пример содержимого файла:

```env
OPENAI_API_KEY=YOUR_OPENAI_API_KEY

```

- `OPENAI_API_KEY` - ключ для работы с моделью LLM.

## Установка проекта

1. **Склонируйте репозиторий**:

   ```bash
   git clone https://github.com/Viktori77/python_AI.git
   cd python_AI
   ```

2. **Не забудьте установить и активировать виртуальное окружение.**

Для windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Для linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Установите зависимости**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Получение API ключа, например**:

   4.1.

   ```bash
   https://openrouter.ai/settings/keys
   ```

   4.2. Нажать "Create API Key"

   4.3. Вписать Name

   4.4. Нажать "Create"

5. **Создайте файл `.env`** с вашими настройками (см. раздел "Переменные окружения").

6. **Запустите приложение**:
   ```bash
   python server.py
   ```
   или
   ```bash
   uvicorn server:app --host 0.0.0.0 --port 8002 --reload
   ```

## Зависимости

Проект использует следующие зависимости:

```text
asyncio==4.0.0
fastapi==0.128.0
uvicorn==0.40.0
python-decouple==3.8
openai==2.14.0
```

## Распознавание естественного языка:

Используется бесплатная модель LLM.

## Подход распознавания:

```
Запрос:
- вопрос от пользователя c нужными параметрами и правилами в формате:
```

```bash
class GenerateRequest(BaseModel):
    task: str
    name: str
    article: Optional[str] = ""
    characteristics: Optional[str] = ""
```

```
- формируется запрос, на основании которого получается ответ от модели LLM в формате:
```

```bash
class GenerateResponse(BaseModel):
    success: bool
    product: str
    generated_text: str
    original_request: Optional[Dict[str, Any]] = None

```
