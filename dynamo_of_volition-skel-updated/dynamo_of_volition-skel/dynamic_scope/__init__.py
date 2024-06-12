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
    dynamic_scope = DynamicScope()
    frames = inspect.stack()[1:]  # Exclude the current frame

    for frame_info in reversed(frames):
        frame = frame_info.frame
        local_vars = frame.f_locals
        free_vars = frame.f_code.co_freevars

        for var_name, value in local_vars.items():
            if var_name not in free_vars and var_name not in dynamic_scope:
                dynamic_scope[var_name] = value

        # Extra credit: Check for referenced but undefined local variables
        all_vars = set(frame.f_code.co_varnames + frame.f_code.co_cellvars)
        undefined_vars = all_vars - set(local_vars.keys())
        if undefined_vars:
            raise UnboundLocalError(f"Local variable(s) {', '.join(undefined_vars)} referenced before assignment.")

    return dynamic_scope
