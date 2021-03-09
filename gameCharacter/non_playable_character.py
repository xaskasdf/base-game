from abc import ABC

from layers.baseGame.gameCharacter.game_character import GameCharacter


class NonPlayableCharacter(GameCharacter, ABC):
    """
    Defines games non playable characters (NPCs), these are the characters that exist freely roaming in game.

    My goal is to have little to no control over them, i mean, real no control.
    """

    invoker = "NPC"

    _id: any = None
    name: str = None
    ai: object = None  # TODO: Define class for this crap
    location: str = None  # This happens to be a BoardSpace id
