from ProjectEvaluationResult import ProjectEvaluationResult, divide_with_nan


class EvaluationResult:
    def __init__(self) -> None:
        super().__init__()
        self.numberOfGood = 0
        self.numberOfBad = 0
        self.numberOfFoundGood = 0
        self.numberOfFoundBad = 0
        self.numberOfFoundOthers = 0
        self.numberOfFoundGoodWithoutTarget = 0
        self.numberOfFoundBadWithoutTarget = 0
        self.numberOfFoundOthersWithoutTarget = 0
        self.numberOfFoundOthersOnlyGood = 0
        self.numberOfFoundOthersWithoutTargetOnlyGood = 0

    def add_result(self, evaluation_result: ProjectEvaluationResult) -> None:
        self.numberOfGood += evaluation_result.get_good_refactorings_number()
        self.numberOfBad += evaluation_result.get_bad_refactorings_number()
        self.numberOfFoundGood += evaluation_result.get_found_good_refactorings_number()
        self.numberOfFoundBad += evaluation_result.get_found_bad_refactorings_number()
        self.numberOfFoundOthers += evaluation_result.get_found_others_refactorings_number()
        self.numberOfFoundGoodWithoutTarget += evaluation_result.get_found_good_refactorings_without_target_number()
        self.numberOfFoundBadWithoutTarget += evaluation_result.get_found_bad_refactorings_without_target_number()
        self.numberOfFoundOthersWithoutTarget += evaluation_result.get_found_others_refactorings_without_target_number()
        self.numberOfFoundOthersOnlyGood += \
            evaluation_result.get_found_others_refactorings_only_good_number()
        self.numberOfFoundOthersWithoutTargetOnlyGood += \
            evaluation_result.get_found_others_refactorings_without_target_only_good_number()

    def get_good_recall(self) -> float:
        return divide_with_nan(self.numberOfFoundGood, self.numberOfGood)

    def get_good_precision(self) -> float:
        return divide_with_nan(self.numberOfFoundGood, self.get_number_of_found_bad_and_good())

    def get_good_f_measure(self) -> float:
        return divide_with_nan(2 * self.get_good_precision() * self.get_good_recall(),
                               (self.get_good_precision() + self.get_good_recall()))

    def get_bad_precision(self) -> float:
        return divide_with_nan(self.numberOfBad - self.numberOfFoundBad,
                               self.get_number_of_bad_and_good() - self.get_number_of_found_bad_and_good())

    def get_bad_recall(self) -> float:
        return divide_with_nan(self.numberOfBad - self.numberOfFoundBad, self.numberOfBad)

    def get_bad_f_measure(self) -> float:
        return divide_with_nan(2 * self.get_bad_precision() * self.get_bad_recall(),
                               (self.get_bad_precision() + self.get_bad_recall()))

    def get_number_of_bad_and_good(self) -> int:
        return self.numberOfGood + self.numberOfBad

    def get_number_of_found_bad_and_good(self) -> int:
        return self.numberOfFoundGood + self.numberOfFoundBad

    def get_good_recall_without_target(self) -> float:
        return divide_with_nan(self.numberOfFoundGoodWithoutTarget, self.numberOfGood)

    def get_good_precision_without_target(self) -> float:
        return divide_with_nan(self.numberOfFoundGoodWithoutTarget,
                               self.get_number_of_found_bad_and_good_without_target())

    def get_good_f_measure_without_target(self) -> float:
        return divide_with_nan(2 * self.get_good_precision_without_target() * self.get_good_recall_without_target(),
                               (self.get_good_precision_without_target() + self.get_good_recall_without_target()))

    def get_bad_precision_without_target(self) -> float:
        return divide_with_nan(self.numberOfBad - self.numberOfFoundBadWithoutTarget,
                               self.get_number_of_bad_and_good() -
                               self.get_number_of_found_bad_and_good_without_target())

    def get_bad_recall_without_target(self) -> float:
        return divide_with_nan(self.numberOfBad - self.numberOfFoundBadWithoutTarget, self.numberOfBad)

    def get_bad_f_measure_without_target(self) -> float:
        return divide_with_nan(2 * self.get_bad_precision_without_target() * self.get_bad_recall_without_target(),
                               (self.get_bad_precision_without_target() + self.get_bad_recall_without_target()))

    def get_good_recall_only_good(self) -> float:
        return divide_with_nan(self.numberOfFoundGood, self.numberOfGood)

    def get_good_precision_only_good(self) -> float:
        return divide_with_nan(self.numberOfFoundGood, self.numberOfFoundGood + self.numberOfFoundOthersOnlyGood)

    def get_good_f_measure_only_good(self) -> float:
        return divide_with_nan(2 * self.get_good_precision_only_good() * self.get_good_recall_only_good(),
                               (self.get_good_precision_only_good() + self.get_good_recall_only_good()))

    def get_good_recall_without_target_only_good(self) -> float:
        return divide_with_nan(self.numberOfFoundGoodWithoutTarget, self.numberOfGood)

    def get_good_precision_without_target_only_good(self) -> float:
        return divide_with_nan(self.numberOfFoundGoodWithoutTarget,
                               self.numberOfFoundGoodWithoutTarget + self.numberOfFoundOthersWithoutTargetOnlyGood)

    def get_good_f_measure_without_target_only_good(self) -> float:
        return divide_with_nan(2 * self.get_good_precision_without_target_only_good() *
                               self.get_good_recall_without_target_only_good(),
                               (self.get_good_precision_without_target_only_good() +
                                self.get_good_recall_without_target_only_good()))

    def get_good_accuracy(self) -> float:
        return divide_with_nan(self.numberOfFoundGood, self.numberOfFoundGoodWithoutTarget)

    def get_bad_accuracy(self) -> float:
        return divide_with_nan(self.numberOfFoundBad, self.numberOfFoundBadWithoutTarget)

    def get_number_of_found_bad_and_good_without_target(self) -> int:
        return self.numberOfFoundGoodWithoutTarget + self.numberOfFoundBadWithoutTarget
