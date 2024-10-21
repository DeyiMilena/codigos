import datetime

# Decorador que añade funcionalidad de logging con inicialización de archivo
class loggerDecorator:
    def __init__(self, log_file_name="user_creation_log.txt"):
        # Inicializa el nombre del archivo de log donde se guardarán los registros.
        self.log_file_name = log_file_name

    def __call__(self, func):
        # Este método convierte a la clase en un decorador que puede ser aplicado a funciones.
        def wrapper(*args, **kwargs):
            # Llama a la función original (creación de usuario) y almacena el resultado en la variable 'user'.
            user = func(*args, **kwargs)
            # Abre el archivo de log en modo append para agregar nuevas entradas sin sobrescribir el contenido existente.
            with open(self.log_file_name, "a") as log_file:
                # Escribe la fecha y hora actuales junto con el nombre del usuario creado en el archivo de log.
                log_file.write(f"{datetime.datetime.now()}: Usuario {user.name} creado.\n")
            # Imprime un mensaje de log en la consola informando que se ha creado un nuevo usuario.
            print(f"Log: Se ha creado el usuario {user.name}.")
            # Retorna el objeto 'user' creado, permitiendo que la función original siga funcionando como se esperaba.
            return user
        return wrapper  # Retorna la función 'wrapper' que contiene la lógica adicional del decorador.
