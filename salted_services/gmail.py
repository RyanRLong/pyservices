import smtplib
from environment import EnvironmentMixin, EnvironmentVariableNotFoundError


class Gmail:
    gmail_username = 'GMAIL_USERNAME'
    gmail_password = 'GMAIL_PASSWORD'

    def __init__(self):
        self.username = self.get_username()
        self.password = self.get_password()

    def sendmail(self, recipients, subject, body):
        smtp_server = smtplib.SMTP('smtp.gmail.com, 587')
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(self.username, self.password)

        smtp_server.sendmail(self.username, recipients, "{}::\{}".format(subject, body))
        smtp_server.quit()
        return True

    def get_username(self):
        try:
            return EnvironmentMixin.get_environ_variable_value(self.gmail_username)
        except EnvironmentVariableNotFoundError:
            username = input("Username not set.  Set now: ")
            if username is not None:
                EnvironmentMixin.set_environ_variable_value(self.gmail_username, username)
            return username

    def get_password(self):
        try:
            return EnvironmentMixin.get_environ_variable_value(self.gmail_password)
        except EnvironmentVariableNotFoundError:
            password = input("Password not set.  Set now: ")
            if password is not None:
                EnvironmentMixin.set_environ_variable_value(self.gmail_password, password)
            return password


if __name__ == "__main__":
    gmail = Gmail()
    gmail.sendmail(['ryanlong1004@gmail.com'], 'tst', 'hello world')