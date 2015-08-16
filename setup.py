from setuptools import setup, find_packages

setup(
    name='leaguetable',
    version='0.9',
    description='Football League Table library',
    url='https://github.com/dochead/LeagueTable',
    author='Shayan Raghavjee',
    author_email='dochead@gmail.com',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    scripts=['bin/run_league'],
    include_package_data=True
)
