from typing import List

from requests.cookies import RequestsCookieJar
from requests.packages.urllib3.util.retry import Retry

from waypoint.models import StatHistory
from waypoint.enum import GameVariant, Game
from waypoint.client.base import APIClient, http_method


class WaypointClient(APIClient):
    retry_strategy = Retry(
        total=10,
        backoff_factor=1,
        status_forcelist=[500],
    )

    def __init__(self, auth_cookie: str):
        super().__init__(
            "https://www.halowaypoint.com/en-us/games/halo-the-master-chief-collection/xbox-one/"
        )
        cookie_jar = RequestsCookieJar()
        cookie_jar.set("Auth", auth_cookie)
        self.session.cookies = cookie_jar

    @http_method(StatHistory)
    def get_game_history(
        self,
        game_variant: GameVariant,
        gamertags: List[str],
        page: int = 1,
        game: Game = Game.ALL,
    ):
        return self.session.get(
            "game-history",
            params={
                "gameVariant": game_variant.value,
                "gamertags": ",".join(gamertags),
                "page": page,
                "game": game.value,
                "view": "DataOnly",
            },
        )
