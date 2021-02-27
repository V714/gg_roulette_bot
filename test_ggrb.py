# Unittest of GG bot by V7

import unittest
import ggrb

class ParserTest(unittest.TestCase):
    
    def test_values(self):
        login = "test_login"
        password = "test_password"
        sex = 'female'
        loops = '34'

        parser = ggrb.make_parse_args(["--login",login,"--passw",password,'--sex',sex,'--loops',loops])

        self.assertEqual(parser.login, login)
        self.assertEqual(parser.passw, password)
        self.assertEqual(parser.sex, sex)
        self.assertEqual(str(parser.loops), loops)

if __name__ == '__main__':
    unittest.main()