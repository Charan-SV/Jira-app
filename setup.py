# setup.py
from setuptools import setup, find_packages

setup(
    name='jira',
    version='0.1',
    packages=find_packages(),
    py_modules=['main', 'jira_functions'],
    entry_points={
        'console_scripts': [
            'jira=main:main',
        ],
    },
    install_requires=[
        'requests',
        'tabulate',
    ],
)
