from pathlib import Path
import subprocess

"""
/*
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
 */
"""


def compress_file(file: str, format: str) -> str:
    path = Path(file)

    if not path.exists():
        raise FileNotFoundError(f"El fichero '{file}' no existe")

    output_file: str

    match format:
        case "gz":
            output_file = f"{path.name}.tar.gz"
            cmd = ["tar", "-czf", output_file, file]

        case "bz2":
            output_file = f"{path.name}.tar.bz2"
            cmd = ["tar", "-cjf", output_file, file]

        case "xz":
            output_file = f"{path.name}.tar.xz"
            cmd = ["tar", "-cJf", output_file, file]

        case "zip":
            output_file = f"{path.name}.zip"
            cmd = ["zip", "-r", output_file, file]

        case _:
            raise ValueError("Formato no válido")

    subprocess.run(cmd, check=True)
    return output_file


def decompress_file(file: str) -> str:
    path = Path(file)

    if not path.exists():
        raise FileNotFoundError(f"El archivo '{file}' no existe")

    name = path.name.lower()

    if name.endswith(".tar.gz"):
        subprocess.run(["tar", "-xzf", file], check=True)

    elif name.endswith(".tar.bz2"):
        subprocess.run(["tar", "-xjf", file], check=True)

    elif name.endswith(".tar.xz"):
        subprocess.run(["tar", "-xJf", file], check=True)

    elif name.endswith(".zip"):
        if not shutil.which("unzip"):
            raise RuntimeError("El comando 'unzip' no está instalado")
        subprocess.run(["unzip", file], check=True)

    else:
        raise ValueError(f"Formato de archivo no soportado: {path.suffix}")

    return "Descompresión completada correctamente"


def main():
    print("🗜️  Gestor de compresión")
    print("1️⃣  Comprimir archivo o carpeta")
    print("2️⃣  Descomprimir archivo")

    opcion = input("Elige una opción [1/2]: ").strip()

    try:
        match opcion:
            case "1":
                fichero = input("Fichero o carpeta a comprimir: ").strip()
                formato = input("Formato [gz, bz2, xz, zip]: ").lower().strip()

                resultado = compress_file(fichero, formato)
                print(f"✅ Archivo creado: {resultado}")

            case "2":
                fichero = input("Archivo a descomprimir: ").strip()

                resultado = decompress_file(fichero)
                print(f"✅ {resultado}")

            case _:
                print("❌ Opción no válida")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
