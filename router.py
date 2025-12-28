from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from nlp.query_parser import parse_with_openai 
import logging

logging.basicConfig(
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат
    datefmt='%Y-%m-%d %H:%M:%S'  # Формат даты
)
logger = logging.getLogger(__name__)


router = APIRouter(prefix="", tags=["Сгенерировать ответы на задания (например, описание товара)"])

class GenerateRequest(BaseModel):
    task: str
    name: str
    article: Optional[str] = ""
    characteristics: Optional[str] = ""

class GenerateResponse(BaseModel):
    success: bool
    product: str
    generated_text: str
    original_request: Optional[Dict[str, Any]] = None
    

@router.post("/generate")
async def generate(request: GenerateRequest) -> GenerateResponse:
    """Генерация описания товара"""
    try:
        logger.info(f"Получен запрос из 1С:")
        logger.info(f"   Задача: {request.task}")
        logger.info(f"   Название: {request.name}")
        logger.info(f"   Артикул: {request.article}")
        logger.info(f"   Характеристики: {request.characteristics}")
        
        # Формируем текст запроса для нейросети в нужном формате
        query_text = (
            f"Задача: {request.task} | "
            f"Название товара: {request.name} | "
            f"Артикул: {request.article} | "
            f"Характеристики: {request.characteristics} | "
        )
        
        logger.info(f"Запрос для нейросети: {query_text}")
        
        # Вызываем нейросеть
        result = await parse_with_openai(query_text)
        
        return GenerateResponse(
            success=True,
            product=request.name,
            generated_text=result,
            original_request={
                "task": request.task,
                "name": request.name,
                "article": request.article,
                "characteristics": request.characteristics
            }
        )
        
    except Exception as e:
        logger.info(f" Ошибка: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка генерации: {str(e)}")
