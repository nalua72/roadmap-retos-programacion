class usuario:
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age= edad

    def __repr__(self):
        return f"Nombre: {self.name}, Edad: {self.age}"
    

usuario1 = usuario("jose", 53)
usuario2 = usuario("saul", 14)

print(usuario1)
print(usuario2)

""" EXTRA """

def main():
    class Stack:
        def __init__(self):
            self.stack = []

        def push(self, element):
            self.stack.append(element)

        def pop(self):
            if len(self.stack) > 0:
                self.stack.pop()
            else:
                print("Pila vacia")

        def count(self):
            print(f"El tamaño de la pila es: {len(self.stack)} elementos")

        def __repr__(self):
            return str(self.stack)
    
    class Queue:
        def __init__(self):
            self.queue = []

        def inqueue(self, element):
            self.queue.insert(0, element)

        def outqueue(self):
            if len(self.queue) > 0:
                del self.queue[-1]
            else:
                print("Cola vacia")

        def count(self):
            print(f"El tamaño de la cola es de: {len(self.queue)} elementos")

        def __repr__(self):
            return str(self.queue)
    
    my_stack = Stack()
    my_stack.push("elem1")
    print(my_stack)
    my_stack.push("elem2")
    print(my_stack)
    my_stack.push("elem3")
    print(my_stack)
    my_stack.push("elem4")
    my_stack.count()
    print(my_stack)
    my_stack.pop()
    print(my_stack)
    my_stack.pop()
    print(my_stack)
    my_stack.pop()
    print(my_stack)
    my_stack.pop()
    print(my_stack)
    my_stack.pop()
    print(my_stack)

    my_queue = Queue()
    my_queue.inqueue("queue1")
    print(my_queue)
    my_queue.inqueue("queue2")
    print(my_queue)
    my_queue.inqueue("queue3")
    my_queue.count()
    print(my_queue)
    my_queue.outqueue()
    print(my_queue)
    my_queue.outqueue()
    print(my_queue)
    my_queue.outqueue()
    print(my_queue)
    
if __name__ == "__main__":
    main()
