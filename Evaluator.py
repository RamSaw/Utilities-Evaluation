import getopt
import os
import sys

from EvaluationResult import EvaluationResult
from ProjectEvaluator import JDeodorantProjectEvaluator


class Evaluator:
    @staticmethod
    def evaluate(dataset_root_path: str, tool_name: str) -> EvaluationResult:
        evaluation_result = EvaluationResult()
        with open(os.path.join(dataset_root_path, "evaluationResults",
                               tool_name + "_project_evaluation_results"), "w") as f:
            dataset_root_path = os.path.join(dataset_root_path, "projects")
            for project in os.listdir(dataset_root_path):
                try:
                    project_result = JDeodorantProjectEvaluator.evaluate(os.path.join(dataset_root_path, project),
                                                                         tool_name)
                    if project_result is None:
                        print("No file with found refactorings for " + project + " project")
                        continue
                    f.write("===========" + project + "===========" + "\n")
                    f.write("Good refactorings number: " + str(project_result.get_good_refactorings_number()) + "\n")
                    f.write("Bad refactorings number: " + str(project_result.get_bad_refactorings_number()) + "\n")
                    f.write("Found good refactorings number: " + str(
                        project_result.get_found_good_refactorings_number()) + "\n")
                    f.write(
                        "Found bad refactorings number: " + str(
                            project_result.get_found_bad_refactorings_number()) + "\n")
                    f.write("Found others refactorings number: " +
                            str(project_result.get_found_others_refactorings_number()) + "\n")
                    # without target
                    f.write("Found good refactorings without target number: " + str(
                        project_result.get_found_good_refactorings_without_target_number()) + "\n")
                    f.write(
                        "Found bad refactorings without target number: " + str(
                            project_result.get_found_bad_refactorings_without_target_number()) + "\n")
                    f.write("Found others refactorings without target number: " +
                            str(project_result.get_found_others_refactorings_without_target_number()) + "\n")
                    f.write("\n\n")
                    evaluation_result.add_result(project_result)
                except Exception:
                    print("Error on project: " + project)
                    raise
            return evaluation_result


def write_result_to_file(filename: str, evaluation_result: EvaluationResult):
    with open(filename, "w") as f:
        string_to_write = "Good Precision: " + str(evaluation_result.get_good_precision()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good Recall: " + str(evaluation_result.get_good_recall()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good F-measure: " + str(evaluation_result.get_good_f_measure()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Bad Precision: " + str(evaluation_result.get_bad_precision()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Bad Recall: " + str(evaluation_result.get_bad_recall()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Bad F-measure: " + str(evaluation_result.get_bad_f_measure()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good Precision Without Target: " + \
                          str(evaluation_result.get_good_precision_without_target()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good Recall Without Target: " + \
                          str(evaluation_result.get_good_recall_without_target()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good F-measure Without Target: " + \
                          str(evaluation_result.get_good_f_measure_without_target()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Bad Precision Without Target: " + \
                          str(evaluation_result.get_bad_precision_without_target()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Bad Recall Without Target: " + \
                          str(evaluation_result.get_bad_recall_without_target()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Bad F-measure Without Target: " + \
                          str(evaluation_result.get_bad_f_measure_without_target()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good Precision Only Good: " + str(evaluation_result.get_good_precision_only_good()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good Recall Only Good: " + str(evaluation_result.get_good_recall_only_good()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good F-measure Only Good: " + \
                          str(evaluation_result.get_good_f_measure_only_good()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good Precision Without Target Only Good: " + \
                          str(evaluation_result.get_good_precision_without_target_only_good()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good Recall Without Target Only Good: " + \
                          str(evaluation_result.get_good_recall_without_target_only_good()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        string_to_write = "Good F-measure Without Target Only Good: " + \
                          str(evaluation_result.get_good_f_measure_without_target_only_good()) + "\n"
        print(string_to_write)
        f.write(string_to_write)

        f.write("Good refactorings number: " + str(evaluation_result.numberOfGood) + "\n")
        f.write("Bad refactorings number: " + str(evaluation_result.numberOfBad) + "\n")
        f.write("Found good refactorings number: " + str(evaluation_result.numberOfFoundGood) + "\n")
        f.write("Found bad refactorings number: " + str(evaluation_result.numberOfFoundBad) + "\n")
        f.write("Found others refactorings number: " +
                str(evaluation_result.numberOfFoundOthers) + "\n")
        # without target
        f.write("Found good refactorings without target number: " +
                str(evaluation_result.numberOfFoundGoodWithoutTarget) + "\n")
        f.write("Found bad refactorings without target number: " +
                str(evaluation_result.numberOfFoundBadWithoutTarget) + "\n")
        f.write("Found others refactorings without target number: " +
                str(evaluation_result.numberOfFoundOthersWithoutTarget) + "\n")
        # only good
        f.write("Found others refactorings number only good: " +
                str(evaluation_result.numberOfFoundOthersOnlyGood) + "\n")
        f.write("Found others refactorings without target only good number: " +
                str(evaluation_result.numberOfFoundOthersWithoutTargetOnlyGood) + "\n")


def print_help():
    print('Evaluator.py -d <path_to_dataset> -u <utility: "JDeodorant" or "JMove">')


def main(argv):
    dataset_root_path = None
    tool = None
    try:
        opts, args = getopt.getopt(argv, "hd:t:", ["dataset=", "tool="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-d", "--dataset"):
            dataset_root_path = arg
        elif opt in ("-t", "--tool"):
            tool = arg
    if tool is None or dataset_root_path is None:
        print("Param is missing, try again\n")
        print_help()
        sys.exit(2)
    path_to_save_evaluation_result = os.path.join(dataset_root_path, "evaluationResults", tool + "_result_ALL")
    write_result_to_file(path_to_save_evaluation_result, Evaluator.evaluate(dataset_root_path, tool))


if __name__ == "__main__":
    main(sys.argv[1:])
