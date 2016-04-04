from Config import Config


class VKUser(object):
    def __init__(self, api):
        config = Config.Instance()
        data = api.users.get()
        self.vk_id = data[0]['id']
        self.first_name = data[0]['first_name']
        self.last_name = data[0]['last_name']
        config['User'] = {'id': self.vk_id,
                          'first_name': self.first_name,
                          'last_name': self.last_name}
        print('Добрый день, ', self.first_name + ' ' + self.last_name)
