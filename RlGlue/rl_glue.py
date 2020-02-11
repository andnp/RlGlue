class RlGlue:
    def __init__(self, agent, env):
        self.environment = env
        self.agent = agent

        self.last_action = None
        self.total_reward = 0.0
        self.num_steps = 0
        self.num_episodes = 0

    def start(self):
        self.num_steps = 0
        self.total_reward = 0

        s = self.environment.start()
        obs = self.observationChannel(s)
        self.last_action = self.agent.start(obs)

        return (obs, self.last_action)

    def step(self):
        (reward, s, term) = self.environment.step(self.last_action)
        obs = self.observationChannel(s)

        self.total_reward += reward

        if term:
            self.num_episodes += 1
            self.agent.end(reward)
            roat = (reward, obs, None, term)
        else:
            self.num_steps += 1
            self.last_action = self.agent.step(reward, obs)
            roat = (reward, obs, self.last_action, term)

        self.recordTrajectory(roat[1], roat[2], roat[0], roat[3])
        return roat

    def runEpisode(self, max_steps = 0):
        is_terminal = False

        self.start()

        while (not is_terminal) and ((max_steps == 0) or (self.num_steps < max_steps)):
            rl_step_result = self.step()
            is_terminal = rl_step_result[3]

        return is_terminal

    def observationChannel(self, s):
        return s

    def recordTrajectory(self, s, a, r, t):
        pass
