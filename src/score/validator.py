"""Validate HLA scoring data.

This module provides a way to make sure the data you've obtained from the HLA curation
interface is valid for scoring.
"""

import json
from typing import List, Literal, Union

from pydantic import BaseModel

from score.steps import steps


class ValidStep1Data(BaseModel):
    """Model the first step of the scoring process."""

    a_allele_or_haplotype: Literal[*steps.get_option_names("1A")]  # type: ignore
    b_allele_resolution: Literal[*steps.get_option_names("1B")]  # type: ignore
    c_zygosity: Literal[*steps.get_option_names("1C")]  # type: ignore
    d_phase: Literal[*steps.get_option_names("1D")]  # type: ignore


class ValidStep2Data(BaseModel):
    """Model the second step of the scoring process."""

    typing_method: Literal[*steps.get_option_names("2")]  # type: ignore


class ValidStep3Data(BaseModel):
    # pylint: disable=invalid-name
    # pylint: disable=line-too-long
    """Model the third step of the scoring process."""

    a_statistics_p_value: Literal[*steps.get_option_names("3A")]  # type: ignore

    # The type here looks scary. It means: "Either a single option name for
    # step 3B or a list of option names for step 3B that contains a subset of
    # the option names." (A subset can be the full set or a strict subset.)
    # For example:
    #     steps.get_option_names("3B") = ["apple", "banana", "cherry"]
    #     b_multiple_testing_correction = "apple"  # valid
    #     b_multiple_testing_correction = ["apple", "banana", "cherry"]  # valid
    #     b_multiple_testing_correction = ["apple", "cherry"]  # valid
    #     b_multiple_testing_correction = ["apple", "date"]  # invalid
    type SingleOrSubset3B = Union[Literal[*steps.get_option_names("3B")], List[Literal[*steps.get_option_names("3B")]]]  # type: ignore
    b_multiple_testing_correction: SingleOrSubset3B
    type SingleOrSubset3C = Union[Literal[*steps.get_option_names("3C")], List[Literal[*steps.get_option_names("3C")]]]  # type: ignore
    c_statistics_effect_size: SingleOrSubset3C


class ValidStep4Data(BaseModel):
    """Model the fourth step of the scoring process."""

    cohort_size: Literal[*steps.get_option_names("4")]  # type: ignore


class ValidStep5Data(BaseModel):
    """Model the fifth step of the scoring process."""

    additional_phenotypes: Literal[*steps.get_option_names("5")]  # type: ignore


class ValidScoreData(BaseModel):
    """Model a classification score."""

    step_1: ValidStep1Data
    step_2: ValidStep2Data
    step_3: ValidStep3Data
    step_4: ValidStep4Data
    step_5: ValidStep5Data


if __name__ == "__main__":
    score_data_json_schema = ValidScoreData.model_json_schema()
    print(json.dumps(score_data_json_schema, indent=2))
