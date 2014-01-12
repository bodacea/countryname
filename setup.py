from distutils.core import setup

setup(
    name='CountryName',
    version='0.1.0',
    author='Sara-Jayne Terp',
    author_email='sarajterp@gmail.com',
    packages=['countryname'],
    url='http://pypi.python.org/pypi/countryname/',
    license='LICENSE.txt',
    description='Cleaners for country name standards',
    long_description=open('README.txt').read(),
    install_requires=[
        "Python >= 2.7",
    ],
)
