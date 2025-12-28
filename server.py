from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from router import router 

@asynccontextmanager
async def lifespan(app: FastAPI):

  print("Сервер запускается...")
  yield
  
  print("Сервер останавливается...")


app = FastAPI(lifespan=lifespan,
    title="Generator tasks",
    description="API для генерации ответов на задания.",
    version="1.0.0",
    )

origins = [
   "http://localhost:5173",
   "http://127.0.0.1:5173",
   "http://localhost:8000",
    "http://127.0.0.1:8000",   
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["POST", "GET", "DELETE", "PUT"],
    allow_headers=["*"],
    max_age=3600, #Устанавливает время ожидания (TTL) для кэширования ответов CORS в браузере
    expose_headers=["Content-Disposition"],
)


app.include_router(router)

if __name__ == "__main__":    
    uvicorn.run(app, host="0.0.0.0", port=8002, log_level="info")