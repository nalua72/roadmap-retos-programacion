
"""
This script demonstrates serialization and deserialization of a Python dictionary to JSON and XML formats,
as well as reading the data back and mapping it to a custom User class.

Features:
- Defines a sample data dictionary with personal information and programming languages.
- Provides a utility function to delete files if they exist.
- Serializes the data dictionary to a JSON file and reads it back.
- Serializes the data dictionary to an XML file and reads it back.
- Defines a User class to represent the data structure.
- Maps the loaded JSON and XML data to User instances and prints their attributes.
- Cleans up by deleting the generated files.

Functions:
- delete_file_if_exists(file_path): Deletes the specified file if it exists.
- create_json(data, filename): Serializes the data dictionary to a JSON file.
- create_xml(data, filename): Serializes the data dictionary to an XML file.

Classes:
- User: Represents a user with name, age, birth date, and programming languages.

Usage:
Run the script to see the serialization, deserialization, and mapping processes in action.
"""


import json
import pathlib
import xml.etree.ElementTree as ET


data = {
    "Nombre": "Jose Manuel Rodriguez Perez",
    "Edad": 42,
    "Fecha_de_nacimiento": "10/07/1972",
    "Lenguajes_de_programacion": ["bash", "python", "C", ]
}


def delete_file_if_exists(file_path):
    file = pathlib.Path(file_path)
    if file.exists():
        file.unlink()
        print(f"El archivo {file_path} ha sido eliminado.")


#JSON
def create_json(data, filename):
    with open(pathlib.Path("nalua72.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

create_json(data, "nalua72.json")

with open(pathlib.Path("nalua72.json"), "r", encoding="utf-8") as f:
    data_loaded = json.load(f) 
    print(data_loaded)

delete_file_if_exists("nalua72.json")


#XML


def create_xml(data, filename):
    root = ET.Element("root")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                item_element = ET.SubElement(child, "item")
                item_element.text = str(item)
        else:
            child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

create_xml(data, "nalua72.xml")

with open("nalua72.xml", "r", encoding="utf-8") as f:
    xml_content = f.read()
    print(xml_content)

delete_file_if_exists("nalua72.xml")


""" EXTRA """


class User:
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes


create_json(data, "nalua72.json")
create_xml(data, "nalua72.xml")


with open(pathlib.Path("nalua72.json"), "r", encoding="utf-8") as f:
    data_loaded = json.load(f)
    jose = User(
        data_loaded["Nombre"],
        data_loaded["Edad"],
        data_loaded["Fecha_de_nacimiento"],
        data_loaded["Lenguajes_de_programacion"]
    )
    print(f"Nombre: {jose.nombre}, Edad: {jose.edad}, Fecha de naciminto: {jose.fecha_nacimiento}, Lenguajes de programacion: {jose.lenguajes}")


with open("nalua72.xml", "r", encoding="utf-8") as f:
    tree = ET.parse(f)
    root = tree.getroot()
    nombre = root.find("Nombre").text
    edad = int(root.find("Edad").text)
    fecha_nacimiento = root.find("Fecha_de_nacimiento").text
    lenguajes = [item.text for item in root.find("Lenguajes_de_programacion").findall("item")]
    jose_xml = User(nombre, edad, fecha_nacimiento, lenguajes)
    print(f"Nombre: {jose_xml.nombre}, Edad: {jose_xml.edad}, Fecha de naciminto: {jose_xml.fecha_nacimiento}, Lenguajes de programacion: {jose_xml.lenguajes}")


delete_file_if_exists("nalua72.json")
delete_file_if_exists("nalua72.xml")