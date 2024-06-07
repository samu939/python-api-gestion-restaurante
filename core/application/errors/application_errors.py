class ApplicationError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.__class__.__name__, self.message)

    @property
    @classmethod
    def name(cls) -> str:
        return cls.__name__
