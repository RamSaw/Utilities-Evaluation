import unittest

from JDeodorantMoveMethodLoader import JDeodorantMoveMethodLoader
from MoveMethodRefactoring import MoveMethodRefactoring


class InputTest(unittest.TestCase):
    def test_input(self):
        refactoring1 = MoveMethodRefactoring("org.apache.B", "org.apache.A",
                                             "method1", ["P1", "P2", "P3"])
        refactoring2 = MoveMethodRefactoring("org.apache.B", "org.apache.A",
                                             "method1", ["List<? extends Bclass>", "List<K>", "P3"])
        refactoring3 = MoveMethodRefactoring("org.apache.B", "org.apache.A", "method1",
                                             ["List<? extends Bclass>", "Map<String,? extends Person>", "Model<T>"])
        refactoring4 = MoveMethodRefactoring("org.apache.B", "org.apache.A", "method1",
                                             ["Map<String,Person>"])
        refactoring5 = MoveMethodRefactoring("org.apache.B", "org.apache.A", "method1",
                                             [])
        expected_refactorings = [refactoring1, refactoring2, refactoring3, refactoring4, refactoring5]
        self.assertEqual(expected_refactorings, JDeodorantMoveMethodLoader.load("./testInput"))


if __name__ == '__main__':
    unittest.main()
