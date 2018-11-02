import unittest

from EvaluationResult import EvaluationResult
from Evaluator import Evaluator


class ComplexTest(unittest.TestCase):
    dataset_path = "./"
    numberOfGood_project1 = 0
    numberOfGood_project2 = 3
    numberOfGood_project3 = 3
    numberOfGood_project1_found = 0
    numberOfGood_project2_found = 2
    numberOfGood_project3_found = 2
    numberOfBad_project1 = 3
    numberOfBad_project2 = 0
    numberOfBad_project3 = 3
    numberOfBad_project1_found = 2
    numberOfBad_project2_found = 0
    numberOfBad_project3_found = 2
    numberOfOthers_project1_found = 1
    numberOfOthers_project2_found = 2
    numberOfOthers_project3_found = 3
    numberOfGood_all = numberOfGood_project1 + numberOfGood_project2 + numberOfGood_project3
    numberOfBad_all = numberOfBad_project1 + numberOfBad_project2 + numberOfBad_project3
    numberOfGood_all_found = numberOfGood_project1_found + numberOfGood_project2_found + numberOfGood_project3_found
    numberOfBad_all_found = numberOfBad_project1_found + numberOfBad_project2_found + numberOfBad_project3_found
    numberOfOthers_all_found = numberOfOthers_project1_found + numberOfOthers_project2_found \
        + numberOfOthers_project3_found
    goodPrecision = numberOfGood_all_found / (numberOfGood_all_found + numberOfBad_all_found)
    goodRecall = numberOfGood_all_found / numberOfGood_all
    badPrecision = (numberOfBad_all - numberOfBad_all_found) / \
        (numberOfGood_all + numberOfBad_all - numberOfBad_all_found - numberOfGood_all_found)
    badRecall = (numberOfBad_all - numberOfBad_all_found) / numberOfBad_all

    def test_evaluate_all_dataset(self):
        evaluation_result = Evaluator.evaluate(ComplexTest.dataset_path)
        self.assertEqual(self.numberOfGood_all, evaluation_result.numberOfGood)
        self.assertEqual(self.numberOfGood_all_found, evaluation_result.numberOfFoundGood)
        self.assertEqual(self.numberOfBad_all, evaluation_result.numberOfBad)
        self.assertEqual(self.numberOfBad_all_found, evaluation_result.numberOfFoundBad)
        self.assertEqual(self.numberOfOthers_all_found, evaluation_result.numberOfFoundOthers)
        self.assertEqual(self.goodPrecision, evaluation_result.get_good_precision())
        self.assertEqual(self.goodRecall, evaluation_result.get_good_recall())
        self.assertEqual(self.badPrecision, evaluation_result.get_bad_precision())
        self.assertEqual(self.badRecall, evaluation_result.get_bad_recall())

if __name__ == '__main__':
    unittest.main()
