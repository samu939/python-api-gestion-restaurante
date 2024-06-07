from fastapi import Request
from starlette.responses import JSONResponse


class AppExceptionCase(Exception):
    def __init__(self, status_code: int, msg: str): 
        self.exception_case = self.__class__.__name__
        self.status_code = status_code
        self.msg = msg

    def __str__(self):
        return (
            f"<AppException {self.exception_case} - "
            + f"status_code={self.status_code} - msg={self.msg}>"
        )


async def app_exception_handler(request: Request, exc: AppExceptionCase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "app_exception": exc.exception_case,
            # "context": exc.context,
            "msg": exc.msg,
        },
    )
