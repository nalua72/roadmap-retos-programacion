import subprocess
from pathlib import Path


"""
/*
 * EJERCICIO:
 * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
 *
 * Desarrolla un CLI (Command Line Interface) que permita
 * interactuar con Git y GitHub de manera real desde terminal.
 *
 * El programa debe permitir las siguientes opciones:
 * 1. Establecer el directorio de trabajo
 * 2. Crear un nuevo repositorio
 * 3. Crear una nueva rama
 * 4. Cambiar de rama
 * 5. Mostrar ficheros pendientes de hacer commit
 * 6. Hacer commit (junto con un add de todos los ficheros)
 * 7. Mostrar el historial de commits
 * 8. Eliminar rama
 * 9. Establecer repositorio remoto
 * 10. Hacer pull
 * 11. Hacer push
 * 12. Salir
 *
 * Puedes intentar controlar los diferentes errores.
 */
"""


class GitCLI:

    def __init__(self):
        self.working_directory = None

    # ==============================
    # CONFIGURACIÓN
    # ==============================

    def set_working_directory(self):
        path_input = input(
            "Introduce el directorio completo de trabajo: ").strip()
        path = Path(path_input).expanduser().resolve()

        if not path.is_dir():
            print("❌ El directorio no existe.")
            return

        self.working_directory = path
        print(f"✅ Directorio establecido: {self.working_directory}")

    def _ensure_working_directory(self):
        if self.working_directory is None:
            print("⚠️ Primero debes establecer un directorio de trabajo.")
            return False
        return True

    def _ensure_git_repository(self):
        if not self._ensure_working_directory():
            return False

        try:
            result = subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                cwd=self.working_directory,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip() == "true"
        except subprocess.CalledProcessError:
            print("❌ El directorio no es un repositorio Git.")
            return False

    # ==============================
    # EJECUCIÓN BASE
    # ==============================

    def _run_git(self, args):
        try:
            result = subprocess.run(
                ["git"] + args,
                cwd=self.working_directory,
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("❌ Error ejecutando comando Git:")
            print(e.stderr)

    # ==============================
    # OPERACIONES GIT
    # ==============================

    def git_init(self):
        if not self._ensure_working_directory():
            return
        self._run_git(["init"])

    def git_status(self):
        if not self._ensure_git_repository():
            return
        self._run_git(["status"])

    def git_add_all(self):
        if not self._ensure_git_repository():
            return
        self._run_git(["add", "."])

    def git_commit(self):
        if not self._ensure_git_repository():
            return

        message = input("Introduce el mensaje del commit: ").strip()
        if not message:
            print("❌ El mensaje no puede estar vacío.")
            return

        self._run_git(["commit", "-m", message])

    def git_log(self):
        if not self._ensure_git_repository():
            return
        self._run_git(["log", "--oneline"])

    def create_branch(self):
        if not self._ensure_git_repository():
            return

        branch = input("Nombre de la nueva rama: ").strip()
        if branch:
            self._run_git(["branch", branch])

    def delete_branch(self):
        if not self._ensure_git_repository():
            return

        branch = input("Nombre de la rama a eliminar: ").strip()
        if branch:
            self._run_git(["branch", "-d", branch])

    def set_remote(self):
        if not self._ensure_git_repository():
            return

        url = input("Introduce la URL del repositorio remoto: ").strip()
        if url:
            self._run_git(["remote", "add", "origin", url])

    def git_pull(self):
        if not self._ensure_git_repository():
            return
        self._run_git(["pull"])

    def git_push(self):
        if not self._ensure_git_repository():
            return
        self._run_git(["push"])


# ==============================
# MENÚ
# ==============================

def show_menu():
    print("""
=============================
        GIT CLI
=============================
1. Establecer directorio de trabajo
2. Inicializar repositorio
3. Mostrar estado
4. Añadir todos los archivos
5. Commit
6. Historial
7. Crear rama
8. Eliminar rama
9. Añadir repositorio remoto
10. Pull
11. Push
0. Salir
""")


def main():
    cli = GitCLI()

    while True:
        show_menu()
        try:
            option = int(input("Opción: "))
        except ValueError:
            print("❌ Opción inválida.")
            continue

        match option:
            case 1:
                cli.set_working_directory()
            case 2:
                cli.git_init()
            case 3:
                cli.git_status()
            case 4:
                cli.git_add_all()
            case 5:
                cli.git_commit()
            case 6:
                cli.git_log()
            case 7:
                cli.create_branch()
            case 8:
                cli.delete_branch()
            case 9:
                cli.set_remote()
            case 10:
                cli.git_pull()
            case 11:
                cli.git_push()
            case 0:
                print("👋 Saliendo...")
                break
            case _:
                print("❌ Opción no válida.")


if __name__ == "__main__":
    main()
