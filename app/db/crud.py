from app.db.models import Book, Category

def create_category(session, title: str) -> Category:
    category = Category(title=title)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def get_category(session, category_id: int) -> Category | None:
    return session.get(Category, category_id)


def get_categories(session) -> list[Category]:
    return session.query(Category).all()


def update_category(session, category_id: int, new_title: str) -> Category | None:
    category = session.get(Category, category_id)
    if category is None:
        return None
    category.title = new_title
    session.commit()
    session.refresh(category)
    return category


def delete_category(session, category_id: int) -> bool:
    category = session.get(Category, category_id)
    if category is None:
        return False
    session.delete(category)
    session.commit()
    return True

def create_book(
    session,
    title: str,
    description: str,
    price: float,
    category_id: int,
    url: str = "",
) -> Book:
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id,
    )
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def get_book(session, book_id: int) -> Book | None:
    return session.get(Book, book_id)


def get_books(session) -> list[Book]:
    return session.query(Book).all()


def get_books_by_category(session, category_id: int) -> list[Book]:
    return session.query(Book).filter(Book.category_id == category_id).all()


def update_book(session, book_id: int, **fields) -> Book | None:
    book = session.get(Book, book_id)
    if book is None:
        return None
    for key, value in fields.items():
        if hasattr(book, key):
            setattr(book, key, value)
    session.commit()
    session.refresh(book)
    return book


def delete_book(session, book_id: int) -> bool:
    book = session.get(Book, book_id)
    if book is None:
        return False
    session.delete(book)
    session.commit()
    return True