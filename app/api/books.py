from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import crud
from app.db.db import get_db
from app.schemas import BookCreate, BookResponse, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[BookResponse])
def list_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    if category_id is not None:
        category = crud.get_category(db, category_id)
        if category is None:
            raise HTTPException(status_code=404, detail="Категория не найдена")
        return crud.get_books_by_category(db, category_id)
    return crud.get_books(db)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, book.category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Указанная категория не найдена")

    return crud.create_book(
        db,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url or "",
    )


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    existing = crud.get_book(db, book_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    update_data = book.model_dump(exclude_unset=True)

    if "category_id" in update_data:
        category = crud.get_category(db, update_data["category_id"])
        if category is None:
            raise HTTPException(status_code=404, detail="Указанная категория не найдена")

    updated = crud.update_book(db, book_id, **update_data)
    return updated


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return None