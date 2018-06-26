"""
Ryan Long
2018-06-26
sms.py
"""
from twilio.rest import Client
from salted_services.environment import EnvironmentMixin, EnvironmentVariableNotFoundError


class SmsService(EnvironmentMixin):
    """
    This module is responsible for interacting with
    the twilio API to send and receive text messages
    from a number.

    It used EnvironmentMixin to set and get environment
    varibles that are not already set.
    """

    _TWILIO_ACCOUNT_ID = 'TWILIO_ACCOUNT_SID'
    _TWILIO_TOKEN = 'TWILIO_AUTH_TOKEN'

    def __init__(self):
        self.account = self.get_twilio_account_id()
        self.token = self.get_twilio_token()
        self.client = Client(self.account, self.token)

    def send_message(self, message, to_number, from_number="+14153002630"):
        """
        Sends an sms message via the twilio API.  The from number must be valid
        and owned by the twilio account.

        :param message: message to be sent
        :param to_number: 10 digit phone number of recipient
        :param from_number: 10 digit phone number of sender.  Must be
        a valid phone number owned by the twilio account.
        :return: boolean
        """
        message = self.client.messages.create(to=to_number, from_=from_number, body=message)
        if message.error_code is None:
            return True
        return False

    def get_twilio_account_id(self):
        """
        Returns the twilio account id environment variable

        If the Id is not set, the user will be prompted to set it
        via the command line.

        :return: string
        """
        try:
            return self.get_environ_variable_value(self._TWILIO_ACCOUNT_ID)
        except EnvironmentVariableNotFoundError as e:
            if y == input(e.message + ". Would you like to set it now? (Y)").lower():
                self.set_environ_variable_value(self._TWILIO_ACCOUNT_ID, input("Enter value now: "))
                return self.get_environ_variable_value(self._TWILIO_ACCOUNT_ID)
            exit(2)


    def get_twilio_token(self):
        """
        Returns the twilio account token environment variable

        If the Id is not set, the user will be prompted to set it
        via the command line.

        :return: string
        """
        try:
            return self.get_environ_variable_value(self._TWILIO_TOKEN)
        except EnvironmentVariableNotFoundError as e:
            if y == input(e.message + ". Would you like to set it now? (Y)").lower():
                self.set_environ_variable_value(self._TWILIO_TOKENinput("Enter value now: "))
                return self.get_environ_variable_value(self._TWILIO_TOKEN)
            exit(2)


if __name__ == "__main__":
    sms = SmsService()
    sms.send_message("Hey", "+15707661004")
