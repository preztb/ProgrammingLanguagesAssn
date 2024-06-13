from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}

    def __getitem__(self, key: str) -> Any:
        return self.env.get(key, False)

    def __setitem__(self, key: str, value: Any) -> None:
        self.env[key] = value

    def __iter__(self) -> Iterator[str]:
        return iter(self.env)

    def __len__(self) -> int:
        return len(self.env)


def get_dynamic_re() -> DynamicScope:
    dynamic_scope = DynamicScope()
    frames = inspect.stack()[1:]  # Exclude the current frame

    for frame_info in reversed(frames):
        frame = frame_info.frame
        local_vars = frame.f_locals
        free_vars = frame.f_code.co_freevars

        for var_name, value in local_vars.items():
            if var_name not in free_vars and var_name not in dynamic_scope:
                dynamic_scope[var_name] = value

        

    return dynamic_scope
