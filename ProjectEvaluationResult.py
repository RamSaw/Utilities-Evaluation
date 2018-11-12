from typing import List

from MoveMethodRefactoring import MoveMethodRefactoring


class ProjectEvaluationResult:
    def __init__(self,
                 good_refactorings: List[MoveMethodRefactoring],
                 bad_refactorings: List[MoveMethodRefactoring],
                 found_refactorings: List[MoveMethodRefactoring],
                 project_name: str) -> None:
        super().__init__()
        self.good_refactorings = list(good_refactorings)
        self.bad_refactorings = list(bad_refactorings)
        assert len(set(self.good_refactorings)) == len(good_refactorings)
        assert len(set(self.bad_refactorings)) == len(bad_refactorings)
        self.found_good_refactorings = list(set(good_refactorings) & set(found_refactorings))
        self.found_bad_refactorings = list(set(bad_refactorings) & set(found_refactorings))
        self.found_others_refactorings = list(set(found_refactorings) -
                                              (set(self.found_bad_refactorings) | set(self.found_good_refactorings)))
        if len(self.good_refactorings) != 0 and len(self.found_good_refactorings) == 0:
            print("SUSPICIOUS PROJECT: " + project_name + ", no bad and good refactorings found")

    def get_good_refactorings_number(self) -> int:
        return len(self.good_refactorings)

    def get_bad_refactorings_number(self) -> int:
        return len(self.bad_refactorings)

    def get_found_good_refactorings_number(self) -> int:
        return len(self.found_good_refactorings)

    def get_found_bad_refactorings_number(self) -> int:
        return len(self.found_bad_refactorings)

    def get_found_others_refactorings_number(self) -> int:
        return len(self.found_others_refactorings)
