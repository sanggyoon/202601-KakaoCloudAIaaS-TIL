# 다음 클래스를 구현하세요:
  # Book: 도서 정보(제목, 저자, ISBN, 출판연도 등)를 관리
  # Library: 도서 컬렉션을 관리하고 대출/반납 기능 제공
  # Member: 도서관 회원 정보와 대출 목록 관리

# 다음 기능을 구현하세요:
  # 도서 추가/삭제
  # 도서 대출/반납
  # 도서 검색 기능
  # 회원 등록/관리
  # 회원별 대출 현황 확인

# 객체 지향 설계 원칙(SOLID)을 최소한 2가지 이상 적용하세요.
# 적절한 캡슐화를 통해 데이터를 보호하세요.

class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self._is_rented = False

    def rent(self):
        if self._is_rented:
            raise ValueError("이미 대출 중인 도서입니다.")
        self._is_rented = True

    def return_book(self):
        self._is_rented = False

    def is_rented(self):
        return self._is_rented
    
class Member:
    def __init__(self, name):
        self.name = name
        self._borrowed_books = []

    def borrow(self, book: Book):
        self._borrowed_books.append(book)

    def return_book(self, book: Book):
        self._borrowed_books.remove(book)

    def borrowed_books(self):
        return list(self._borrowed_books)
    
class Library:
    def __init__(self):
        self._books = []
        self._members = []

    # ================= 회원 관리 =================
    def add_member(self, member: Member):
        self._members.append(member)

    def remove_member(self, member: Member):
        self._members.remove(member)

    # ================= 도서 관리 =================
    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, book: Book):
        if book.is_rented():
            raise ValueError("대출 중인 도서는 제거할 수 없습니다.")
        self._books.remove(book)

    # ================= 대출 / 반납 =================
    def rent_book(self, book: Book, member: Member):
        if book not in self._books:
            raise ValueError("도서관에 없는 책입니다.")
        if member not in self._members:
            raise ValueError("등록되지 않은 회원입니다.")

        book.rent()
        member.borrow(book)

    def return_book(self, book: Book, member: Member):
        member.return_book(book)
        book.return_book()

    # ================= 도서 검색 기능 =================

    def search_by_title(self, keyword):
        return [
            book for book in self._books
            if keyword.lower() in book.title.lower()
        ]

    def search_by_author(self, author_name):
        return [
            book for book in self._books
            if author_name.lower() in book.author.lower()
        ]

    def search_by_isbn(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def search_by_publication_year(self, year):
        return [
            book for book in self._books
            if book.publication_year == year
        ]

    # ================= 현황 출력 =================
    def print_status(self):
        print("=== 보유 도서 ===")
        for book in self._books:
            status = "대출 중" if book.is_rented() else "대출 가능"
            print(f"{book.title} ({status})")

        print("\n=== 회원 목록 ===")
        for member in self._members:
            print(member.name)

        print("\n=== 대출 현황 ===")
        for member in self._members:
            for book in member.get_borrowed_books():
                print(f"{member.name} → {book.title}")
        print("=== 보유 도서 ===")
        for book in self._books:
            status = "대출 중" if book.is_rented() else "대출 가능"
            print(f"{book.title} ({status})")

        print("\n=== 회원 목록 ===")
        for member in self._members:
            print(member.name)

        print("\n=== 대출 현황 ===")
        for member in self._members:
            for book in member.borrowed_books():
                print(f"{member.name} → {book.title}")
