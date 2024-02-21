from fastapi import FastAPI, Body, Path
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
  id: int
  title: str
  author: str
  publisher: str

books = []  # List to store books (later)


def __repr__(self):
    return f"Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})"

books = ["/books"]  # List to store books

##function to create books
@app.post("/books")
async def create_book(book: Book):
  book.id = len(books) + 1
  books.append(book)
  return {"message": "Book created", "book": book}

##function to read the books
@app.get("/books")
async def get_all_books():
  return {"books": books}

if __name__ == "__main__":
  app.run(debug=True)