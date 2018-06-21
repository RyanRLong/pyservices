import os


class Environment:

    _TWILIO_ACCOUNT_ID = 'TWILIO_ACCOUNT_SID'
    _TWILIO_TOKEN = 'TWILIO_AUTH_TOKEN'

    @classmethod
    def get_twilio_account_id(cls):
        return cls._get_environ_variable_value(cls._TWILIO_ACCOUNT_ID)

    @classmethod
    def get_twilio_token(cls):
        return cls._get_environ_variable_value(cls._TWILIO_TOKEN)

    @classmethod
    def get_twilio_credentials(cls):
        return tuple(cls.get_twilio_account_id(), cls.get_twilio_credentials())

    @staticmethod
    def _get_environ_variable_value(name):
        return os.environ[name]
