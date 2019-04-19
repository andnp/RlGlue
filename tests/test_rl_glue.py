import unittest
import numpy as np
import RlGlue
from RlGlue import RlGlue, BaseEnvironment, BaseAgent

class MarkovChain(BaseEnvironment):
    def __init__(self, params):
        self.state = params['size'] // 2
        self.size = params['size']

    def start(self):
        return self.state

    def step(self, a):
        self.state = self.state + a

        if self.state < 0:
            self.state = 0
        elif self.state >= self.size:
            self.state = self.size - 1

        r = 1 if self.state == 0 else 0
        done = self.state == 0

        return (r, self.state, done)

class TestAgent(BaseAgent):
    def start(self, s):
        return np.random.choice([-1, 0, 1])

    def step(self, r, s):
        if r is None:
            raise Exception('Expected a reward')
        if s is None:
            raise Exception('Expected a state')

        return np.random.choice([-1, 0, 1])

    def end(self, r):
        if r is None:
            raise Exception('Expected a reward')

class TestInterface(unittest.TestCase):
    def test_start(self):
        env = MarkovChain({ 'size': 5 })
        agent = TestAgent()
        exp = RlGlue(agent, env)

        state, action = exp.start()

        self.assertEqual(state, 2)
        self.assertIn(action, [-1, 0, 1])

    def test_step(self):
        env = MarkovChain({ 'size': 5 })
        agent = TestAgent()
        exp = RlGlue(agent, env)

        exp.start()
        (r, s, a, t) = exp.step()

        self.assertIn(r, [0, 1])
        self.assertIn(s, range(5))
        self.assertIn(a, [-1, 0, 1])
        self.assertIn(t, [True, False])

    def test_runEpisode(self):
        env = MarkovChain({ 'size': 5 })
        agent = TestAgent()
        exp = RlGlue(agent, env)

        terminated = exp.runEpisode(100)

        self.assertIn(terminated, [True, False])
        self.assertIn(exp.num_steps, range(100))
        self.assertEqual(exp.total_reward, 1)
        self.assertEqual(exp.num_episodes, 1)