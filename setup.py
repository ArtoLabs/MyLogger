from setuptools import setup, find_packages

setup(
    python_requires='>=3.0',
    name='MyLogger',
    version='0.1',
    packages=['mylogger'],
    license='MIT',
    long_description=open('README.txt').read(),
    keywords='log logging logger',
    url='http://github.com/artolabs/mylogger',
    author='ArtoLabs',
    author_email='artopium@gmail.com',
    py_modules=['mylogger'],
    include_package_data=True,
    zip_safe=False
)


