from src.log_mixin import LogMixin


def test_log_mixin_output(capsys):
    class TempClass(LogMixin):
        def __init__(self, param1, param2, **kwargs):
            self.param1 = param1
            self.param2 = param2
            super().__init__(param1, param2, **kwargs)

    LogMixin.enable_logging()
    LogMixin._logged_classes.clear()  # Очищаем перед тестом
    _ = TempClass("value1", "value2", extra_param="extra_value")

    captured = capsys.readouterr()
    output = captured.out
    assert "Создан объект класса TempClass с параметрами:" in output
    assert "param1: value1" in output
    assert "param2: value2" in output
    assert "extra_param: extra_value" in output


def test_log_mixin_disabled(capsys):
    class TempClass(LogMixin):
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2
            super().__init__(p1, p2)

    LogMixin.disable_logging()
    LogMixin._logged_classes.clear()
    _ = TempClass("value1", "value2")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_log_mixin_no_duplicate_logging(capsys):
    class TempClass(LogMixin):
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2
            super().__init__(p1, p2)

    LogMixin.enable_logging()
    LogMixin._logged_classes.clear()  # Очищаем перед тестом

    # Первое создание - должно вывести сообщение
    _ = TempClass("v1", "v2")
    captured = capsys.readouterr()
    assert "Создан объект класса TempClass" in captured.out
    assert captured.out.count("Создан объект класса") == 1

    # Повторное создание - не должно выводить
    _ = TempClass("v3", "v4")
    captured = capsys.readouterr()
    assert captured.out == ""

    # Проверяем, что класс остался в _logged_classes
    assert TempClass in LogMixin._logged_classes
