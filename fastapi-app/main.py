from contextlib import asynccontextmanager
from core.models import db_helper
import uvicorn
from fastapi import FastAPI
from api import router as api_router
from core.config import settings
from fastapi.responses import ORJSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Запуск приложения
    yield
    # Остановка приложения
    print("Завершение приложения... stopping server... Done!  :D")
    await db_helper.dispose()  # Закрытие соединения с базой данных


main_app = FastAPI(
    default_response_class=ORJSONResponse,  # Использование ORJSONResponse для ускорения отправки JSON
    lifespan=lifespan,
)  # Инициализация FastAPI
main_app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app", reload=True, host=settings.run.host, port=settings.run.port
    )
