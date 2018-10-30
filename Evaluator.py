import os

from ProjectEvaluator import JDeodorantProjectEvaluator
from EvaluationResult import EvaluationResult


class Evaluator:
    @staticmethod
    def evaluate(dataset_root_path: str) -> EvaluationResult:
        evaluation_result = EvaluationResult()
        with open("../project_evaluation_results", "w") as f:
            for project in os.listdir(dataset_root_path):
                project_result = JDeodorantProjectEvaluator.evaluate(os.path.join(dataset_root_path, project))
                if project_result is None:
                    print("No file with found refactorings for " + project + " project")
                    continue
                f.write("===========" + project + "===========" + "\n")
                f.write("Good refactorings number: " + str(project_result.get_good_refactorings_number()) + "\n")
                f.write("Bad refactorings number: " + str(project_result.get_bad_refactorings_number()) + "\n")
                f.write("Found good refactorings number: " + str(project_result.get_found_good_refactorings_number()) + "\n")
                f.write("Found bad refactorings number: " + str(project_result.get_found_bad_refactorings_number()) + "\n")
                f.write("Found others refactorings number: " +
                        str(project_result.get_found_others_refactorings_number()) + "\n")
                f.write("\n\n")
                evaluation_result.add_result(project_result)
            return evaluation_result


def write_result_to_file(filename: str, evaluation_result: EvaluationResult):
    with open(filename, "w") as f:
        string_to_write = "Good Precision: " + str(evaluation_result.get_good_precision()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Bad Precision: " + str(evaluation_result.get_bad_precision()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good Recall: " + str(evaluation_result.get_good_recall()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Bad Recall: " + str(evaluation_result.get_bad_recall()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        f.write("Good refactorings number: " + str(evaluation_result.numberOfGood) + "\n")
        f.write("Bad refactorings number: " + str(evaluation_result.numberOfBad) + "\n")
        f.write("Found good refactorings number: " + str(evaluation_result.numberOfFoundGood) + "\n")
        f.write("Found bad refactorings number: " + str(evaluation_result.numberOfFoundBad) + "\n")
        f.write("Found others refactorings number: " +
                str(evaluation_result.numberOfFoundOthers) + "\n")


def main():
    dataset_root_path = "/home/mikhail/Documents/Development/UtilitiesEvaluation/Dataset/projects/"
    evaluation_result_to_save = "/home/mikhail/Documents/Development/UtilitiesEvaluation/Dataset/JDeodorant_result"
    write_result_to_file(evaluation_result_to_save, Evaluator.evaluate(dataset_root_path))

if __name__ == "__main__":
    main()
