from abc import ABC, abstractmethod

from layers.baseGame.gameError.game_error import GameError


class BoardLogic(ABC):
    """
    Defines abstract class for making Game logic engines.

    A game board should be designed to support anything you could imagine in a game, that's why LogicBoard is an
    abstract class. You can make any class like 'DefaultBoard(LogicBoard)'.

    Here should be added any logic that can be needed and should be accessed for low level engines and models and
    interacts with the game, like a player position that can be used by the graphics layer library, idk.

    _id: ID of the board than can and SHOULD be accessed for any layer for reference.
    """

    invoker = "BaseGameLogicBoard"
    invoker_code = 5

    _id: any = None

    @abstractmethod
    def create_board(self):
        """
        Creates board, here the id should be created on child's class init method using create_board logic for
        db_model and logic model layer responsibility disaggregation.

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
                message="Logic Board id can't be empty.",
                code=1,
                data=self,
            )

    @abstractmethod
    def save_board(self):
        """
        Saves board on db engine defined for these purposes.
        :return:
        """
        pass

    @abstractmethod
    def load_board(self, _id: any = None):
        """
        Loads board on db engine defined for these purposes.
        :param _id: ID of the board than can and SHOULD be accessed for any layer for reference.
        :return:
        """
        pass
