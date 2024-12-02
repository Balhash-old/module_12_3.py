import unittest
import test_12_3

runn_test = unittest.TestSuite()
runn_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
runn_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runn_test)

