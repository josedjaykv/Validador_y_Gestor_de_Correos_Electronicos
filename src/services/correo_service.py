'''- Solicitar al usuario que ingrese una dirección de correo electrónico.
- Validar la dirección usando una expresión regular sencilla.
- Clasificar automáticamente el correo como 'estudiante' o 'docente', basándose en la estructura del correo:
   • Estudiantes: terminan con "@estudiante.utv.edu.co"
   • Docentes: terminan con "@utv.edu.co"
- Almacenar los correos válidos junto con su clasificación en una colección adecuada.'''

from typing import List, Optional
from models.correo import Correo
from utils.constantes import TIPO_ESTUDIANTE, TIPO_DOCENTE
import difflib

class CorreoService:
    _correos: List[Correo] = []

    @classmethod
    def registrar_correo(cls, direccion: str) -> bool:
        """
        Registra un nuevo correo electrónico.
        Retorna True si el registro fue exitoso, False en caso contrario.
        """
        try:
            correo = Correo(direccion)
            if not correo.es_valido():
                print("Error: El correo no tiene un formato válido para la UTV")
                return False
            
            # Verificar si el correo ya existe
            if correo in cls._correos:
                print("Error: Este correo ya está registrado")
                return False
            
            cls._correos.append(correo)
            print(f"Correo registrado exitosamente: {correo}")
            return True
            
        except Exception as e:
            print(f"Error al registrar el correo: {str(e)}")
            return False

    @classmethod
    def obtener_correos(cls) -> List[Correo]:
        """Retorna la lista de todos los correos registrados."""
        return cls._correos

    @classmethod
    def obtener_correos_estudiantes(cls) -> List[Correo]:
        """Retorna la lista de correos de estudiantes."""
        return [correo for correo in cls._correos if correo.clasificacion == TIPO_ESTUDIANTE]

    @classmethod
    def obtener_correos_docentes(cls) -> List[Correo]:
        """Retorna la lista de correos de docentes."""
        return [correo for correo in cls._correos if correo.clasificacion == TIPO_DOCENTE]

    @classmethod
    def buscar_por_direccion(cls, direccion: str) -> list[Correo]:
        """Busca todos los correos con direcciones similares a la buscada."""
        direcciones = [correo.direccion.lower() for correo in cls._correos]
        similares = difflib.get_close_matches(direccion.lower(), direcciones, n=len(direcciones), cutoff=0.3)
        
        coincidencias = []
        for correo in cls._correos:
            if correo.direccion.lower() in similares:
                coincidencias.append(correo)
        return coincidencias

    @classmethod
    def buscar_por_dominio(cls, dominio: str) -> List[Correo]:
        """Busca correos que contengan el dominio especificado."""
        return [correo for correo in cls._correos if dominio in correo.direccion]

    @classmethod
    def obtener_por_clasificacion(cls, clasificacion: str) -> List[Correo]:
        """Retorna los correos de una clasificación específica (estudiante/docente)."""
        return [correo for correo in cls._correos if correo.clasificacion == clasificacion]

    def mostrar_correos(self):
        pass 