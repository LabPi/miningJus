from setuptools import find_packages
from setuptools import setup

setup (
       name='crawl',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=[
        'lxml',
       ],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='Joao Antonio Gardin Vieira',
       author_email='gardin1992@gmail.com',

       #summary = 'Just another Python package for the cheese shop',
       url='https://github.com/gardin1992/miningJus',
       license='GPL',
       long_description='Web Crawler para extracao de dados do dominio http://dados.gov.br'  
       )