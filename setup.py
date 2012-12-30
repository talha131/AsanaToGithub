from setuptools import setup, find_packages
from asana_to_github import __version__ as version

install_requires = [
    'git+git://github.com/jacquev6/PyGithub.git',
    'git+git://github.com/talha131/asana.git',
    ]

name = 'Asana to Github'

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
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Asana',
        'Topic :: Github Issues',
        'Environment :: Console',
        'Intended Audience :: Developers',
        ],
    install_requires=install_requires,
    )
