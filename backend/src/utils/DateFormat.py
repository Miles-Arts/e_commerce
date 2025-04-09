from datetime import datetime

class DateFormat:
    @staticmethod
    def convert_data(value):
        try:
            # Asegúrate de que el valor sea una cadena
            if not isinstance(value, str):
                value = str(value)

            # Valida que el valor esté en el formato estándar YYYY-MM-DD
            datetime.strptime(value, '%Y-%m-%d')  # Valida el formato
            return value  # Devuelve el valor tal cual si es válido
        except ValueError as ex:
            raise ValueError(f"Error al convertir la fecha: {value}. Detalles: El formato debe ser YYYY-MM-DD.")