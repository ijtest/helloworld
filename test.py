import unittest

import helloworld

class TestMyFunc(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_increment_one_1(self):
        self.assertEqual( helloworld.hello(1), "Hello")
  

if __name__ == '__main__':
unittest.main()
