"""Score an HLA classification.

Input:
    HLA score data.
Output:
    A numeric score for the HLA classification.
"""

import logging

from pydantic import ValidationError

from score.steps import steps
from score.validator import ValidScoreData, ValidStep1Data

logger = logging.getLogger(__name__)


class CalculatorException(Exception):
    """Define an exception for the calculator module."""


def _get_points(option: str, step_number: str) -> float:
    """Return points for the given step/option combination."""
    options_to_points_map = steps.get_option_to_points_map(step_number)
    if option in options_to_points_map:
        return options_to_points_map[option]
    raise CalculatorException(
        f"Option name {option} not found in canonical list of option names"
    )


def calculate_step_1(data: ValidStep1Data) -> float:
    """Calculate score for step 1."""
    step_1_points = 0.0
    step_1_points += _get_points(data.a_allele_or_haplotype, "1A")
    step_1_points += _get_points(data.b_allele_resolution, "1B")
    step_1_points += _get_points(data.c_zygosity, "1C")
    step_1_points += _get_points(data.d_phase, "1D")
    return step_1_points


def calculate(data: dict) -> float:
    """Calculate a score for an HLA classification."""
    score = 0.0

    try:
        data = ValidScoreData(**data)  # type: ignore
    except ValidationError as err:
        logger.error("Unable to validate score")
        logger.error(err.errors())

    score += calculate_step_1(data.step_1)  # type: ignore

    return score
