from openai import AsyncOpenAI
import logging
from decouple import config
import asyncio

logging.basicConfig(
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат
    datefmt='%Y-%m-%d %H:%M:%S'  # Формат даты
)

logger = logging.getLogger(__name__)

OPENAI_API_KEY=config('OPENAI_API_KEY')

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENAI_API_KEY,
)

async def parse_with_openai(query: str) -> str:
        """Использование OpenAI для парсинга"""
        logger.info(f"Запрос доставлен: {query}")
        try:
            completion = await client.chat.completions.create(
                model="nex-agi/deepseek-v3.1-nex-n1:free",
                messages=
                    [
                            {"role": "user", "content": f"Вход: {query}"}
                        ],
            )
            result = completion.choices[0].message.content.strip()
            # Убираем возможные кавычки
            result = result.replace('```result', '').replace('```', '').strip()
            logger.info(f"Результат запроса: {result}")
            return result
        
        except Exception as e:
            logger.error(f"Ошибка OpenAI: {e}")


# Для тестирования
async def main():
    logger.info("Тестирование OpenAI API...")
    
    # Простой тест
    description = await parse_with_openai(
        "Газосиликатный блок" 
        
    )
    
    logger.info("СГЕНЕРИРОВАННОЕ ОПИСАНИЕ:")
    logger.info(description)

if __name__ == "__main__":
    asyncio.run(main())
            
    
    