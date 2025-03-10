from abc import abstractmethod
from typing import Any, Protocol


class BaseEnvironment(Protocol):
    @abstractmethod
    def start(self) -> Any:
        raise NotImplementedError('Expected `start` to be implemented')

    @abstractmethod
    def step(self, action: int) -> tuple[Any, float, bool, bool, dict[str, Any]]:
        raise NotImplementedError('Expected `step` to be implemented')
