"""  
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
"""

#Forma incorrecta
class MySQLDatabase:
    def connect(self):
        print("Conectando a MySQL...")

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # ⛔ UserService depende de MySQL directamente

    def get_user(self, user_id):
        self.db.connect()
        print(f"Obteniendo usuario {user_id}")

#Forma Correcta
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQLDatabase(Database):
    def connect(self):
        print("Conectando a MySQL...")

class PostgresDatabase(Database):
    def connect(self):
        print("Conectando a PostgreSQL...")


class UserService:
    def __init__(self, db: Database):  # depende de la interfaz, no del detalle
        self.db = db

    def get_user(self, user_id):
        self.db.connect()
        print(f"Obteniendo usuario {user_id}")


service = UserService(MySQLDatabase())
service.get_user(10)

# O cambiar por Postgres sin modificar UserService:
service = UserService(PostgresDatabase())
service.get_user(10)


"""  
 * DIFICULTAD EXTRA (opcional):
 * Crea un sistema de notificaciones.
 * Requisitos:
 * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 * Instrucciones:
 * 1. Crea la interfaz o clase abstracta.
 * 2. Desarrolla las implementaciones específicas.
 * 3. Crea el sistema de notificaciones usando el DIP.
 * 4. Desarrolla un código que compruebe que se cumple el principio.
"""

class NotificationService(ABC):
    @abstractmethod
    def notification_method(self, message: str):
        pass


class EmailNotification(NotificationService):
    def notification_method(self, message: str) -> None:
        print(f"Usando el servicio de email para enviar el mensaje: {message}")


class SMSNotification(NotificationService):
    def notification_method(self, message: str) -> None:
        print(f"Usando el servicio de sms para enviar el mensaje: {message}")


class PushNotification(NotificationService):
    def notification_method(self, message: str) -> None:
        print(f"Usando el servicio PUSH para enviar el mensaje: {message}")


class Notification:
    def __init__(self, notification: NotificationService) -> None:
        self.notification = notification

    def send_notification(self, message) -> str:
        return self.notification.notification_method(message)


def main():
    mensaje_test = "Esto es un mensaje de test"

    notificacion = Notification(EmailNotification())
    notificacion.send_notification(mensaje_test)

    notificacion = Notification(SMSNotification())
    notificacion.send_notification(mensaje_test)

    notificacion = Notification(PushNotification())
    notificacion.send_notification(mensaje_test)


if __name__ == "__main__":
    main()