from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect


class DynamicScope(abc.Mapping):

    #initalization
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}

    #get variable names
    def __getitem__(self, key: str) -> Any:

        #if key is found, return key
        if key in self.env:
            return self.env[key]
        else:
            #raise name error if var is not found
            raise NameError("name '{key}' not found")
        

    #iterates through varables
    def __iter__(self) -> Iterator[str]:
        return iter(self.env)

    #determines the number of variables
    def __len__(self) -> int:
        return len(self.env)


def get_dynamic_re() -> DynamicScope:
    #inspects the stack
    stack = inspect.stack()

    #creates an object for Dynamic Scope Class
    dynamicScope = DynamicScope()

    #iterates through each frame 
    for frameInfo in stack[1:]: 

        #frame object
        frame = frameInfo.frame


        #get local variables in the frame
        localVariable = frame.f_locals


        #get free variables in the frame
        freeVariables = frame.f_code.co_freevars



       

        #iterate over each local variable in the frame
        for variableName, variableValue in localVariable.items():

            #check if variable is not free and not currently in dyn scope
            if variableName not in freeVariables and variableName not in dynamicScope.env:

                #add variable and its value to dynamic scope
                dynamicScope.env[variableName] = variableValue
    return dynamicScope


