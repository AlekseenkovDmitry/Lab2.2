BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
    Класс, представляющий книгу.
    """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка формата 'Книга "название_книги"'.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        :return: Строка формата 'Book(id_=..., name=..., pages=...)'.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # Проверяем метод __str__

    # Дополнительно: проверяем метод __repr__
    for book in list_books:
        print(repr(book))
