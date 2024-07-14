from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_name) -> List[str]:
    '''
    This function is to get all the package requirements to be installed
    '''
    with open(file_name) as file_obj:
        requirements = file_obj.readlines()
    requirements=[req.replace('\n', '') for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ml-project',
    version='0.0.1',
    author='divyarj',
    author_email='divyapriya074@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)