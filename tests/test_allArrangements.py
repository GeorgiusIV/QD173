
import unittest
import main
import CharOrdException

class method_testing(unittest.TestCase):
    def rearrange_letters_should_be_True(self):

        answer = ["abc","acb","bac","bca","cba","cab"]
        self.assertEqual(main.allArrangements("a","b","c"), answer)

    def rearrange_letters_should_be_True(self):
        
        self.assertRaises(main.allArrangements("a","b",1), TypeError)

    def rearrange_letters_should_be_True(self):
        
        self.assertEqual(main.allArrangements("a","b","]"), CharOrdException.CharOrdError)




if __name__ == "__main__":
    method_testing.run()