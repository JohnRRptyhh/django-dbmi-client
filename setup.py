import os
import re
from io import open

from setuptools import find_packages, setup


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.join(package, '__init__.py'))).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('dbmi_client')

setup(
    name='django-dbmi-client',
    version=version,
    url='https://github.com/hms-dbmi/django-dbmi-client',
    author='HMS DBMI Tech-core',
    author_email='dbmi-tech-core@hms.harvard.edu',
    packages=find_packages(exclude=['tests*']),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=[
        'django>=1.11',
        'djangorestframework',
        'cryptography',
        'requests',
        "jwcrypto",
        "furl",
        "pyjwt",
        "django-bootstrap3",
        "raven>=6.9.0",
        # 'django>=1.11.0,<2.2',
        # 'djangorestframework>=3.8.2',
        # 'cryptography~=2.5',
        # 'requests~=2.19.1',
        # "jwcrypto~=0.6.0",
        # "furl~=1.2.1",
        # "pyjwt~=1.7.1",
        # "django-bootstrap3~=11.0.0",
    ],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
