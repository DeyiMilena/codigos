from design_patterns.factory import UserFactory
from design_patterns.observer import UserObserver
from logger import loggerDecorator  # Importamos el decorador

class UserService:   #clase servicio de usuario
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter
        self.observe = UserObserver()

    @log_creation  # Aplica el decorador a create_user
    def create_user(self, user_type, name):
        user = UserFactory.create_user(user_type, name)
        self.db_adapter.execute_query(
            "INSERT INTO users (type, name) VALUES (?, ?)", (user_type, name)
        )
        self.observe.notify(f"El usuario {name}, de tipo {user_type}, se ha creado con éxito.")
        return user    # retorna usuario
