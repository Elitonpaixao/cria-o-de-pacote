from setuptools import setup, find_packages

setup(
    name='mini-banco',
    version='0.1',
    packages=find_packages(),
    description='Uma biblioteca simples de contas bancárias para iniciantes.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Eliton',
    author_email='elitonpaixao@hotmail.com',
    url='https://github.dev/Elitonpaixao/cria-o-de-pacote',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
