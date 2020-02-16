## Dependencies
Only python3 and functools (which comes built-in) is required, and usually comes with most Linux distributions; if not, you can install dependencies with one of the following commands, depending on your package manager:
### brew
brew install python3.6
### apt
sudo apt-get update

sudo apt-get install python3.6
### yum
yum install -y python3.6

## Tests
There are three functions implemented in the odd_occurrences.py file.
One can simply execute the file in the command line, then call the following functions, each with a list of integers as the only argument.

odd_occurrence_xor(<List[Int]>)

odd_occurrence_parity_set(<List[Int]>)

odd_occurrence_hashmap(<List[Int]>)
