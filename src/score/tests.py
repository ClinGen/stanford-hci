"""Test the score package."""

import unittest

from score.calculator import calculate_step_1_points, calculate_step_2_points
from score.validator import ValidStep1Data, ValidStep2Data


class TestCalculator(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
