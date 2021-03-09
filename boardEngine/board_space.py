from abc import ABC, abstractmethod

from layers.baseModelLayer.gameError.game_error import GameError


class BoardSpace(ABC):
    """
    Defines abstract class for defining board spaces.

    A game board should contain some spaces defined in order to hold items, characters and/or space references.

    _id: ID of the board than can and SHOULD be accessed for any layer for reference.
    """

    invoker = "BaseGameBoardSpace"
    invoker_code = 4

    _id: any = None

    @abstractmethod
    def create_board_space(self):
        """
        Creates board space, here the id should be created on child's class init method using create_board_space
        logic for db_model and logic model layer responsibility disaggregation.

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
                message="Space id can't be empty.",
                code=1,
                data=self,
            )

    @abstractmethod
    def save_board_space(self):
        """
        Saves board on db engine defined for these purposes.
        :return:
        """
        pass

    @abstractmethod
    def load_board_space(self, _id: any = None):
        """
        Loads board on db engine defined for these purposes.
        :param _id: ID of the board than can and SHOULD be accessed for any layer for reference.
        :return:
        """
        pass
