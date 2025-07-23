#LIFO

stack =[]

#PUSH
stack.append("cad1")
stack.append("cad2")
stack.append("cad3")
print(stack)

#POP
print(stack.pop())
print(stack)

#FIFO

queu = []

#PUSH
queu.insert(0, "cola1")
queu.insert(0, "cola2")
queu.insert(0, "cola3")
print(queu)

#POP
print(queu[-1])
del queu[-1]
print(queu)

queu.pop(len(queu) - 1)
print(queu)


""" EXTRA """

def browser():
   
    web_stack = []

    while True:
        option = input("Select an url or an option (ADELANTE/ATRAS/SALIR): ")

        if option.lower() == "atras":
            if len(web_stack) > 0:
                web_stack.pop()
        elif option.lower() == "adelante":
            pass
        elif option.lower() == "salir":
            print("Saliendo...")
            break
        else:
            web_stack.append(option.lower())
        
        if len(web_stack) > 0:
            print(f"URL: {web_stack[-1]}")
        else:
            print("Inicial web")

def printer_queu():
    queue = []

    while True:

        option = input("Send a document to the printer or select an option (SALIR/IMPRIMR): ")

        if option.lower() == "salir":
            print("Quiting...")
            break
        if option.lower() == "imprimir":
            if len(queue) > 0:
                print(f"Printing: {queue.pop(len(queue) - 1)}")
            else:
                print("No jobs to print")
        else:
            queue.insert(0, option)
        
        print(f"Jobs in queu: {queue}")

def main():

    browser()
    printer_queu()
    
if __name__ == "__main__":
    main()
