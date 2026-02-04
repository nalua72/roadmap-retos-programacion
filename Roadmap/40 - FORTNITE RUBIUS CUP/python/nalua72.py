import os
from dataclasses import dataclass
from datetime import datetime
from dotenv import load_dotenv
from typing import Optional
import requests
from typing import Optional
import re


"""
/*
 * EJERCICIO:
 * ¡Rubius tiene su propia skin en Fortnite!
 * Y va a organizar una competición para celebrarlo.
 * Esta es la lista de participantes:
 * https://x.com/Rubiu5/status/1840161450154692876
 *
 * Desarrolla un programa que obtenga el número de seguidores en
 * Twitch de cada participante, la fecha de creación de la cuenta
 * y ordene los resultados en dos listados.
 * - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
 *   (NO subas las credenciales de autenticación)
 * - Crea un ranking por número de seguidores y por antigüedad.
 * - Si algún participante no tiene usuario en Twitch, debe reflejarlo.
 */
"""


PARTICIPANTS_LIST = ['ABBY', 'ACHE', 'ADRI CONTRERAS', 'AGUSTIN', 'ALEXBY', 'AMPETER', 'ANDER', 'ARI GAMEPLAYS', 'ARIGELI', 'AURONPLAY', 'AXOZER', 'BENIJU', 'BY CALITOS', 'BYVIRUZZ', 'CARRERA', 'CELOPAN', 'CHEETO', 'CRYSTALMOLLY', 'DARIO EMEHACHE', 'DHEYLO', 'DJMARIIO', 'DOBLE', 'ELVISA', 'ELYAS360', 'FOLAGOR', 'GREFG', 'GUANYA', 'HIKA', 'HIPER', 'IBAI', 'IBELKY', 'ILLOJUAN', 'IMANTADO', 'IRINA ISASIA', 'JESSKIU', 'JOPA', 'JORDIWILD', 'KENAI SOUZA', 'KERORO', 'KIDD KEO', 'KIKO RIVERA', 'KNEKRO', 'KOKO', 'KRONNOZOMBER', 'LEVIATHAN', 'LIT KILLAH',
                     'LOLA LOLITA', 'LOLITO', 'LUH', 'LUZU', 'MANGEL', 'MAYICHI', 'MELO', 'MISSASINFONIA', 'MIXWELL', 'MR JAGGER', 'NATE GENTILE', 'NEXXUZ', 'NIA', 'NIL OJEDA', 'NISSAXTER', 'OLLIE', 'ORSLOK', 'OUTCONSUMER', 'PAPI GAVI', 'PARACETAMOR', 'PATICA', 'PAULA GONU', 'PAUSENPAII', 'PERXITAA', 'PLEX', 'POLISPOL', 'QUACKITY', 'RECUERDOP', 'REVEN', 'RIVERS', 'ROBERTPG', 'ROIER', 'ROJUU', 'RUBIUS', 'SHADOUNE', 'SILITHUR', 'SPOKSPONHA', 'SPREEN', 'SPURSITO', 'STAXX', 'SUZYROXX', 'VICENS', 'VITUBER', 'WERLYB', 'XAVI', 'XCRY', 'XOKAS', 'ZARCORT', 'ZELING', 'ZORMAN']


@dataclass
class Participant:
    """Define a un participante"""
    name: str
    twitch_login: Optional[str] = None
    followers: Optional[int] = None
    created_at: Optional[datetime] = None
    exists_on_twitch: bool = True


class TwitchAPI():
    """Gestiona las conexiones con Twitch"""
    BASE_URL = "https://api.twitch.tv/helix"

    def __init__(self):
        self.client_id = os.getenv("TWITCH_CLIENT_ID")
        self.client_secret = os.getenv("TWITCH_CLIENT_SECRET")

        # self.client_id = CLIENT_ID
        # self.client_secret = CLIENT_SECRET
        self.token = self._get_access_token()

    def _get_access_token(self) -> str:
        """Obtiene el TOKEN de Twitch"""
        url = "https://id.twitch.tv/oauth2/token"
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()["access_token"]

    def _headers(self):
        return {
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {self.token}"
        }

    def map_names_to_logins_search(self, participants_list: list[str]) -> dict[str, Optional[str]]:
        """
        Busca posibles canales en Twitch y delega la elección del login
        a un método auxiliar de selección.
        """
        mapping: dict[str, Optional[str]] = {}

        for name in participants_list:
            search_url = f"{self.BASE_URL}/search/channels"
            response = requests.get(
                search_url,
                headers=self._headers(),
                params={"query": name, "first": 5},
                timeout=5
            )

            candidates = response.json().get("data", [])
            selected_login = self._select_best_login(candidates, name)

            mapping[name] = selected_login

        return mapping

    def get_user(self, login: str):
        """Obtiene de Twitch elos datos de un usuario"""
        URL = f"{self.BASE_URL}/users"

        response = requests.get(URL, headers=self._headers(),
                                params={"login": login}, timeout=5)
        data = response.json()["data"]
        return data[0] if data else None

    def get_followers(self, user_id: str) -> int:
        """Obtiene de Twitch el numero de followers de un usuario"""
        URL = f"{self.BASE_URL}/channels/followers"

        response = requests.get(URL, headers=self._headers(), params={
                                "broadcaster_id": user_id}, timeout=5)
        data = response.json()["total"]
        return data

    def _normalize(self, value: str) -> str:
        return value.lower().replace(" ", "")

    def _select_best_login(self, candidates: list[dict], searched_name: str) -> Optional[str]:
        """
        Selecciona el mejor login de Twitch aplicando una estrategia jerárquica:
        1. Match exacto (display_name o login)
        2. Match con prefijos comunes (el_, the_)
        3. Match parcial limpio (evitando canales secundarios)
        4. Fallback: mayor número de seguidores
        """

        searched = self._normalize(searched_name)
        strong_matches = []
        partial_matches = []
        fallback = []

        for candidate in candidates:
            display = self._normalize(candidate["display_name"])
            login = self._normalize(candidate["broadcaster_login"])
            user_id = candidate["id"]

            try:
                followers = self.get_followers(user_id)
            except Exception:
                continue

            entry = {
                "login": candidate["broadcaster_login"],
                "followers": followers
            }

            # 1. Match exacto
            if display == searched or login == searched:
                strong_matches.append(entry)
                continue

            # 2. Prefijos típicos de Twitch
            if display in {f"el{searched}", f"the{searched}"}:
                strong_matches.append(entry)
                continue

            if login in {f"el{searched}", f"the{searched}"}:
                strong_matches.append(entry)
                continue

            # 3. Match parcial limpio (evita "clips", "pov", etc.)
            pattern = rf"\b{re.escape(searched)}\b"
            if re.search(pattern, display):
                partial_matches.append(entry)
                continue

            fallback.append(entry)

        if strong_matches:
            return max(strong_matches, key=lambda x: x["followers"])["login"]

        if partial_matches:
            return max(partial_matches, key=lambda x: x["followers"])["login"]

        if fallback:
            return max(fallback, key=lambda x: x["followers"])["login"]

        return None


def main():
    load_dotenv()
    participantes: list[Participant] = []

    twitch_api = TwitchAPI()

    # Copie la lista de mouredev porque ningun algoritmo probado coseguia bien los login reales de los usuarios a prtir de la lista de nombres
    real_login = [
        "littleragergirl", "ache", "adricontreras4", "agustin51", "alexby11", "ampeterby7", "tvander",
        "arigameplays", "arigeli_", "auronplay", "axozer", "beniju03", "bycalitos",
        "byviruzz", "carreraaa", "celopan", "srcheeto", "crystalmolly", "darioemehache",
        "dheylo", "djmariio", "doble", "elvisayomastercard", "elyas360", "folagorlives", "thegrefg",
        "guanyar", "hika", "hiperop", "ibai", "ibelky_", "illojuan", "imantado",
        "irinaissaia", "jesskiu", "jopa", "jordiwild", "kenaivsouza", "mrkeroro10",
        "thekiddkeo95", "kikorivera", "knekro", "kokoop", "kronnozomberoficial", "leviathan",
        "litkillah", "lolalolita", "lolitofdez", "luh", "luzu", "mangel", "mayichi",
        "melo", "missasinfonia", "mixwell", "jaggerprincesa", "nategentile7", "nexxuz",
        "lakshartnia", "nilojeda", "nissaxter", "olliegamerz", "orslok", "outconsumer", "papigavitv",
        "paracetamor", "patica1999", "paulagonu", "pausenpaii", "perxitaa", "nosoyplex",
        "polispol1", "quackity", "recuerd0p", "reventxz", "rivers_gg", "robertpg", "roier",
        "ceuvebrokenheart", "rubius", "shadoune666", "silithur", "spok_sponha", "elspreen", "spursito",
        "bystaxx", "suzyroxx", "vicens", "vitu", "werlyb", "xavi", "xcry", "elxokas",
        "thezarcort", "zeling", "zormanworld", "mouredev"
    ]

    # mapped_users = twitch_api.map_names_to_logins_search(PARTICIPANTS_LIST)
    # Me quedo solo con los login con cuenta de Twitch
    # real_login = [login for login in mapped_users.values() if login is not None]

    for login in real_login:
        datos_participante = twitch_api.get_user(login)

        if datos_participante is not None:
            name = datos_participante["display_name"]
            login = datos_participante["login"]
            followers = twitch_api.get_followers(datos_participante["id"])
            created_at = datetime.fromisoformat(
                datos_participante["created_at"])
            exists_on_twitch = True

            participantes.append(Participant(name=name, twitch_login=login, followers=followers,
                                 created_at=created_at, exists_on_twitch=exists_on_twitch))

    # Ordenados por fecha de antigüedad
    print("\n*******************Ranking por Antigüedad*******************")
    participantes.sort(key=lambda x: x.created_at, reverse=False)
    for ranking, participante in enumerate(participantes):
        print(
            f"{ranking + 1} - {participante.name}, Antigüedad: {participante.created_at.strftime("%Y-%m-%d")}")

    # Ordenados por numero de seguidores
    print(
        "\n*******************Ranking por Número de Seguidores*******************")
    participantes.sort(key=lambda x: x.followers, reverse=True)
    for ranking, participante in enumerate(participantes):
        print(
            f"{ranking + 1} {participante.name}, Seguidores: {participante.followers}")


if __name__ == "__main__":
    main()
