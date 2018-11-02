from typing import List
import json

from MoveMethodRefactoring import MoveMethodRefactoring


class JBMoveMethodLoader:
    source_class_qualified_name_field = "sourceClassQualifiedName"
    target_class_qualified_name_field = "targetClassQualifiedName"
    method_name_field = "methodName"
    params_classes_field = "paramsClasses"

    @staticmethod
    def load(file_path: str, leave_params_quilified: bool) -> List[MoveMethodRefactoring]:
        with open(file_path) as f:
            loaded_json = json.loads(f.read())
            move_method_refactorings = []
            for json_move_method_refactoring in loaded_json:
                source_class_qualified_name = \
                    json_move_method_refactoring[JBMoveMethodLoader.source_class_qualified_name_field]
                target_class_qualified_name = \
                    json_move_method_refactoring[JBMoveMethodLoader.target_class_qualified_name_field]
                method_name = json_move_method_refactoring[JBMoveMethodLoader.method_name_field]
                params_classes = json_move_method_refactoring[JBMoveMethodLoader.params_classes_field]
                if not leave_params_quilified:
                    params_classes = list(map(lambda el: el.split(".")[len(el.split(".")) - 1], params_classes))
                move_method_refactorings.append(
                    MoveMethodRefactoring(
                        target_class_qualified_name, source_class_qualified_name, method_name, params_classes
                    )
                )
            return move_method_refactorings
