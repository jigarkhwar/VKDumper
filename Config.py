from configparser import RawConfigParser


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class Config(RawConfigParser):
    def __init__(self):
        super().__init__()
        self.open()
        self['Application'] = {'app_id': '5179007'}

    def __setitem__(self, key, value):
        self.open()
        super().__setitem__(key, value)
        self.save()

    def open(self):
        self.read('config.cfg')

    def save(self):
        with open('config.cfg', 'w') as configfile:
            self.write(configfile)

    @property
    def app_id(self):
        return self['Application']['app_id']

        # @app_id.setter
        # def app_id(self, value):
        #    self.app_id = value
        #    self.config.set('Application', 'app_id', self.app_id)
