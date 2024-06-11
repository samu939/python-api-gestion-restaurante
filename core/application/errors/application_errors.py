class ApplicationError(Exception):
    def __init__(self, message: str, code: int, name: str):
        self.message = message
        self.code = code
        self.name = name
        super().__init__(self.__class__.__name__, self.message, self.code, self.name)

