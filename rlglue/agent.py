from abc import abstractmethod
from typing import Any, Protocol


class BaseAgent(Protocol):
    @abstractmethod
    def start(self, obs: Any) -> int:
        raise NotImplementedError('Expected `start` to be implemented')

    @abstractmethod
    def step(self, reward: float, obs: Any, extra: dict[str, Any]) -> int:
        raise NotImplementedError('Expected `step` to be implemented')

    @abstractmethod
    def end(self, reward: float, extra: dict[str, Any]) -> None:
        raise NotImplementedError('Expected `end` to be implemented')
