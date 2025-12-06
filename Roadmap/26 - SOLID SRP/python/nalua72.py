""" 
Ejercicio:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 """

# Forma incorrecta

class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        # Lógica de negocio
        return sum(self.data) / len(self.data)

    def save_to_file(self, filename):
        # Responsabilidad de persistencia
        with open(filename, "w") as f:
            f.write(str(self.data))

    def print_report(self):
        # Responsabilidad de presentación
        print("Datos:", self.data)

# Forma correcta

class ReportCalculator:
    def calculate_statistics(self, data):
        return sum(data) / len(data)

class ReportSaver:
    def save(self, filename, data):
        with open(filename, "w") as f:
            f.write(str(data))

class ReportPrinter:
    def print(self, data):
        print("Datos:", data)

"""  
DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
 """

# Clase que no cumple el principio de SRP

class MessyLibrary():
    
    def __init__(self):
        self.books_db = []
        self.users_db = []
        self.loans_db = []

    def book_register(self, title: str, author: str, copies: int) -> None:
        if self._is_book(author):
            print(f"Libro {title} ya registrado")
            return
        self.books_db.append({"titulo": title, "autor": author, "copias": copies})


    def user_register(self, user_name: str, user_id: int, user_email: str) -> None:
        if self._is_user(user_id):
            print(f"Usuario {user_name}, ya esta registrado")
            return
        self.users_db.append({"nombre": user_name, "numero_identificacion": user_id, "correo electronico": user_email})


    def book_loan(self, book_title: str, user_name: str) -> None:
        if not self._is_user(user_name):
            print(f"El usuario {user_name} no está registrado")
            return
        
        if not self._is_book(book_title):
            print(f"No existe el libro {book_title}")
            return
        
        book = self.get_book(book_title)
        if book["copias"] > 0:
            print(f"{book_title} prestado a {user_name}")
            book["copias"] -= 1
            self.loans_db.append({"prestamo": book_title, "usuario": user_name})
            return
        print(f"No hay copias disponibles de {book_title}")
        return
    

    def book_return(self, book_title: str) -> None:
        if not self._is_loan(book_title):
            print(f"El libro {book_title} no está prestado")
            return
        
        for ind, book in enumerate(self.books_db):
            if book["titulo"] == book_title:
                print(f"{book_title} devuelto")
                book["copias"] += 1
                del self.loans_db[ind]
                return
        return


    def _is_user(self, user_name) -> bool:
        return any(u["nombre"] == user_name for u in self.users_db)


    def _is_book(self, book_title) -> bool:
        return any(b["titulo"] == book_title for b in self.books_db)

 
    def _is_loan(self, book_title) -> bool:
        return any(b["prestamo"] == book_title for b in self.loans_db)
    

    def get_book(self, title) -> str | None:
        for book in self.books_db:
            if book["titulo"] == title:
                return book
        return None


#Refactorizar el codigo para que cumpla SPR

class Library():

    def __init__(self):
        self.books = BooksManagement()
        self.users = UsersManagement()
        self.loans = LoanService(self.books, self.users)

class BooksManagement():

    def __init__(self):
        self.books_db = []

    def register(self, title: str, author: str, copies: int) -> None:
        if self._is_book(title):
            print(f"Libro {title} ya registrado")
            return
        self.books_db.append({"titulo": title, "autor": author, "copias": copies})

    def _is_book(self, book_title) -> bool:
        return any(b["titulo"] == book_title for b in self.books_db)


class UsersManagement():

    def __init__(self):
        self.users_db =  []


    def register(self, user_name: str, user_id: int, user_email: str) -> None:
        if self._is_user(user_name):
            print(f"Usuario {user_name}, ya esta registrado")
            return
        self.users_db.append({"nombre": user_name, "numero_identificacion": user_id, "correo electronico": user_email})

    def _is_user(self, user_name) -> bool:
        return any(u["nombre"] == user_name for u in self.users_db)


class LoanService():

    def __init__(self, book_class: BooksManagement, user_class: UsersManagement) -> None:
        self.loans_db = []
        self.book_class = book_class
        self.user_class = user_class

    def book_loan(self, title: str, user_name: str) -> None:
        if not self.user_class._is_user(user_name):
            print(f"El usuario {user_name} no está registrado")
            return
        
        if not self.book_class._is_book(title):
            print(f"No existe el libro {title}")
            return
        
        book = self.get_book(title)
        if book["copias"] > 0:
            print(f"{title} prestado a {user_name}")
            book["copias"] -= 1
            self.loans_db.append({"prestamo": title, "usuario": user_name})
            return
        print(f"No hay copias disponibles de {title}")
        return
    

    def book_return(self, book_title: str) -> None:
        if not self._is_loan(book_title):
            print(f"El libro {book_title} no está prestado")
            return
        
        for ind, book in enumerate(self.book_class.books_db):
            if book["titulo"] == book_title:
                print(f"{book_title} devuelto")
                book["copias"] += 1
                del self.loans_db[ind - 1]
                return
        return


    def get_book(self, title) -> str | None:
        for book in self.book_class.books_db:
            if book["titulo"] == title:
                return book
        return None
    
    
    def _is_loan(self, book_title) -> bool:
        return any(b["prestamo"] == book_title for b in self.loans_db)

def main():
    #Examples using no RPS class
    biblioteca1 = MessyLibrary()
    biblioteca1.book_register("La isla del tesoro", "Robert l. Stevenson", 4)
    biblioteca1.book_register("Moby Dick", "Hermann Melville", 2)
    biblioteca1.user_register("Jose Rodriguez", 101, "jrodriguez@test.com")
    biblioteca1.user_register("Isabel Vara", 102, "ivara@test.com")
    print(biblioteca1.books_db)
    print(biblioteca1.users_db)
    biblioteca1.book_loan("Moby Dik", "Jose Rodriguez")
    biblioteca1.book_loan("Moby Dick", "Juan Rodriguez")
    biblioteca1.book_loan("Moby Dick", "Jose Rodriguez")
    biblioteca1.book_loan("La isla del tesoro", "Isabel Vara")
    print(biblioteca1.books_db)
    print(biblioteca1.loans_db)
    biblioteca1.book_return("Moby Dick")
    print(biblioteca1.books_db)
    print(biblioteca1.loans_db)

    #Examples using no RPS class
    print(f"\t*******************************")
    biblioteca2 = Library()
    biblioteca2.books.register("Anatomia de un instante", "Javier Cercas", 3)
    biblioteca2.books.register("Las bicicletas son para el verano", "Fernando Fernan Gomez", 2)
    biblioteca2.books.register("Las bicicletas son para el verano", "Fernando Fernan Gomez", 2)
    print(biblioteca2.books.books_db)
    biblioteca2.users.register("Saul Rodriguez", 103, "srodriguez@test.com")
    biblioteca2.users.register("Alberto Torices", 104, "atorices@test.com")
    biblioteca2.users.register("Alberto Torices", 104, "atorices@test.com")
    print(biblioteca2.users.users_db)
    biblioteca2.loans.book_loan("Las bicicletas son para el verano", "Saul Rodriguez")
    biblioteca2.loans.book_loan("Anatomia de un instante", "Alberto Torices")
    biblioteca2.loans.book_loan("Anatomia de un instante", "Alberto orices")
    biblioteca2.loans.book_loan("El Quijote", "Saul Rodriguez")
    print(biblioteca2.books.books_db)
    print(biblioteca2.loans.loans_db)
    biblioteca2.loans.book_return("Las bicicletas son para el verano")
    print(biblioteca2.books.books_db)
    print(biblioteca2.loans.loans_db)

if "__name__" == "__name__":
    main()