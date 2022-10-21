from codecs import open
from os.path import join, abspath, dirname
from setuptools import setup, find_packages
import os

requirementPath = 'requirements.txt'

if os.path.isfile(requirementPath):
    with open(requirementPath, encoding='utf-8') as f:
        install_requires = f.read().splitlines()
        print(install_requires)

here = abspath(dirname(__file__))

with open(join(here, 'README.md'), encoding='utf-8') as buff:
    long_description = buff.read()

setup(
    name="PublicNewsArchive",
    version="0.1",
    description="A module that allows you to get and analyze news in detail",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diogocorreia01/PublicNewsArchive.git",
    author="Diogo Correia"
           "Ricardo Campos",
    author_email="diogo.correia01@outlook.com",
    packages=find_packages(),
    license='LGPLv3',
    include_package_data=True,
    install_requires=install_requires
)