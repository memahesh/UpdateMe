import unittest
from update_me import UpdateMe

class TestUpdateMe(unittest.TestCase):

	def runTest(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            answer()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def testNo(self):
        self.runTest('no', 'you entered no')

    def testYes(self):
        self.runTest('yes', 'you entered yes')

if __name__ == "__main__":
	unittest.main()