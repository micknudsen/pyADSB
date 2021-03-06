from setuptools import setup, find_packages

setup(

    name='pyadsb',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    test_suite='tests',

    python_requires='>=3.6',

    author='Michael Knudsen',
    author_email='micknudsen@gmail.com',
    license='MIT'

)
