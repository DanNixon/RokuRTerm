from setuptools import setup

setup(
    name='rokurterm',
    version='0.1.0',
    entry_points = {
        'console_scripts': ['roku=rokurterm:main'],
    },
    description='Basic command line remote control for Roku based players.',
    classifiers=[
	'License :: OSI Approved :: Apache Software License',
	'Natural Language :: English',
	'Programming Language :: Python :: 2.7',
    ],
    keywords='roku remote',
    url='http://github.com/DanNixon/RokuRTerm',
    author='Dan Nixon',
    author_email='dan@dan-nixon.com',
    license='Apache',
    packages=['rokurterm'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False)
