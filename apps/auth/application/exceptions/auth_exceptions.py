from core.infrastructure.utils.app_exceptions import AppExceptionCase


class AuthExceptions:
    class AuthNoUsernameException(AppExceptionCase):
        """_
        Auth no username
        """

        def __init__(self, msg: str = ""):  # context: dict = None):
            status_code = 422
            # context = {"message": "No se ha ingresado un nombre de usuario"}
            msg = "No se ha ingresado un nombre de usuario"
            AppExceptionCase.__init__(self, status_code, msg)

    class AuthNoPasswordException(AppExceptionCase):
        """_
        Auth no password
        """

        def __init__(self, msg: str = ""):  # context: dict = None):
            status_code = 422
            # context = {"message": "No se ha ingresado una clave de ingreso"}
            msg = "No se ha ingresado una clave de ingreso"
            AppExceptionCase.__init__(self, status_code, msg)

    class AuthNoRoleException(AppExceptionCase):
        """_
        Auth no role
        """

        def __init__(self, msg: str = ""):  # context: dict = None):
            status_code = 422
            # context = {"message": "No se ha ingresado una clave de ingreso"}
            msg = "No se ha ingresado un role de usuario"
            AppExceptionCase.__init__(self, status_code, msg)

    class AuthNoValidCredencialsException(AppExceptionCase):
        """_
        Auth no valid credentials
        """

        def __init__(self, msg: str = ""):  # context: dict = None):
            status_code = 401
            # context = {"message": "Credenciales no válidas"}
            msg = "Credenciales inválidas"
            AppExceptionCase.__init__(self, status_code, msg)

    class AuthDuplicatedUsernameException(AppExceptionCase):
        """_
        Auth no valid credentials
        """

        def __init__(self, msg: str = ""):  # context: dict = None):
            status_code = 401
            # context = {"message": "Credenciales no válidas"}
            msg = "Username already exists"
            AppExceptionCase.__init__(self, status_code, msg)

    class AuthNoValidTokenCredentialsException(AppExceptionCase):
        """_
        Auth no valid credentials
        """

        def __init__(self, msg: str = ""):  # context: dict = None):
            status_code = 401
            # context = {"message": "No se pudo validar el token"}
            msg = "No se pudo validar el token"
            AppExceptionCase.__init__(self, status_code, msg)

    class AuthUnauthorizedException(AppExceptionCase):
        """
        No access authorization
        """

        def __init__(self, msg: str = ""):
            status_code = 401
            msg = "No está autorizado para ejecutar esta función"
            AppExceptionCase.__init__(self, status_code, msg)

    class AuthTokenExpiredException(AppExceptionCase):
        """_
        Auth no valid credentials
        """

        def __init__(self, msg: str = ""):  # context: dict = None):
            status_code = 401
            # context = {"message": "No se pudo validar el token"}
            msg = "EL tiempo de su sessión ha expirado, por favor vuelva a ingresar"
            AppExceptionCase.__init__(self, status_code, msg)

    class AuthRestPswTokenExpiredException(AppExceptionCase):
        """_
        Token de reset de passwaord está vencido
        """

        def __init__(self, msg: str = ""):  # context: dict = None):
            status_code = 400
            # context = {"message": "No se pudo validar el token"}
            msg = "El tiempo de renovación de la clave ha vencido, vuelva a intentarlo"
            AppExceptionCase.__init__(self, status_code, msg)

    class AuthRestPswTokenUsedException(AppExceptionCase):
        """_
        Token de reset de passwaord ha sido usado
        """

        def __init__(self, msg: str = ""):  # context: dict = None):
            status_code = 400
            # context = {"message": "No se pudo validar el token"}
            msg = "El token ya no es válido"
            AppExceptionCase.__init__(self, status_code, msg)
