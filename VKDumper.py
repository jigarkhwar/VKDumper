from Config import Config
import vk_requests

from VKAccount import VKAccount
from VKUser import VKUser


def main():
    config = Config.Instance()
    account = VKAccount()

    api = vk_requests.create_api(app_id=config.app_id, login=account.login, password=account.password)

    vk_user = VKUser(api)


if __name__ == '__main__':
    main()
