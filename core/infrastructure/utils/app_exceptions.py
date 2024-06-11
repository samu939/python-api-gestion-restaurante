from fastapi import Request
from starlette.responses import JSONResponse


class AppExceptionCase(Exception):
    def __init__(self, status_code: int, msg: str): 
        self.name = self.__class__.__name__
        self.code = status_code
        self.message = msg

    def __str__(self):
        return (
            f"<AppException {self.exception_case} - "
            + f"status_code={self.status_code} - msg={self.msg}>"
        )


async def app_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=exc.code,
        content={
            "app_exception": exc.name,
            # "context": exc.context,
            "msg": exc.message,
        },
    )
