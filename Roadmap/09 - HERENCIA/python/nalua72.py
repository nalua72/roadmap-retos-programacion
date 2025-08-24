class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!. I am a {self.breed}."


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


sultan = Dog("Sultan", "Golden Retriever")
print(sultan.speak())

jewels = Cat("Jewels")
print(jewels.speak())

pig = Animal("Piggy")
print(pig.speak())


""" EJERCICIO EXTRA """

def main():
    """
    Demonstrates a simple employee hierarchy using inheritance.
    This function defines the following classes:
        - Employee: Base class for all employees, supports subordinates.
        - Manager: Inherits from Employee, represents a department manager.
        - Project_Manager: Inherits from Employee, represents a project manager.
        - Developer: Inherits from Employee, represents a developer with a programming language.
    The function creates instances of managers, project managers, and developers,
    assigns subordinates accordingly, and prints the organizational hierarchy.
    Output:
        Prints the hierarchy of managers, their project managers, and developers.
    """
    # Base class for all employees
    class Employee:
        def __init__(self, employee_name, employee_id):
            self.name = employee_name
            self.id = employee_id
            self.employees = []  # List to store subordinates

        def add_subordinate(self, employee):
            # Add a subordinate employee
            self.employees.append(employee)

        def list_subordinates(self):
            # Return a list of subordinate names
            return [emp.name for emp in self.employees]
        
    # Manager class inherits from Employee
    class Manager(Employee):
        def __init__(self, employee_name, employee_id, department=None):
            super().__init__(employee_name, employee_id)
            self.department = department

        def manager_activity(self):
            # Return a string describing manager's activity
            return f"Manager {self.name}, manages department: {self.department}"

    # Project Manager class inherits from Employee
    class Project_Manager(Employee):
        def __init__(self, employee_name, employee_id, project=None):
            super().__init__(employee_name, employee_id)
            self.project = project

        def project_manager_activity(self):
            # Return a string describing project manager's activity
            return f"Project manager {self.name}, manages project: {self.project}"

    # Developer class inherits from Employee
    class Developer(Employee):
        def __init__(self, employee_name, employee_id, language=None):
            super().__init__(employee_name, employee_id)
            self.language = language

        def developer_activity(self):
            # Return a string describing developer's activity
            return f"Developer {self.name}, programs in: {self.language}"
   
    # Create Manager instances
    m1 = Manager("Alice", 101, "IT")
    m2 = Manager("Bob", 102, "HR")

    # Create Project Manager instances
    pm1 = Project_Manager("Charlie", 201, "Project X")
    pm2 = Project_Manager("David", 202, "Project Y")
    pm3 = Project_Manager("Eve", 203, "Project Z")
    pm4 = Project_Manager("Frank", 204, "Project A")

    # Create Developer instances
    d1 = Developer("Grace", 301, "Python")
    d2 = Developer("Heidi", 302, "Java")
    d3 = Developer("Ivan", 303, "C++")
    d4 = Developer("Judy", 304, "JavaScript")
    d5 = Developer("Mallory", 305, "Ruby")
    d6 = Developer("Niaj", 306, "Go")
    d7 = Developer("Olivia", 307, "Swift")
    d8 = Developer("Peggy", 308, "Kotlin")

    # Assign Project Managers as subordinates to Managers
    m1.add_subordinate(pm1)
    m1.add_subordinate(pm2)
    m2.add_subordinate(pm3)
    m2.add_subordinate(pm4)

    # Assign Developers as subordinates to Project Managers
    pm1.add_subordinate(d1)
    pm1.add_subordinate(d2)
    pm2.add_subordinate(d3)
    pm2.add_subordinate(d4)
    pm3.add_subordinate(d5)
    pm3.add_subordinate(d6)
    pm4.add_subordinate(d7)
    pm4.add_subordinate(d8)

    # Display the hierarchy of managers, project managers, and developers
    for manager in [m1, m2]:    
        print(f"\n{manager.manager_activity()}")
        for pm in manager.employees:
            print(f"\t{pm.project_manager_activity()}")
            for dev in pm.employees:
                print(f"\t\t{dev.developer_activity()}")

if __name__ == "__main__":
    main()
