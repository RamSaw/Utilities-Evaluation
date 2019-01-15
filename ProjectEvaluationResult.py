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
        self.found_refactorings = list(found_refactorings)
        assert len(set(self.good_refactorings)) == len(good_refactorings)
        assert len(set(self.bad_refactorings)) == len(bad_refactorings)
        self.found_good_refactorings = list(set(good_refactorings) & set(found_refactorings))
        self.found_bad_refactorings = list(set(bad_refactorings) & set(found_refactorings))
        self.found_others_refactorings = list(set(found_refactorings) -
                                              (set(self.found_bad_refactorings) | set(self.found_good_refactorings)))
        if len(self.good_refactorings) != 0 and len(self.found_good_refactorings) == 0:
            print("SUSPICIOUS PROJECT: " + project_name + ", no bad and good refactorings found")
        # without target counting
        self.good_refactorings_without_target = list(good_refactorings)
        for refactoring in self.good_refactorings_without_target:
            refactoring.target_class_qualified_name = None
        self.bad_refactorings_without_target = list(bad_refactorings)
        for refactoring in self.bad_refactorings_without_target:
            refactoring.target_class_qualified_name = None
        self.found_refactorings_without_target = list(found_refactorings)
        for refactoring in self.found_refactorings_without_target:
            refactoring.target_class_qualified_name = None
        self.found_good_refactorings_without_target = list(set(self.good_refactorings_without_target) &
                                                           set(self.found_refactorings_without_target))
        self.found_bad_refactorings_without_target = list(set(self.bad_refactorings_without_target) &
                                                          set(self.found_refactorings_without_target))
        self.found_others_refactorings_without_target = list(set(self.found_refactorings_without_target) -
                                                             (set(self.found_bad_refactorings_without_target) |
                                                              set(self.found_good_refactorings_without_target)))

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

    def get_found_good_refactorings_without_target_number(self) -> int:
        return len(self.found_good_refactorings_without_target)

    def get_found_bad_refactorings_without_target_number(self) -> int:
        return len(self.found_bad_refactorings_without_target)

    def get_found_others_refactorings_without_target_number(self) -> int:
        return len(self.found_others_refactorings_without_target)
