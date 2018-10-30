import unittest

from MoveMethodRefactoring import MoveMethodRefactoring
from ProjectEvaluationResult import ProjectEvaluationResult


class ProjectEvaluationResultTest(unittest.TestCase):
    def test_complex(self):
        move_method_1 = MoveMethodRefactoring("A", "B", "m1", ["P1, P2"])
        move_method_2 = MoveMethodRefactoring("C", "B", "m2", ["P3, P2"])
        move_method_3 = MoveMethodRefactoring("A", "C", "m3", ["P3, P4"])
        move_method_5 = MoveMethodRefactoring("B", "D", "m5", ["P5, P6"])
        found_move_method_1 = MoveMethodRefactoring("A", "B", "m1", ["P1, P2"])
        found_move_method_3 = MoveMethodRefactoring("A", "C", "m3", ["P3, P4"])
        found_move_method_4 = MoveMethodRefactoring("B", "A", "m4", ["P5, P6"])
        found_move_method_5 = MoveMethodRefactoring("B", "D", "m5", ["P5, P6"])
        good = [move_method_1, move_method_2, move_method_5]
        bad = [move_method_3]
        found = [found_move_method_1, found_move_method_3, found_move_method_4, found_move_method_5]
        result = ProjectEvaluationResult(good, bad, found)
        self.assertEqual(3, result.get_good_refactorings_number())
        self.assertEqual(1, result.get_bad_refactorings_number())
        self.assertEqual(2, result.get_found_good_refactorings_number())
        self.assertEqual(2, result.get_found_good_refactorings_number())
        self.assertEqual(1, result.get_found_bad_refactorings_number())
        self.assertEqual(1, result.get_found_others_refactorings_number())


if __name__ == '__main__':
    unittest.main()
