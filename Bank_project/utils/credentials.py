import base64

class Credentials:
    # Храним пароль в base64 (или другом виде)
    _ENCODED_PASSWORD = "YWRtaW4xMjM="  # это "admin123" в base64

    @staticmethod
    def get_password():
        # Декодируем перед использованием
        return base64.b64decode(Credentials._ENCODED_PASSWORD).decode("utf-8")

    @staticmethod
    def get_username():
        return "admin"