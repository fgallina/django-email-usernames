# -*- encoding: utf-8 -*-
from setuptools import setup

setup(
    name='django-email-usernames',
    version='0.1',
    description="User's email address for login and authentication in Django.",
    long_description=open('README.txt').read(),
    author='Håkan Waara',
    author_email='hwaara@gmail.com',
    url='http://github.com/fgallina/django-email-usernames',
    packages=['email_usernames'],
    package_dir={'email_usernames': 'email_usernames'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
