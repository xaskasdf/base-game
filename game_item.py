from abc import ABC, abstractmethod

from layers.baseGame.gameError.game_error import GameError


class GameItem(ABC):
    """
    Defines games items, these are the items that exists in game.
    """

    invoker = "BaseGameItem"
    invoker_code = 2

    _id: any = None
    name: str = None

    @abstractmethod
    def create_item(self):
        """
        Creates item, here the id should be created on child's class init method on top of use of create_item logic
        for db_model and logic model layer responsibility disaggregation.

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
                message="Board id can't be empty.",
                code=1,
                data=self,
            )

    @abstractmethod
    def save_item(self):
        """
        Saves item on db engine defined for these purposes.
        :return:
        """
        pass

    @abstractmethod
    def load_item(self, _id: any = None):
        """
        Loads item on db engine defined for these purposes.
        :param _id: ID of the item than can and SHOULD be accessed for any layer for reference.
        :return:
        """
        pass
