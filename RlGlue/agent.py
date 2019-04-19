class BaseAgent:
    def start(self, observation):
        raise NotImplementedError('Expected `start` to be implemented')

    def step(self, reward, observation):
        raise NotImplementedError('Expected `step` to be implemented')

    def end(self, reward):
        raise NotImplementedError('Expected `end` to be implemented')
