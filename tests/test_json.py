from unittest import TestCase, main

from wildq.filetypes.json_type import loader, dumper, colorizer


class TestFiletypeJSON(TestCase):
    def setUp(self):
        self.data = """
{
    "general": {
        "user": "admin"
    },
    "keys": [
        {"key": "value1"},
        {"key": "value2"},
        "alone"
    ]
}
"""

    def test_loader(self):
        assert loader(self.data)["general"]["user"] == "admin"

    def test_dumper(self):
        dumped = dumper({"general": {"user": "admin"}})
        assert loader(dumped)["general"]["user"] == "admin"


if __name__ == "__main__":
    main(module="test_json")
