import sys
from setuptools import setup, find_packages

setup(name='Sample',
      version='1.0.0',  # @UndefinedVariable
      description='Sample python module for package demo',
      url='https://github.com/ManivannanPeriathambi/PythonPackage.git',
      author='Manivannan Periathambi',
      author_email='manivannan.periathambi@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['docs','tests*']),
      zip_safe=True,
	  datafile=None)