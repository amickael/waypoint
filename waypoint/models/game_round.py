from typing import List, Dict

from pydantic import BaseModel

from waypoint.models.stat import Stat


class GameRound(BaseModel):
    id: str
    Participants: List[str]
    Winner: str
    PlayerStats: Dict[str, Stat]
    Map: str
    Game: str
