from fastapi import FastAPI

from app.api import books, categories
from app.db.db import init_db

app = FastAPI(
    title="Octagon Bookstore API",
    description="Простое API для управления книгами и категориями",
    version="1.0.0",
)

app.include_router(categories.router)
app.include_router(books.router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}