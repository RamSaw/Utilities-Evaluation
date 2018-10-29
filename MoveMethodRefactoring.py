from typing import List


class MoveMethodRefactoring:
    def __init__(self, target_class_qualified_name: str, source_class_qualified_name: str,
                 method_name: str, params_classes: List[str]) -> None:
        super().__init__()
        self.target_class_qualified_name = target_class_qualified_name
        self.source_class_qualified_name = source_class_qualified_name
        self.method_name = method_name
        self.params_classes = params_classes
        # self.additional_data = additional_data
