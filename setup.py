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
    long_description = """
    AsanaToGithub copies your tasks from an Asana project to your Github repository's issue tracker. It copies Asana task title, notes, comments and attachments to Github issues. It supports UTF-8 encoding.

    Asana task's title and note is created as Github issue. The comments and attachments of the task are added as a comment to the Github issue. AsanaToGithub supports linking the Asana task and Github issue together by means of adding links in the comments at both sites.

    Features
    --------
    #. You can copy incomplete and completed tasks.
    #. Tasks can be copied in batch or interactively. 
    #. You can copy Asana comments and attachments to the Github issue which can be disabled.
    #. A comment is added to Asana task which has link to the Github issue. This can be disabled.
    #. After copy, tag and labels are applied to the Asana task and Github issue respectively. This too can be disabled.

    Example
    -------

    This is a `sample Github issue <https://github.com/talha131/AsanaToGithub/issues/1>`_ copied from Asana using AsanaToGithub.
    """,
    license = 'Apache License, (2.0)',
    keywords = 'Asana, Github, Github issues, issue tracker',
    url = 'https://github.com/talha131/asana-to-github',
    download_url = 'https://github.com/talha131/AsanaToGithub/tarball/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Utilities',
        'Environment :: Console',
        'Intended Audience :: Developers',
        ],
    install_requires=install_requires,
    dependency_links = dependency_links,
    entry_points = {
        'console_scripts': ['asanatogithub = asana_to_github.asana_to_github:main']
        }
    )
