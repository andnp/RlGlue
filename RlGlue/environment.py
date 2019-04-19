class BaseEnvironment:
    def init(self, params={}):
        raise NotImplementedError('Expected `init` to be implemented')

    def start(self):
        raise NotImplementedError('Expected `init` to be implemented')

    def step(self, action):
        raise NotImplementedError('Expected `init` to be implemented')
