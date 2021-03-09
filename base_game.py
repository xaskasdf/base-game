from abc import ABC


class BaseGame(ABC):
    """
    Defines base game conditions, as game definitions, such as a board, 1st it. example.

    You can define any game definitions here, any upgrades made here should be made carefully, since can crash some
    upper level definitions made on top of this.

    Is this an Engine? Idk - Samuel
    It's like a world reality constitution maker - stoned Samuel
    """

    # NOTE: Base game groups main definitions, these ARE the definitions.
    # NOTE: Base game groups main definitions, these ARE the definitions.

    version = 1.0
    engine_codename = "flying_whale"
