from setuptools import setup, find_packages

setup(
    name='jira',
    version='0.1',
    packages=find_packages(),
    py_modules=['get_projects'],
    entry_points={
        'console_scripts': [
            'jira=get_projects:main',
        ],
    },
    install_requires=[
        'requests',
        'tabulate',
    ],
)
