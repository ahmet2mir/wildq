from unittest import TestCase, main

from wildq.filetypes.xml_type import loader, dumper, colorizer


class TestFiletypeXML(TestCase):
    def setUp(self):
        self.data = """<?xml version="1.0" encoding="UTF-8"?>
    <root>
       <general>
          <user>admin</user>
       </general>
       <keys>
          <element>
             <key>value1</key>
          </element>
          <element>
             <key>value2</key>
          </element>
          <element>alone</element>
       </keys>
    </root>
"""

    def test_loader(self):
        assert loader(self.data)["root"]["general"]["user"] == "admin"

    def test_dumper(self):
        dumped = dumper({"general": {"user": "admin"}})
        assert loader(dumped)["general"]["user"] == "admin"

        dumped = dumper({"general": {"user": "admin"}, "otherroot": 1})
        assert loader(dumped)["virtualroot"]["general"]["user"] == "admin"


if __name__ == "__main__":
    main(module="test_xml")
