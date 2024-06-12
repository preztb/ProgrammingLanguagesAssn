from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}

    def __getitem__(self, key: str) -> Any:
        if key not in self.env:
            raise NameError(f"Name '{key}' is not defined.")
        return self.env[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.env[key] = value

    def __iter__(self) -> Iterator[str]:
        return iter(self.env)

    def __len__(self) -> int:
        return len(self.env)


def get_dynamic_re() -> DynamicScope:
    return None
