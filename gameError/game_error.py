from abc import ABC


class GameError(ABC, Exception):
    """
    Invokable base error than can be raised and inherited by more specific error classes.
    """

    invoker: str
    message: str
    code: int
    data: object

    def __init__(
        self,
        invoker: str = None,
        invoker_code: int = None,
        message: str = None,
        code: int = None,
        data: object = None,
    ):
        if invoker is not None:
            self.invoker = invoker
        if data is not None:
            self.data = data
            if invoker is None:
                self.invoker = str(type(data))
        if code is not None:
            self.code = code
        else:
            self.code = -1
        if invoker_code is not None:
            self.code = (
                (self.code + invoker_code) if self.code > 0 else (-1 - invoker_code)
            )
        if message is not None:
            self.message = message
        else:
            if self.code is -1:
                # This is the worst error possible, if you get this, maybe you fucked up things pretty bad or didn't
                # follow any error usage logic and you don't know where you are, good luck and have fun.
                self.message = "UNKNOWN ERROR, DETAIL: {}".format(data)
            else:
                self.message = "{}"
