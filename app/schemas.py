"""Pydantic request/response schemas."""
from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class UserCreate(BaseModel):
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$", max_length=255)
    full_name: str = Field(min_length=1, max_length=120)
    password: str = Field(min_length=8, max_length=128)


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    full_name: str
    is_librarian: bool


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class BookBase(BaseModel):
    isbn: str = Field(min_length=10, max_length=20)
    title: str = Field(min_length=1, max_length=255)
    author: str = Field(min_length=1, max_length=255)
    published_year: int | None = Field(default=None, ge=0, le=2100)


class BookCreate(BookBase):
    total_copies: int = Field(default=1, ge=1, le=1000)


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    author: str | None = Field(default=None, min_length=1, max_length=255)
    published_year: int | None = Field(default=None, ge=0, le=2100)
    total_copies: int | None = Field(default=None, ge=1, le=1000)


class BookOut(BookBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    total_copies: int
    available_copies: int


class BookPage(BaseModel):
    items: list[BookOut]
    total: int
    page: int
    size: int


class LoanOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    book: BookOut
    borrowed_on: date
    due_on: date
    returned_on: date | None
    is_overdue: bool = False
