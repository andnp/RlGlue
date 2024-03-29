from abc import abstractmethod
from typing import Any, Dict


class BaseAgent:
    @abstractmethod
    def start(self, observation: Any) -> int:
        raise NotImplementedError('Expected `start` to be implemented')

    @abstractmethod
    def step(self, reward: float, observation: Any, extra: Dict[str, Any]) -> int:
        raise NotImplementedError('Expected `step` to be implemented')

    @abstractmethod
    def end(self, reward: float, extra: Dict[str, Any]) -> None:
        raise NotImplementedError('Expected `end` to be implemented')
