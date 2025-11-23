""" Ejercicio """

class Singleton:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._data = {}   # diccionario interno
        return cls._instancia
    
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)

""" Extra """

class Session:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("New instance")
            cls._instance = super().__new__(cls)
            cls._instance._data = {}   # diccionario interno
        return cls._instance
    
    def session_set(self, id, username, name, email):
        self._data["id"] = id
        self._data["username"] = username
        self._data["name"] = name
        self._data["email"] = email
    
    def session_get(self):
        print(self._data)

    def session_del(self):
        self._data = {}

def main():
    user_session = Session()
    user_session.session_get()
    user_session.session_set(101, "jmanuel", "Jose Manuel", "jmanuel@correo.es")
    user_session.session_get()
    user_session.session_del()
    user_session.session_get()
    user_session = Session()
    user_session.session_set(101, "jmanuel", "Jose Manuel", "jmanuel@correo.es")
    user_session.session_get()

if __name__ == "__main__":
    main()

