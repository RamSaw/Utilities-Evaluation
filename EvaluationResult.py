from ProjectEvaluationResult import ProjectEvaluationResult


def divide_with_nan(a: float, b: float) -> float:
    return a / b if b != 0 else float('nan')


class EvaluationResult:
    def __init__(self) -> None:
        super().__init__()
        self.numberOfGood = 0
        self.numberOfBad = 0
        self.numberOfFoundGood = 0
        self.numberOfFoundBad = 0
        self.numberOfFoundOthers = 0

    def add_result(self, evaluation_result: ProjectEvaluationResult) -> None:
        self.numberOfGood += evaluation_result.get_good_refactorings_number()
        self.numberOfBad += evaluation_result.get_bad_refactorings_number()
        self.numberOfFoundGood += evaluation_result.get_found_good_refactorings_number()
        self.numberOfFoundBad += evaluation_result.get_found_bad_refactorings_number()
        self.numberOfFoundOthers += evaluation_result.get_found_others_refactorings_number()

    def get_good_recall(self) -> float:
        return divide_with_nan(self.numberOfFoundGood, self.numberOfGood)

    def get_good_precision(self) -> float:
        return divide_with_nan(self.numberOfFoundGood, self.get_number_of_found_bad_and_good())

    def get_bad_precision(self) -> float:
        return divide_with_nan(self.numberOfBad - self.numberOfFoundBad,
                               self.get_number_of_bad_and_good() - self.get_number_of_found_bad_and_good())

    def get_bad_recall(self) -> float:
        return divide_with_nan(self.numberOfBad - self.numberOfFoundBad, self.numberOfBad)

    def get_number_of_bad_and_good(self) -> int:
        return self.numberOfGood + self.numberOfBad

    def get_number_of_found_bad_and_good(self) -> int:
        return self.numberOfFoundGood + self.numberOfFoundBad
