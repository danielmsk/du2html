#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    # 'prettytable'
    # 'rich',
    # 'pyreadr',
    # 'prettytable',
    # 'pandas',
    # 'numpy',
    # 'pytabix'
]

tests_require = [
    # 'nose',
    # 'mock'
]

extras_require = {
    'docs': []
}

setup(name='du2html',
    version='0.0.6',
    url='https://github.com/danielmsk/du2html',
    license='MIT',
    author='Daniel Minseok Kwon',
    author_email='daniel.minseok.kwon@gmail.com',
    description='',
    download_url='',
    keywords=['linux', 'disk usage'],
    classifiers=[
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    # packages=find_packages(exclude=['tests']),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=['nose>=1.0'],
    test_suite='nose.collector',
    package_data={
        'du2html': ['templates/*'],
    },
    entry_points={
        'console_scripts': [
            'du2html=du2html:cli',
        ]
    })
