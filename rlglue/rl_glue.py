from dataclasses import dataclass
from typing import Any
from rlglue.agent import BaseAgent
from rlglue.environment import BaseEnvironment


@dataclass
class Interaction:
    obs: Any
    action: int | None
    term: bool
    trunc: bool
    reward: float
    extra: dict[str, Any]


class RlGlue:
    def __init__(self, agent: BaseAgent, env: BaseEnvironment):
        self.environment = env
        self.agent = agent

        self.last_action: int | None = None
        self.total_reward: float = 0.0
        self.num_steps: int = 0
        self.total_steps: int = 0
        self.num_episodes: int = 0

    def start(self):
        self.num_steps = 0
        self.total_reward = 0

        s = self.environment.start()
        self.last_action = self.agent.start(s)

        return (s, self.last_action)

    def step(self) -> Interaction:
        assert self.last_action is not None, 'Action is None; make sure to call glue.start() before calling glue.step().'
        (reward, s, term, trunc, extra) = self.environment.step(self.last_action)

        self.total_reward += reward

        self.num_steps += 1
        self.total_steps += 1
        if term:
            self.num_episodes += 1
            self.agent.end(reward, extra)
            return Interaction(
                obs=s,
                action=None,
                term=term,
                trunc=trunc,
                reward=reward,
                extra=extra,
            )

        self.last_action = self.agent.step(reward, s, extra)
        return Interaction(
            obs=s,
            action=self.last_action,
            term=term,
            trunc=trunc,
            reward=reward,
            extra=extra,
        )

    def runEpisode(self, max_steps: int = 0):
        is_terminal = False

        self.start()

        while (not is_terminal) and ((max_steps == 0) or (self.num_steps < max_steps)):
            rl_step_result = self.step()
            is_terminal = rl_step_result.term

        # even at episode cutoff, this still counts as completing an episode
        if not is_terminal:
            self.num_episodes += 1

        return is_terminal
