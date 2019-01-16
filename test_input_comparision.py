import unittest
from input_comparision import compareInputs

class TestInput(unittest.TestCase):

    def test_greater_than(self):
        result = compareInputs('1.2','1.3')
        self.assertEqual(result.greater_than(), '1.3 is greater than 1.2')
        
    def test_greater_than(self):
        result = compareInputs('-1.2','-1.3')
        self.assertEqual(result.greater_than(),'-1.3 is greater than -1.2')

    def test_greater_than(self):
        result = compareInputs('1.2','0')
        self.assertEqual(result.greater_than(),'1.2 is greater than 0')
        

    def test_equla(self):
        result = compareInputs('1.2','1.2')
        self.assertEqual(result.equal(), '1.2 is equal to 1.2')

    def test_equla(self):
        result = compareInputs('1.0','1.2')
        self.assertEqual(result.equal(), '1.0 is not equal to 1.2')

    
    
    def test_less_than(self):
        result = compareInputs('1.1','1.2')
        self.assertEqual(result.less_than(), '1.1 is less than 1.2')

    def test_less_than(self):
        result = compareInputs('1.2','1.1')
        self.assertEqual(result.less_than(), '1.2 is less than 1.1')

    def test_less_than(self):
        result = compareInputs('-1.2','-1.1')
        self.assertEqual(result.less_than(), '-1.2 is less than -1.1')



if __name__ == '__main__':
    unittest.main()
