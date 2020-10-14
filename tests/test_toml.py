from unittest import TestCase, main

from wildq.filetypes.toml_type import loader, dumper, colorizer


class TestFiletypeTOML(TestCase):
    def setUp(self):
        self.data = """
    [[keys]]
    key = "value2"

    [[keys]]
    key = "value1"

    [general]
    user = "admin"
"""

    def test_loader(self):
        assert loader(self.data)["general"]["user"] == "admin"

    def test_dumper(self):
        dumped = dumper({"general": {"user": "admin"}})
        assert loader(dumped)["general"]["user"] == "admin"


if __name__ == "__main__":
    main(module="test_toml")
