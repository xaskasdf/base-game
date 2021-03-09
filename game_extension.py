from abc import abstractmethod, ABC

from layers.baseGame.gameError.game_error import GameError


class GameExtension(ABC):
    """
    Defines game extension for add game functionality, set for future greater purposes.
    """

    invoker = "BaseGameExtension"
    invoker_code = 4

    _id: any = None
    name: str = None

    @abstractmethod
    def load_extension(self, _id: any = None):
        """
        Loads board on db engine defined for this purposes.
        :param _id: ID of the extension than can and SHOULD be accessed for any layer for reference.
        :return:
        """
        if _id is None:
            raise GameError(
                invoker=self.invoker,
                invoker_code=self.invoker_code,
                message="Unable to load. Extension id can't be empty.",
                code=1,
                data=self,
            )
        else:
            pass
