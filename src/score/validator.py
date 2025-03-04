"""Validate HLA scoring data."""

from typing import Literal

from pydantic import BaseModel

from score.steps import steps


class ValidStep1Data(BaseModel):
    """Model the first step of the scoring process."""

    a_allele_or_haplotype: Literal[*steps.get_option_names("1A")]  # type: ignore
    b_allele_resolution: Literal[*steps.get_option_names("1B")]  # type: ignore
    c_zygosity: Literal[*steps.get_option_names("1C")]  # type: ignore
    d_phase: Literal[*steps.get_option_names("1D")]  # type: ignore


class ValidScoreData(BaseModel):
    """Model a classification score."""

    step_1: ValidStep1Data
