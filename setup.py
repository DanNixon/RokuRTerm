from setuptools import setup, find_packages

setup(
    name='rokurterm',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['roku=rokurterm.main:main'],
    },
    description='Basic command line remote control for Roku based players.',
    url='http://github.com/DanNixon/RokuRTerm',
    author='Dan Nixon',
    author_email='dan@dan-nixon.com',
    license='Apache',
    install_requires=[
        'requests'
    ]
)
