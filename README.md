# Flowlog monitoring service

This is the Flowlog monitoring service. It records number of bytes transferred for evey network flows and provides an API to query it at an hourly basis.

## Design Details

The Flowlog monitoring service consists of a front end REST server that receives the POST and GET calls.
The calls then are routed to another class which does the input validation and performs the business logic.
Datastore that stores the request data is stored in another module.

The POST/ Write Flow goes like this:

POST call --> main/Frontend --> FlowMonitoringService --> Validation --> DataStore 

The GET/ Read Flow goes like this:

GET call --> main/Frontend --> FlowMonitoringService --> Validation --> DataStore --> Returns Output

## Implementation Details
Python is used as the language to implement this assignment due to its ease of use.
[Flask](https://flask.palletsprojects.com/en/2.1.x/) is used as a framework to easily create a REST API server. 
The flowlogs are stored in an in-memory datastore which is backed by a python dictionary. The dictionary is keyed by the hour so that all flowlogs for that hour are stored together. The value of the dictionary is another dictionary. The key for this inner dictionary is the unique combination of source app, destination app and vpc_id. The value of the inner dictionary is the flowlog object that stores all info about a flow.

## Error Handling

The below validations are captured in the design/implementation

GET call:
- Validate Query param is not empty
- Validate hour is integer
- Validate hour is positive

POST call:
- Validate input data is not empty
- Validate hour is integer
- Validate hour is positive
- Validate bytes_tx is integer
- Validate bytes_tx is positive
- Validate bytes_rx is integer
- Validate bytes_rx is positive
- Validate src_app is string
- Validate dest_app is string
- Validate vpc_id is string


## Assumptions and limitations
- This implementation assumes that the service will be run on a single node.
- This implementation does not tolerate crashes/restarts. That is, upon restarting the service, any flow data that was stored previously will be lost.

## Code layout
All the python source code is under the src/ directory. The main.py file is the starting point of the application.

## Requirements
This application is tested on macOS Big Sur (version 11.2) using python 3.8.2.
The external python packages required are listed in requirements.txt file.

## Run the service
Navigate to the src/ directory of the project. Then run - 
> python3 main.py

This command starts the Flowlog monitoring service. The service listens on all interfaces on port 3000. You can press Ctrl-C to exit.

## Run tests
You can run the unit tests using the included Makefile. To run the tests, from the src/ directory, run - 
> make test

This will run all the unit tests. If you wish to run a subset of the tests, you can use pytest filter flag via the Makefile as follows - 
> make test-filter FILTER=\<pattern-to-match>

The \<pattern-to-match> argument is forwarded to pytest's -k flag. You can pass string patterns that will be matched against file names and function names. You can read the documentation for the flag [here](https://docs.pytest.org/en/stable/usage.html#specifying-tests-selecting-tests).

Happy reviewing!
