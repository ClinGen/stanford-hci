"""Test the score package."""

import unittest

from score.calculator import (
    calculate_step_1_points,
    calculate_step_2_points,
    calculate_step_3_points,
)
from score.validator import ValidStep1Data, ValidStep2Data, ValidStep3Data


class TestCalculator(unittest.TestCase):
    # pylint: disable=too-many-instance-attributes
    """Make sure the calculator works."""

    def setUp(self):
        """Set up test data for the unit tests."""
        self.step_1_data = {
            "a_allele_or_haplotype": "Allele",
            "b_allele_resolution": "2-field",
            "c_zygosity": "Biallelic (homozygous)",
            "d_phase": "Phase confirmed",
        }
        self.step_1_expected_score = 0 + 1 + 0.5 + 0.5
        self.step_2_data = {"typing_method": "Low Resolution Typing"}
        self.step_2_expected_score = 3
        self.step_3_data_singles = {
            "a_statistics_p_value": "GWAS <5x10e-8, Non-GWAS <0.01",
            "b_multiple_testing_correction": "Overall correction for multiple testing",
            "c_statistics_effect_size": "OR/RR: ≥2 or ≤0.5, Beta: ≥0.5 or ≤-0.5",
        }
        self.step_3_singles_expected_score = 1 + 1 + 1
        self.step_3_data_lists = {
            "a_statistics_p_value": "GWAS <1x10e-14, Non-GWAS <0.0001",
            "b_multiple_testing_correction": [
                "Overall correction for multiple testing",
                "2-step p-value correction",
            ],
            "c_statistics_effect_size": [
                "OR/RR: ≥2 or ≤0.5, Beta: ≥0.5 or ≤-0.5",
                "CI does not cross 1 (OR/RR) or 0 (beta)",
            ],
        }
        self.step_3_lists_expected_score = 2 + (1 + 2) + (1 + 1)

    def test_calculate_step_1(self):
        """Make sure we can calculate the points for step 1."""
        valid_step_1_data = ValidStep1Data(**self.step_1_data)
        self.assertEqual(
            self.step_1_expected_score, calculate_step_1_points(valid_step_1_data)
        )

    def test_calculate_step_2(self):
        """Make sure we can calculate the points for step 2."""
        valid_step_2_data = ValidStep2Data(**self.step_2_data)
        self.assertEqual(
            self.step_2_expected_score, calculate_step_2_points(valid_step_2_data)
        )

    def test_calculate_step_3_singles(self):
        """Make sure we can calculate the points for step 3 with single options."""
        valid_step_3_data = ValidStep3Data(**self.step_3_data_singles)
        self.assertEqual(
            self.step_3_singles_expected_score,
            calculate_step_3_points(valid_step_3_data),
        )

    def test_calculate_step_3_lists(self):
        """Make sure we can calculate the points for step 3 with multiple options."""
        valid_step_3_data = ValidStep3Data(**self.step_3_data_lists)
        self.assertEqual(
            self.step_3_lists_expected_score, calculate_step_3_points(valid_step_3_data)
        )


if __name__ == "__main__":
    unittest.main()
