"""
/*
 * EJERCICIO:
 * GitHub ha publicado el Octoverse 2024, el informe
 * anual del estado de la plataforma:
 * https://octoverse.github.com
 *
 * Utilizando el API de GitHub, crea un informe asociado
 * a un usuario concreto.
 *
 * - Se debe poder definir el nombre del usuario
 *   sobre el que se va a generar el informe.
 *
 * - Crea un informe de usuario basándote en las 5 métricas
 *   que tú quieras, utilizando la información que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
 */
"""

from typing import Any
from dataclasses import dataclass
import requests


def get_user() -> str:
    """Gets the name if the github user from user"""
    return input("Dime el nombre de usuario: ")


@dataclass(frozen=True)
class UserMetrics:
    """Class to store user github metrics"""
    name: str
    login: str
    created_at: str
    most_used_language: str = ""
    followers_count: int = 0
    following_count: int = 0
    public_repos: int = 0
    public_gists_count: int = 0
    stargazers_count: int = 0
    forks_count: int = 0


class UserReport:
    """Class to get the github user metrics"""

    def __init__(self, name: str) -> None:
        self.name = name

    def get_user_report(self) -> UserMetrics | None:
        """Method to manage all metrics"""
        user_data = self.get_github_user_data()

        if not user_data:
            return None

        repos = self.get_github_user_repos()

        if not repos:
            user_metrics = UserMetrics(name=self.name,
                                       login=user_data["login"],
                                       followers_count=user_data["followers"],
                                       following_count=user_data["following"],
                                       public_repos=user_data["public_repos"],
                                       created_at=user_data["created_at"],
                                       public_gists_count=user_data["public_gists"],
                                       )
        else:
            user_metrics = UserMetrics(name=self.name,
                                       login=user_data["login"],
                                       followers_count=user_data["followers"],
                                       following_count=user_data["following"],
                                       public_repos=user_data["public_repos"],
                                       created_at=user_data["created_at"],
                                       public_gists_count=user_data["public_gists"],
                                       stargazers_count=self.get_user_stargazers_count(
                                           repos),
                                       forks_count=self.get_user_forks_count(
                                           repos),
                                       most_used_language=self.get_user_most_used_language(
                                           repos)
                                       )

        return user_metrics

    def get_github_user_data(self) -> dict[str, Any] | None:
        """Method to get main github metrics"""

        url = f"https://api.github.com/users/{self.name}"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        return response.json()

    def get_github_user_repos(self) -> list[dict[str, Any]] | None:
        """Method to get the user github metrics"""
        url = f"https://api.github.com/users/{self.name}/repos?per_page=100"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        return response.json()

    @staticmethod
    def get_user_stargazers_count(repos: list[dict[str, Any]]) -> int:
        """Method to calculate the stargazers count"""
        return sum(repo["stargazers_count"] for repo in repos)

    @staticmethod
    def get_user_forks_count(repos: list[dict[str, Any]]) -> int:
        """Method to calculate the number of forks"""
        return sum(repo["forks"] for repo in repos)

    @staticmethod
    def get_user_most_used_language(repos: list[dict[str, Any]]) -> str:
        """Method to calculate the most used programming language"""
        languages: dict[str, int] = {}

        for repo in repos:
            language = repo["language"]
            if language:
                languages[language] = languages.get(language, 0) + 1

        if not languages:
            return "No hay lenguajes de programación defenidos"

        return max(languages, key=languages.get)


def main():
    """Main function"""
    usuario = get_user()

    user_report = UserReport(usuario)
    metricas_usuario = user_report.get_user_report()

    if not metricas_usuario:
        print(f"Usuario {usuario} no existe")
    else:
        print(f"""
                Usuario: {metricas_usuario.login}
                Nombre: {metricas_usuario.name}
                Seguidores: {metricas_usuario.followers_count}
                Seguidos: {metricas_usuario.following_count}
                Repos públicos: {metricas_usuario.public_repos}
                Gists públicos: {metricas_usuario.public_gists_count}
                Stargazers: {metricas_usuario.stargazers_count}
                Forks: {metricas_usuario.forks_count}
                Lenguaje más usado: {metricas_usuario.most_used_language}
                Creado el: {metricas_usuario.created_at}
            """)


if __name__ == "__main__":
    main()
