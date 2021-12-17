from typing import Union, Generator


class DataCenter:
    def __init__(self, *data: tuple[object]) -> None:
        """Create new data center."""
        self.data = data

    @property
    def centerdata(self) -> tuple[object]:
        """Get center data."""
        return self.data

class Get:
    def __init__(self, module: str) -> None:
        """Get data from data center."""
        self.module = module

        assert type(module) is str, 'module must be string'

    def get(self, name: str, debug: bool=False) -> Union[None, object, Exception]:
        """Get all data center from file."""
        assert type(name) is str, 'name must be string'
        assert type(debug) is bool, 'debug must be bool'

        try:
            return eval(f'__import__("{self.module}").{name}.centerdata')
        except Exception as err:
            if debug:
                return err

            elif not debug:
                return None

    def getproperty(self, name: str, index: int, debug: bool=False) -> Union[None, object, Exception]:
        """Get property from data center of file."""
        assert type(name) is str, 'name must be string'
        assert type(index) is int, 'index must be int'
        assert type(debug) is bool, 'debug must be bool'

        try:
            return eval(f'__import__("{self.module}").{name}.centerdata[{index - 1}]')
        except Exception as err:
            if debug:
                return err

            elif not debug:
                return None

    def getproperties(self, name: str, debug: bool=False) -> Union[None, Generator, Exception]:
        """Get all properties from data center as generator."""
        assert type(name) is str, 'name must be string'
        assert type(debug) is bool, 'debug must be bool'

        try:
            data = eval(f'__import__("{self.module}").{name}.centerdata')

            for _data in data:
                yield _data
        except Exception as err:
            if debug:
                return err

            elif not debug:
                return None

    def setproperty(self, name: str, index: int, value: object, debug: bool=False) -> Union[None, tuple, Exception]:
        """Update property value."""
        assert type(name) is str, 'name must be string'
        assert type(index) is int, 'index must be int'
        assert type(debug) is bool, 'debug must be bool'

        try:
            properties = list(self.get(name))
            properties[index - 1] = value

            return tuple(properties)
        except Exception as err:
            if debug:
                return err

            elif not debug:
                return None

class FunctionsCenter:
    def __init__(self, *functions: tuple[callable]):
        """Create center with functions."""
        for function in functions:
            if not callable(function):
                raise TypeError('*functions must contain only functions')

        self.functions = functions

    @property
    def center(self):
        """Get all functions center."""
        return self.functions

class FunctionsCaller:
    def __init__(self, module: str) -> None:
        """Get functions from functions center."""
        self.module = module

        assert type(module) is str, 'module must be string'

    def get(self, name: str, debug: bool=False) -> Union[None, object, Exception]:
        """Get all functions center from file."""
        assert type(name) is str, 'name must be string'
        assert type(debug) is bool, 'debug must be bool'

        try:
            return eval(f'__import__("{self.module}").{name}.center')
        except Exception as err:
            if debug:
                return err

            elif not debug:
                return None

    def getproperty(self, name: str, index: int, debug: bool=False) -> Union[None, object, Exception]:
        """Get function from functions center of file."""
        assert type(name) is str, 'name must be string'
        assert type(index) is int, 'index must be int'
        assert type(debug) is bool, 'debug must be bool'

        try:
            return eval(f'__import__("{self.module}").{name}.center[{index - 1}]')
        except Exception as err:
            if debug:
                return err

            elif not debug:
                return None

    def getproperties(self, name: str, debug: bool=False) -> Union[None, Generator, Exception]:
        """Get all functions from function center as generator."""
        assert type(name) is str, 'name must be string'
        assert type(debug) is bool, 'debug must be bool'

        try:
            functions = eval(f'__import__("{self.module}").{name}.center')

            for _func in functions:
                yield _func
        except Exception as err:
            if debug:
                return err

            elif not debug:
                return None

    def setproperty(self, name: str, index: int, func: callable, debug: bool=False) -> Union[None, tuple, Exception]:
        """Update property value."""
        assert type(name) is str, 'name must be string'
        assert type(index) is int, 'index must be int'
        assert callable(func), 'func must be callable'
        assert type(debug) is bool, 'debug must be bool'

        try:
            functions = list(self.get(name))
            functions[index - 1] = func

            return tuple(functions)
        except Exception as err:
            if debug:
                return err

            elif not debug:
                return None

    def call(self, name: str, funcindex: int, debug: bool, *args: tuple[object]) -> Union[None, Exception]:
        """Call function from center."""
        assert type(name) is str, 'name must be string'
        assert type(funcindex) is int, 'funcindex must be int'
        assert type(debug) is bool, 'debug must be bool'

        try:
            eval(f'__import__("{self.module}").{name}.center')[funcindex - 1](*args)
        except Exception as err:
            if debug:
                return err

            elif not debug:
                return None

    def callif(self, name: str, expression: bool, funcindex: int, debug: bool, *args: tuple[object]) -> Union[None, Exception]:
        """Call if expression is true function."""
        assert type(name) is str, 'name must be string'
        assert type(expression) is bool, 'expression must be bool'
        assert type(funcindex) is int, 'funcindex must be int'
        assert type(debug) is bool, 'debug must be bool'

        if expression:
            try:
                eval(f'__import__("{self.module}").{name}.center')[funcindex - 1](*args)
            except Exception as err:
                if debug:
                    return err

                elif not debug:
                    return None

DATASHARE_VERSION = 1.1
