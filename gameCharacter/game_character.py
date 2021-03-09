from abc import ABC, abstractmethod

from layers.baseGame.gameError.game_error import GameError


class GameCharacter(ABC):
    """
    Defines games characters, these are the characters that exist in game.
    """

    invoker = "BaseGameCharacter"
    invoker_code = 1

    _id: any = None
    name: str = None

    @abstractmethod
    def create_character(self, name: str = None):
        """
        Creates character, here the id should be created on child's class init method on top of use of
        create_character logic for db_model and logic model layer responsibility disaggregation.

        :return: This can be redefined, here returns an error message than can be thrived out through the
        controllers, or api, or the game itself, or and all-mentioned.
        """
        if name is not None:
            self.name = name
        else:
            raise GameError(
                invoker=self.invoker,
                invoker_code=self.invoker_code,
                message="Name can't be empty.",
                code=2,
                data=self,
            )
        if self._id is not None:
            # Here you can return a success message or capture event idk.
            pass
        else:
            raise GameError(
                invoker=self.invoker,
                invoker_code=self.invoker_code,
                message="Board id can't be empty",
                code=1,
                data=self,
            )

    @abstractmethod
    def save_item(self):
        """
        Saves character on db engine defined for these purposes.
        :return:
        """
        pass

    @abstractmethod
    def load_board(self, _id: any = None):
        """
        Loads character on db engine defined for these purposes.
        :param _id: ID of the character than can and SHOULD be accessed for any layer for reference.
        :return:
        """
        pass
