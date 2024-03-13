from setuptools import find_packages,setup
from typing import List
REQUIREMENT_FILE_NAME = 'requirements.txt'
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    pass
    with open(REQUIREMENT_FILE_NAME) as f:
        requirement_list = f.readlines()
        requirement_list = [item.replace('\n','') for item in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(
    name="sensor",
    version="0.0.1",
    author="rahel",
    author_email="rahelali13412@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)
