from setuptools import setup, find_packages

setup(
    name='toxsux',
    version='2019.2b2',
	packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://gitlab.com/pypy/toxsux',
    license='MIT',
    author='Laurențiu Andronache',
    author_email='laurentiu.andronache@trailung.ro',
    description='Crap testing.'
)
