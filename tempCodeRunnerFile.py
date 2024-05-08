from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list:
    '''
    This function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip newline characters from each line

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Sachin',
    author_email='sachinghogare1762@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
