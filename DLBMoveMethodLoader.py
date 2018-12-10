import json
from typing import List

from MoveMethodRefactoring import MoveMethodRefactoring


class DLBMoveMethodLoader:
    source_class_qualified_name_field = "source_class_qualified_name"
    target_class_qualified_name_field = "target_class_qualified_name"
    method_name_field = "method_name"
    params_classes_field = "params_classes"

    @staticmethod
    def load(file_path: str) -> List[MoveMethodRefactoring]:
        with open(file_path) as f:
            loaded_json = json.loads(f.read())
            move_method_refactorings = []
            for json_move_method_refactoring in loaded_json:
                source_class_qualified_name = \
                    json_move_method_refactoring[DLBMoveMethodLoader.source_class_qualified_name_field]
                target_class_qualified_name = \
                    json_move_method_refactoring[DLBMoveMethodLoader.target_class_qualified_name_field]
                method_name = json_move_method_refactoring[DLBMoveMethodLoader.method_name_field]
                params_classes = json_move_method_refactoring[DLBMoveMethodLoader.params_classes_field]
                move_method_refactorings.append(
                    MoveMethodRefactoring(
                        target_class_qualified_name, source_class_qualified_name, method_name, params_classes
                    )
                )
            return move_method_refactorings
