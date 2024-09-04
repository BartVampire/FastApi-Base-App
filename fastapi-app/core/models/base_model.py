from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

from utils import camel_case_to_snake_case


class BaseModel(DeclarativeBase):
    """
    Базовая модель для всех других моделей:
    1) Метод __abstract__ для объявления модели будет считаться абстрактной.
    2) Преобразуем имя модели в snake_case для создания таблицы и добавляем s в конце имени таблицы.
    3) Добавляем поле id (Primary Key) с типом int
    """

    __abstract__ = True  # Модель не будет создана в базе данных

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"  # Преобразуем имя модели в snake_case

    id: Mapped[int] = mapped_column(primary_key=True)  # Первичный ключ (Primary Key)
