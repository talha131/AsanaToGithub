from setuptools import setup, find_packages
from asana_to_github import __version__ as version

install_requires = [
        'PyGithub==1.9.1',
        'asana==0.0.1',
        'python-dateutil==1.5',
        ]

dependency_links = [
        'https://github.com/talha131/asana/tarball/master#egg=asana-0.0.1',
    ]

name = 'AsanaToGithub'

setup(
    name = name,
    version = version,
    author = 'Talha Mansoor',
    author_email = 'talha131@gmail.com',
    description = 'Simple script to copy items from Asana to Github issues',
    license = 'Apache License, (2.0)',
    keywords = 'asana github issues issue tracker',
    url = 'https://github.com/talha131/asana-to-github',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Stable',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Asana',
        'Topic :: Github Issues',
        'Environment :: Console',
        'Intended Audience :: Developers',
        ],
    install_requires=install_requires,
    dependency_links = dependency_links,
    entry_points = {
        'console_scripts': ['asanatogithub = asana_to_github.asana_to_github:main']
        }
    )
