import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db import crud
from app.db.db import get_session, init_db


def seed_data():
    init_db()
    session = get_session()

    try:
        fiction = crud.create_category(session, "Художественная литература")
        science = crud.create_category(session, "Научная литература")

        crud.create_book(
            session,
            title="Мастер и Маргарита",
            description="Роман Михаила Булгакова",
            price=650.0,
            category_id=fiction.id,
        )
        crud.create_book(
            session,
            title="Преступление и наказание",
            description="Роман Фёдора Достоевского",
            price=590.0,
            category_id=fiction.id,
        )
        crud.create_book(
            session,
            title="Война и мир",
            description="Роман-эпопея Льва Толстого",
            price=890.0,
            category_id=fiction.id,
        )

        crud.create_book(
            session,
            title="Краткая история времени",
            description="Стивен Хокинг о космологии",
            price=720.0,
            category_id=science.id,
        )
        crud.create_book(
            session,
            title="Происхождение видов",
            description="Чарльз Дарвин о теории эволюции",
            price=540.0,
            category_id=science.id,
        )

        print("База данных успешно наполнена тестовыми данными.")
    finally:
        session.close()


if __name__ == "__main__":
    seed_data()