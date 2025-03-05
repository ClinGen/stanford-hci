"""Score an HLA classification.

Input:
    HLA score data.
Output:
    A numeric score for the HLA classification.

This module contains the scoring logic.
"""

import logging
from typing import List

from pydantic import ValidationError

from score.steps import steps
from score.validator import (
    ValidScoreData,
    ValidStep1Data,
    ValidStep2Data,
    ValidStep3Data,
)

logger = logging.getLogger(__name__)


class CalculatorException(Exception):
    """Define an exception for the calculator module."""


def _get_points_for_single_option(option: str, step_number: str) -> float:
    """Return points for the given option/step combination."""
    options_to_points_map = steps.get_option_to_points_map(step_number)
    if option in options_to_points_map:
        return options_to_points_map[option]
    raise CalculatorException(
        f"Option name {option} not found in canonical list of option names"
    )


def _get_points_for_multiple_options(options: List[str], step_number: str) -> float:
    """Return points for the given options/step combination."""
    points = 0.0
    for option in options:
        if isinstance(option, str):
            points += _get_points_for_single_option(option, step_number)
        else:
            raise CalculatorException("Received non-string option")
    return points


def _get_points(option_or_options: str | List[str] | None, step_number: str) -> float:
    """Return points for the given option(s)/step combination.

    Args:
         option_or_options: A single option or a list of options.
         step_number: The step number we're interested in getting points for, e.g. "1A".
    """
    if isinstance(option_or_options, str):
        return _get_points_for_single_option(option_or_options, step_number)
    if isinstance(option_or_options, list):
        return _get_points_for_multiple_options(option_or_options, step_number)
    if option_or_options is None:
        return 0.0
    raise CalculatorException(
        "Argument `option_or_options` should be of type `str`, `List[str]`, or `None`"
    )


def calculate_step_1_points(data: ValidStep1Data) -> float:
    """Calculate points for step 1."""
    step_1_points = 0.0
    step_1_points += _get_points(data.a_allele_or_haplotype, "1A")
    step_1_points += _get_points(data.b_allele_resolution, "1B")
    step_1_points += _get_points(data.c_zygosity, "1C")
    step_1_points += _get_points(data.d_phase, "1D")
    return step_1_points


def calculate_step_2_points(data: ValidStep2Data) -> float:
    """Calculate points for step 2."""
    return _get_points(data.typing_method, "2")


def calculate_step_3_points(data: ValidStep3Data) -> float:
    """Calculate points for step 2."""
    step_3_points = 0.0
    step_3_points += _get_points(data.a_statistics_p_value, "3A")
    step_3_points += _get_points(data.b_multiple_testing_correction, "3B")
    step_3_points += _get_points(data.c_statistics_effect_size, "3C")
    return step_3_points


def calculate(data: dict) -> float:
    """Calculate a score for an HLA classification.

    Raises:
         ValidationError: Pydantic couldn't validate the data.
         CalculatorException: An option couldn't be found.
    """
    score = 0.0

    try:
        data = ValidScoreData(**data)  # type: ignore
    except ValidationError as err:
        logger.error("Unable to validate score")
        logger.error(err.errors())

    try:
        score += calculate_step_1_points(data.step_1)  # type: ignore
        score += calculate_step_2_points(data.step_2)  # type: ignore
        score += calculate_step_3_points(data.step_3)  # type: ignore
    except CalculatorException as err:
        logger.error("Unable to calculate score")
        logger.error(err)

    return score
