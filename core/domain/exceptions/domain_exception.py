class DomainException(Exception):
    def __init__(self, message: str, code: int, name: str):
        self.message = message
        self.name = name
        self.code = code
        super().__init__(self.__class__.__name__, self.message, self.code, self.name)

