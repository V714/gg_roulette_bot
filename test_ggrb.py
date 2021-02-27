# Unittest of GG bot by V7

import unittest
from .dir import main

class ParserTest(unittest.TestCase):
    
    def setup(self):
        self.parser = main.make.parse_args()


if __name__ == '__main__':

    parser = main.make.parse_args(["--login", "123","--passw", "456"])
    args = parser.parse_args()
    print(args)