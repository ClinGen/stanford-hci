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
    ValidStep4Data,
    ValidStep5Data,
    ValidStep6Data,
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

    :param option_or_options: A single option or a list of options.
    :param step_number: The step number we're interested in getting points for, e.g. "1A".
    :raises CalculatorException: If `option_or_options` is the wrong type.
    :returns: The points for the given `option_or_options`.
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
    """Calculate points for step 3."""
    step_3_points = 0.0
    step_3_points += _get_points(data.a_statistics_p_value, "3A")
    step_3_points += _get_points(data.b_multiple_testing_correction, "3B")
    step_3_points += _get_points(data.c_statistics_effect_size, "3C")
    return step_3_points


def calculate_step_4_points(data: ValidStep4Data) -> float:
    """Calculate points for step 4."""
    return _get_points(data.cohort_size, "4")


def calculate_step_5_points(data: ValidStep5Data) -> float:
    """Calculate points for step 5."""
    return _get_points(data.additional_phenotypes, "5")


def calculate_step_6_points(data: ValidStep6Data) -> float:
    """Calculate points for step 6."""
    factor_a = _get_points(data.a_weighing_association, "6A")
    factor_b = _get_points(data.b_low_field_resolution, "6B")
    return factor_a * factor_b


def calculate(data: dict) -> float:
    """Calculate a score for an HLA classification.

    :raises ValidationError: Couldn't validate data.
    :raises CalculatorException: Something wrong with option(s).
    :returns: The score for an HLA classification.
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
        score += calculate_step_4_points(data.step_4)  # type: ignore
        score += calculate_step_5_points(data.step_4)  # type: ignore
        score *= calculate_step_6_points(data.step_6)  # type: ignore
    except CalculatorException as err:
        logger.error("Unable to calculate score")
        logger.error(err)

    return score
