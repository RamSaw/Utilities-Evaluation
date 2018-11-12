import os
from typing import Optional

from JBMoveMethodLoader import JBMoveMethodLoader
from JDeodorantMoveMethodLoader import JDeodorantMoveMethodLoader
from ProjectEvaluationResult import ProjectEvaluationResult


class JDeodorantProjectEvaluator:
    good_refactorings_name = "good"
    bad_refactorings_name = "bad"
    project_folder = "project"

    @staticmethod
    def evaluate(project_path: str, tool_name: str) -> Optional[ProjectEvaluationResult]:
        project_name = os.path.basename(project_path)
        good_refactorings_path = os.path.join(project_path, JDeodorantProjectEvaluator.good_refactorings_name)
        bad_refactorings_path = os.path.join(project_path, JDeodorantProjectEvaluator.bad_refactorings_name)
        found_refactorings_path = os.path.join(project_path, tool_name
                                               + "_" + project_name)
        if not os.path.isfile(found_refactorings_path):
            return None
        good_refactorings = JBMoveMethodLoader.load(good_refactorings_path, tool_name != "JMove")
        bad_refactorings = JBMoveMethodLoader.load(bad_refactorings_path, tool_name != "JMove")
        found_refactorings = JDeodorantMoveMethodLoader.load(found_refactorings_path)
        return ProjectEvaluationResult(good_refactorings, bad_refactorings, found_refactorings, project_name)
