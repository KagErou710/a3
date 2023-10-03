import unittest
from model import testModel
import numpy as np

class TestYourModel(unittest.TestCase):

    def test_model_input(self):
        input_data = [1, 2, 3]
        input_array = np.array(input_data)
        output = testModel(input_array)
        self.assertEqual(output.shape, (len(input_array),))

    def test_model_output_shape(self):
        dummy_input = [4, 5, 6]
        input_array = np.array(dummy_input)
        output = testModel(input_array)
        self.assertEqual(output.shape, (len(input_array),))

if __name__ == '__main__':
    unittest.main()
