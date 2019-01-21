import os
import re
from typing import Optional

from DLBMoveMethodLoader import DLBMoveMethodLoader
from JBMoveMethodLoader import JBMoveMethodLoader
from JDeodorantMoveMethodLoader import JDeodorantMoveMethodLoader
from ProjectEvaluationResult import ProjectEvaluationResult


class JDeodorantProjectEvaluator:
    good_refactorings_name = "good"
    bad_refactorings_name = "bad"
    project_folder = "project"

    @staticmethod
    def evaluate(project_path: str, tools: str) -> Optional[ProjectEvaluationResult]:
        tools_operations = re.findall('[&|]', tools)
        tool_names = re.split('[&|]', tools)
        project_name = os.path.basename(project_path)
        good_refactorings_path = os.path.join(project_path, JDeodorantProjectEvaluator.good_refactorings_name)
        bad_refactorings_path = os.path.join(project_path, JDeodorantProjectEvaluator.bad_refactorings_name)
        if len(tool_names) > 1:
            found_refactorings = None
            good_refactorings = JBMoveMethodLoader.load(good_refactorings_path, False)
            bad_refactorings = JBMoveMethodLoader.load(bad_refactorings_path, False)
            for i in range(0, len(tool_names)):
                found_refactorings_path = os.path.join(project_path, tool_names[i]
                                                       + "_" + project_name)
                if not os.path.isfile(found_refactorings_path):
                    return None
                if i == 0:
                    found_refactorings = set(JDeodorantProjectEvaluator.get_found_refactorings(found_refactorings_path,
                                                                                               tool_names[i]))
                    for f_ref in found_refactorings:
                        f_ref.params_classes = list(map(lambda el: el.split(".")[len(el.split(".")) - 1],
                                                        f_ref.params_classes))
                else:
                    next_found = set(JDeodorantProjectEvaluator.get_found_refactorings(found_refactorings_path,
                                                                                       tool_names[i]))
                    for f_ref in next_found:
                        f_ref.params_classes = list(map(lambda el: el.split(".")[len(el.split(".")) - 1],
                                                        f_ref.params_classes))
                    if tools_operations[i - 1] == "&":
                        found_refactorings &= set(next_found)
                    else:
                        found_refactorings |= set(next_found)
                i += 1
            return ProjectEvaluationResult(good_refactorings, bad_refactorings, list(found_refactorings), project_name)
        else:
            found_refactorings_path = os.path.join(project_path, tools
                                                   + "_" + project_name)
            if not os.path.isfile(found_refactorings_path):
                return None
            good_refactorings = JBMoveMethodLoader.load(good_refactorings_path, tools != "JMove")
            bad_refactorings = JBMoveMethodLoader.load(bad_refactorings_path, tools != "JMove")
            found_refactorings = JDeodorantProjectEvaluator.get_found_refactorings(found_refactorings_path, tools)
            return ProjectEvaluationResult(good_refactorings, bad_refactorings, found_refactorings, project_name)

    @staticmethod
    def get_found_refactorings(found_refactorings_path, tool_name):
        return DLBMoveMethodLoader.load(found_refactorings_path) if tool_name == "DLB" \
            else JDeodorantMoveMethodLoader.load(found_refactorings_path)
