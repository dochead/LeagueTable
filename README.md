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


Sample:

    Enter match results (leave blank or hit CTRL-D when done)
    : 传统算法通过 2, Liddlypool 1
    : અંગ્રેજી 1, Liddlypool 1
    : 传统算法通过 3, અંગ્રેજી 0
    :
    
    League Table:
    
    1. 传统算法通过, 6pts
    2. Liddlypool, 1pts
    2. અંગ્રેજી, 1pts

#### Run the script with sample data and with logging
* run_league --filename LeagueTable/samples/results.txt
* run_league --filename LeagueTable/samples/results.txt --log_config LeagueTable/samples/logging.json

#### Run the tests
* cd LeagueTable/tests
* python -m unittest discover .

## License
BSD