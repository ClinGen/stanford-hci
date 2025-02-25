# HLA Curation Interface (HCI)

## Getting Started

- Install Python 3.13.
- Install Pipenv.
- Clone the repo.
- Make a directory for your virtual environment in the root of this repo:
  `mkdir .venv`.
- Install Python dependencies: `pipenv sync --dev`.
- Install other dependencies:
    - [ShellCheck](https://www.shellcheck.net/)
    - [sh](https://github.com/mvdan/sh)
    - [hadolint](https://github.com/hadolint/hadolint)
    - [yamlfmt](https://github.com/google/yamlfmt)
    - [Docker](https://www.docker.com/): `brew install docker`
    - [Docker buildx](https://www.docker.com/): `brew install docker-buildx`
    - [Colima](https://github.com/abiosoft/colima): `brew install colima`
    - [Terraform](https://www.terraform.io/)
- Start Colima: `colima start`.