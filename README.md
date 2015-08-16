# LeagueTable
A Football League table representation, feed it results and let it calculate how the league goes.
## Installation and usage
### To use as a library
Inside your virtualenv (or python main if you dare)

* pip install git+https://github.com/dochead/LeagueTable

### To run Tests & Samples and view source

#### Create a virtualenv to test
* virtualenv ~/.vp/leaguetable
* source ~/.vp/leaguetable/bin/activate

#### Clone & install the repo
(in the directory of your choice)

* git clone https://github.com/dochead/LeagueTable.git
* pip install LeagueTable/

#### Run the script with the interactive prompt
* run_league

#### Run the script with sample data
* run_league --filename LeagueTable/samples/results.txt

#### Run the tests
* cd LeagueTable/tests
* python -m unittest discover .

## License
BSD