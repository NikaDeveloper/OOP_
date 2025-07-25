class LogMixin:
    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        for arg_name, arg_value in zip(self.__init__.__code__.co_varnames[1:], args):
            print(f"{arg_name}: {arg_value}")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        super().__init__(*args, **kwargs)
