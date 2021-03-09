from abc import ABC, abstractmethod

from layers.baseGame.gameError.game_error import GameError


class GameEvent(ABC):
    """
    Defines games events, these are the events that affects globally the gameplay.
    These aren't the events that trigger movements or anything like that.
    """

    invoker = "BaseGameEvent"
    invoker_code = 3

    _id: any = None
    name: str = None

    @abstractmethod
    def create_event(self):
        """
        Creates event, here the id should be created on child's class init method and served to the game.

        :return: This can be redefined, here returns an error message than can be thrived out through the
        controllers, or api, or the game itself, or and all-mentioned.
        """
        if self._id is not None:
            # Here you can return a success message or capture event idk.
            pass
        else:
            raise GameError(
                invoker=self.invoker,
                invoker_code=self.invoker_code,
                message="Event id can't be empty.",
                code=1,
                data=self,
            )

    @abstractmethod
    def log_event(self, _id: any = None):
        """
        Register event execution and result on db engine defined for this purposes.
        :param _id: ID of the event than can and SHOULD be accessed for any layer for reference.
        :return:
        """
        pass
