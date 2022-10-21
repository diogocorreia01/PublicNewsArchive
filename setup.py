from codecs import open
from os.path import join, abspath, dirname
from setuptools import setup, find_packages
import os

here = abspath(dirname(__file__))

with open(join(here, 'README.md'), encoding='utf-8') as buff:
    long_description = buff.read()

setup(
    name="PublicNewsArchive",
    version="1.0",
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
    install_requires=[
        'beautifulsoup4==4.11.1',
        'bs4==0.0.1',
        'date-guesser-rc @ git+https://github.com/rncampos/date_guesser@4007399df72fbfba18ab1c9852153cd80eb616e9',
        'geopy==2.2.0',
        'gmplot==1.4.1',
        'matplotlib==3.5.0',
        'numpy',
        'pandas',
        'pt-core-news-lg @ https://github.com/explosion/spacy-models/releases/download/pt_core_news_lg-3.3.0/pt_core_news_lg-3.3.0-py3-none-any.whl',
        'requests==2.28.1',
        'spacy==3.3.0',
        'urllib3==1.26.12',
        'wordcloud==1.8.2.2',
        'yake @ git+https://github.com/LIAAD/yake@6a37efc67912195aebed562cd943bca8acc48f64'
    ]
)