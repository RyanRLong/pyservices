from twilio.rest import Client
from service.environment import Environment as env_

class SmsService:

    def __init__(self):
        self.account = env_.get_twilio_account_id()
        self.token = env_.get_twilio_token()
        self.client = Client(self.account, self.token)

    def send_message(self, message, to_number, from_number="+14153002630"):
        message = self.client.messages.create(to=to_number, from_=from_number, body=message)
        if message.error_code is None:
            return True
        return False


    def buy_number(self, area_code):
        numbers = self._get_twilio_client().available_phone_numbers("US") \
            .local \
            .list(area_code=area_code,
                  sms_enabled=True,
                  voice_enabled=True)

        if numbers:
            number = self._purchase_number(numbers[0])
            self.anonymous_phone_number = number
            return number
        else:
            numbers = self._get_twilio_client().available_phone_numbers("US") \
                .local \
                .list(sms_enabled=True, voice_enabled=True)

            if numbers:
                number = self._purchase_number(numbers[0])
                self.anonymous_phone_number = number
                return number

        return None

if __name__ == "__main__":
    sms = SmsService()
    sms.send_message("Hey", "+15707661004")