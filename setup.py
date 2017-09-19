import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-celery-status-monitor',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GNU GPL v3',
    description='Simple app that runs celery task and provide endpoint to check if celery is up',
    long_description=README,
    url='https://github.com/jakubste/django-celery-status-monitor',
    author='Jakub Stępak',
    author_email='jakub.ste@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: GNU GPL v3',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],
)