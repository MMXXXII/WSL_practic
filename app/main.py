import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db import crud
from app.db.db import get_session


def main():
    session = get_session()

    try:
        categories = crud.get_categories(session)

        if not categories:
            print("В базе данных нет категорий. Сначала запустите app/init_db.py")
            return

        for category in categories:
            print(f"Категория: {category.title} (id={category.id})")
            books = crud.get_books_by_category(session, category.id)

            if not books:
                print("  Книг в этой категории пока нет.")
            for book in books:
                print(f"  - {book.title} | {book.price} руб. | {book.description}")
            print()
    finally:
        session.close()


if __name__ == "__main__":
    main()