# Unittest of GG bot by V7

import unittest
import main

class ParserTest(unittest.TestCase):
    
    def setup(self):
        self.parser = main.parse_args()

    def test_sex(self):
        parser = main.make_parse_args(["--login", "123","--passw", "123"])
        args = parser.parse_args() 
        self.assertIsNotNone(args.login)