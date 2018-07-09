"""
Ryan Long
2018-07-08
gmail.py
"""
import smtplib
from environment import EnvironmentMixin, EnvironmentVariableNotFoundError


class Gmail:
    """
    Coordinates with gmail to send emails
    """
    gmail_username = 'GMAIL_USERNAME'
    gmail_password = 'GMAIL_PASSWORD'

    def __init__(self):
        self.username = self.get_username()
        self.password = self.get_password()

    def sendmail(self, recipients, subject, body):
        """
        Send text mail to the recipient

        :param recipients: list of recipients
        :param subject:
        :param body:
        :return: boolean
        """
        smtp_server = smtplib.SMTP('smtp.gmail.com, 587')
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(self.username, self.password)

        smtp_server.sendmail(self.username, recipients, "{}::\{}".format(subject, body))
        smtp_server.quit()
        return True

    def get_username(self):
        """
        Get username from the environment
        :return: string
        """
        try:
            return EnvironmentMixin.get_environ_variable_value(self.gmail_username)
        except EnvironmentVariableNotFoundError:
            username = input("Username not set.  Set now: ")
            return username

    def get_password(self):
        """
        Get password from environment
        :return:
        """
        try:
            return EnvironmentMixin.get_environ_variable_value(self.gmail_password)
        except EnvironmentVariableNotFoundError:
            password = input("Password not set.  Set now: ")
            return password


if __name__ == "__main__":
    gmail = Gmail()
    gmail.sendmail(['ryanlong1004@gmail.com'], 'tst', 'hello world')