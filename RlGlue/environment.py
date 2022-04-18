from abc import abstractmethod
from typing import Any, Tuple


class BaseEnvironment:
    @abstractmethod
    def start(self) -> Any:
        raise NotImplementedError('Expected `start` to be implemented')

    @abstractmethod
    def step(self, action: int) -> Tuple[float, Any, bool]:
        raise NotImplementedError('Expected `step` to be implemented')
