class MaeException(Exception):
    ...

class MaeNotFoundError(MaeException):
    def __init__(self):
        self.status_code = 404
        self.detail = "MAE_NAO_ENCONTRADA"

class MedicoException(Exception):
    ...

class MedicoNotFoundError(MedicoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "MEDICO_NAO_ENCONTRADO"

class BebeException(Exception):
    ...

class BebeNotFoundError(BebeException):
    def __init__(self):
        self.status_code = 404
        self.detail = "BEBE_NAO_ENCONTRADO"