"""Provide models and data for the steps in scoring an HLA classification.

This is the single source of truth for the data related to the HLA scoring framework
steps.
"""

from typing import Dict, List

from pydantic import BaseModel


class Option(BaseModel):
    """Model an option for a scoring step."""

    option_name: str
    option_points: float


class Step(BaseModel):
    """Model a scoring step."""

    step_number: str
    step_name: str
    step_options: List[Option]


class Steps(BaseModel):
    """Model the steps in scoring an HLA classification."""

    hla_framework_scoring_steps: List[Step]

    def get_option_names(self, step_number: str) -> List[str]:
        """Given a step number, return the associated option names."""
        option_names = []
        for step in self.hla_framework_scoring_steps:
            if step.step_number == step_number:
                for option in step.step_options:
                    option_names.append(option.option_name)
        return option_names

    def get_option_to_points_map(self, step_number: str) -> Dict[str, float]:
        """Given a step number, return the associated options mapped to their points."""
        options_to_points_map = {}
        for step in self.hla_framework_scoring_steps:
            if step.step_number == step_number:
                for option in step.step_options:
                    options_to_points_map[option.option_name] = option.option_points
        return options_to_points_map


# fmt: off
_steps_data = {
    "hla_framework_scoring_steps": [
        {
            "step_number": "1A",
            "step_name": "Allele or Haplotype",
            "step_options": [
                {
                    "option_name": "Allele",
                    "option_points": 0
                },
                {
                    "option_name": "Haplotype",
                    "option_points": 2
                },
            ],
        },
        {
            "step_number": "1B",
            "step_name": "Allele Resolution",
            "step_options": [
                {
                    "option_name": "1-field",
                    "option_points": 0
                },
                {
                    "option_name": "2-field",
                    "option_points": 1
                },
                {
                    "option_name": "3-field, G-group, P-group",
                    "option_points": 2
                },
                {
                    "option_name": "4-field",
                    "option_points": 3
                },
            ],
        },
        {
            "step_number": "1C",
            "step_name": "Zygosity",
            "step_options": [
                {
                    "option_name": "Monoallelic (heterozygous)",
                    "option_points": 0
                },
                {
                    "option_name": "Biallelic (homozygous)",
                    "option_points": 0.5
                },
            ],
        },
        {
            "step_number": "1D",
            "step_name": "Phase",
            "step_options": [
                {
                    "option_name": "Phase not confirmed",
                    "option_points": 0
                },
                {
                    "option_name": "Phase confirmed",
                    "option_points": 0.5
                },
            ],
        },
        {
            "step_number": "2",
            "step_name": "Typing Method",
            "step_options": [
                {
                    "option_name": "Tag SNPs or Microarrays",
                    "option_points": 0
                },
                {
                    "option_name": "Serological",
                    "option_points": 1
                },
                {
                    "option_name": "Imputation",
                    "option_points": 2
                },
                {
                    "option_name": "Low Resolution Typing",
                    "option_points": 3
                },
                {
                    "option_name": "High Resolution Typing",
                    "option_points": 3
                },
                {
                    "option_name": "Whole Exome Sequencing",
                    "option_points": 3
                },
                {
                    "option_name": "Sanger Sequencing-Based Typing",
                    "option_points": 4
                },
                {
                    "option_name": "Whole Gene Sequencing",
                    "option_points": 4
                },
                {
                    "option_name": "Whole Genome Sequencing and/or Panel-Based NGS (>50x coverage)",
                    "option_points": 5
                },
            ],
        },
        {
            "step_number": "3A",
            "step_name": "Statistics (p-value)",
            "step_options": [
                {
                    "option_name": "GWAS >=1x10e-5, Non-GWAS >=0.05",
                    "option_points": 0
                },
                {
                    "option_name": "GWAS <1x10e-5, Non-GWAS <0.05",
                    "option_points": 0.5
                },
                {
                    "option_name": "GWAS <5x10e-8, Non-GWAS <0.01",
                    "option_points": 1
                },
                {
                    "option_name": "GWAS <1x10e-11, Non-GWAS <0.0005",
                    "option_points": 1.5
                },
                {
                    "option_name": "GWAS <1x10e-14, Non-GWAS <0.0001",
                    "option_points": 2
                },
            ],
        },
        {
            "step_number": "3B",
            "step_name": "Multiple Testing Correction",
            "step_options": [
                {
                    "option_name": "Overall correction for multiple testing",
                    "option_points": 1
                },
                {
                    "option_name": "2-step p-value correction",
                    "option_points": 2
                },
            ],
        },
        {
            "step_number": "3C",
            "step_name": "Statistics (Effect Size)",
            "step_options": [
                {
                    "option_name": "OR/RR: ≥2 or ≤0.5, Beta: ≥0.5 or ≤-0.5",
                    "option_points": 1
                },
                {
                    "option_name": "CI does not cross 1 (OR/RR) or 0 (beta)",
                    "option_points": 1
                },
            ],
        },
        {
            "step_number": "4",
            "step_name": "Cohort Size",
            "step_options": [
                {
                    "option_name": "GWAS <1,000, Non-GWAS <50",
                    "option_points": 0
                },
                {
                    "option_name": "GWAS 1,000-2,499, Non-GWAS 50-99",
                    "option_points": 1
                },
                {
                    "option_name": "GWAS 2,500-4,999, Non-GWAS 100-249",
                    "option_points": 2
                },
                {
                    "option_name": "GWAS 5,000-9,999, Non-GWAS 250-499",
                    "option_points": 3
                },
                {
                    "option_name": "GWAS >=10,000, Non-GWAS >=500",
                    "option_points": 4
                },
            ],
        },
        {
            "step_number": "5",
            "step_name": "Additional Phenotypes",
            "step_options": [
                {
                    "option_name": "specific disease-related phenotype",
                    "option_points": 2
                },
                {
                    "option_name": "only disease tested",
                    "option_points": 0
                },
            ],
        },
        {
            "step_number": "6A",
            "step_name": "Weighing Association",
            "step_options": [
                {
                    "option_name": "significant association with disease",
                    "option_points": 1
                },
                {
                    "option_name": "no significant association with disease",
                    "option_points": 0
                },
            ],
        },
        {
            "step_number": "6B",
            "step_name": "Low Field Resolution",
            "step_options": [
                {
                    "option_name": "1-field resolution (from Step 1B)",
                    "option_points": 0.5
                },
                {
                    "option_name": ">1-field resolution",
                    "option_points": 1
                },
            ],
        },
    ]
}
# fmt: on

steps = Steps(**_steps_data)  # type: ignore

if __name__ == "__main__":
    print(steps.model_dump_json(indent=2))
