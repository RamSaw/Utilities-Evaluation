from typing import List

import re

from MoveMethodRefactoring import MoveMethodRefactoring


class JDeodorantMoveMethodLoader:
    @staticmethod
    def load(file_path: str) -> List[MoveMethodRefactoring]:
        with open(file_path) as f:
            move_method_refactorings = []
            for line in f:
                if not line.startswith("Move Method"):
                    continue
                results = re.split(r"\s+(?=[^()]*(?:\(|$))", line)
                source_results = results[2]
                source_class_qualified_name = JDeodorantMoveMethodLoader.get_source_class_qualified_name(source_results)
                target_class_qualified_name = results[3]
                method_name = JDeodorantMoveMethodLoader.get_method_name(source_results)
                params_classes = JDeodorantMoveMethodLoader.get_params_classes(source_results)
                additional_data = results[4]
                move_method_refactorings.append(
                    MoveMethodRefactoring(target_class_qualified_name, source_class_qualified_name,
                                          method_name, params_classes)
                )
            return move_method_refactorings

    @staticmethod
    def get_source_class_qualified_name(source_results: str) -> str:
        return source_results.split("::")[0]

    @staticmethod
    def get_method_name(source_results: str) -> str:
        return source_results.split("::")[1].split("(")[0]

    @staticmethod
    def get_params_classes(source_results: str) -> List[str]:
        result = source_results.split("(")[1].split(")")[0].split(", ")
        if len(result) == 1 and result[0] == "":
            result = []
        return result
