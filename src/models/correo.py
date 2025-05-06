import re
from typing import Optional
from utils.constantes import (
    DOMINIO_ESTUDIANTE,
    DOMINIO_DOCENTE,
    TIPO_ESTUDIANTE,
    TIPO_DOCENTE
)

class Correo:
    """
    Clase que representa un correo electrónico de la UTV
    """
    
    
    #constructor de la clase
    def __init__(self, direccion: str):
        self.direccion = direccion
        self.clasificacion: Optional[str] = None
        self.validar_y_clasificar()
    
    def validar_y_clasificar(self) -> bool:
        """
        Valida que el correo sea de la UTV y lo clasifica como estudiante o docente.
        Retorna True si el correo es válido, False en caso contrario.
        """
        # Patrón para validar correos de la UTV
        patron_estudiante = f"^[a-zA-Z0-9._%+-]+{DOMINIO_ESTUDIANTE}$"
        patron_docente = f"^[a-zA-Z0-9._%+-]+{DOMINIO_DOCENTE}$"
        
        #validacion de correo
        if re.match(patron_estudiante, self.direccion):
            self.clasificacion = TIPO_ESTUDIANTE
            return True
        elif re.match(patron_docente, self.direccion):
            self.clasificacion = TIPO_DOCENTE
            return True
        return False

    def es_valido(self) -> bool:
        """Retorna True si el correo es válido y está clasificado."""
        return self.clasificacion is not None

    def __str__(self) -> str:
        """Retorna una representación en string del correo."""
        return f"Correo: {self.direccion} - Clasificación: {self.clasificacion}"
        