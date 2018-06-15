#!/user/bin/env python3

from distutils.core import setup

setup(
    name='dm_tools',
    description='5e D&D DM Tools',
    author='Stefan Safranek',
    author_email='sjsafranek@gmail.com',
    packages=['dm_tools'],
    package_data={
        'dm_tools': ['lib/data/*']
    }
    # ,
    # include_package_data=True
)
