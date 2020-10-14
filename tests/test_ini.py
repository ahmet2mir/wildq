from unittest import TestCase, main

from wildq.filetypes.ini_type import loader, dumper, colorizer


class TestFiletypeINI(TestCase):
    def setUp(self):
        self.data = """
[general]
user = admin

[keys]
key1 = value1
key2 = value2
"""

    def test_loader(self):
        assert loader(self.data)["general"]["user"] == "admin"

    def test_dumper(self):
        dumped = dumper({"general": {"user": "admin"}})
        assert loader(dumped)["general"]["user"] == "admin"


if __name__ == "__main__":
    main(module="test_ini")
