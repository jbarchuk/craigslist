from setuptools import setup

setup(
    name='craigslist',
    version='0.1.0',
    description='Python wrapper for craigslist.',
    author='Al Johri',
    author_email='al.johri@gmail.com',
    url='https://github.com/AlJohri/craigslist',
    license='MIT',
    packages=['craigslist', 'craigslist.api', 'craigslist._search', 'craigslist._search.jsonsearch', 'craigslist._search.regularsearch'],
    package_data={'craigslist': ['data/*.json']},
    install_requires=['requests', 'cssselect', 'lxml', 'blessings'],
    entry_points={
        'console_scripts': [
            'craigslist=craigslist.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ]
)
