from Config import Config
import getpass


class VKAccount:
    def __init__(self):
        config = Config.Instance()
        try:
            self.login = config['Account']['login']
            print("Your login is ", self.login)
        except Exception:
            print("Enter your login: ")
            self.login = input()
            config['Account'] = {'login': self.login}
        self.password = getpass.getpass(prompt='Enter your password: ')
