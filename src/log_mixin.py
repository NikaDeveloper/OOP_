from typing import Set, Type


class LogMixin:
    _log_enabled: bool = True
    _logged_classes: Set[Type["LogMixin"]] = set()  # Аннотированная переменная класса

    def __init__(self, *args, **kwargs):
        cls = self.__class__

        if self._log_enabled and cls not in self._logged_classes:
            print(f"Создан объект класса {cls.__name__} с параметрами:")

            # Получаем параметры __init__ текущего класса
            init = cls.__init__
            param_names = init.__code__.co_varnames[1 : init.__code__.co_argcount]

            for name, value in zip(param_names, args):
                print(f"{name}: {value}")

            for name, value in kwargs.items():
                print(f"{name}: {value}")

            self._logged_classes.add(cls)

        super().__init__()

    @classmethod
    def disable_logging(cls) -> None:
        cls._log_enabled = False

    @classmethod
    def enable_logging(cls) -> None:
        cls._log_enabled = True
