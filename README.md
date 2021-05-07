# {{cookiecutter.project_name}}

## Installation

## Usage
This pip package template follows the directions outlined here: https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/#creating-a-python-package

To make a package from this repository use the following commands
```sh
git clone https://github.com/roostercoopllc/pip-project-templates.git
pip install -r pip-project-templates/requirements.txt
cookiecutter ./pip-project-templates
# Input responses to fill out template
## project_name [default]: _
## ...
```

#### Create Source Distribution
Check if your package is able to be uploaded

```sh
python setup.py check
```

Creat Distribution
```sh
python setup.py sdist
```

Upload to private repository
```sh
twine upload --repository-url <url> dist/<project_name>-0.1.0.tar.gz
```

#### Create Wheel Distribution

#### Testing and publishing PyPI

## Notes