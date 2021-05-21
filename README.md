# fault-tolerance
Project to demonstrate fault tolerance in loan repayment app.
## Getting Started
- The project consists of an isolated backend and frontend.
- Frontend assets are in the templates directory.
- Backend files are in the project root.
## Test Run
- Deploy a web server on the static assets in the templates directory.
- Install all dependencies for python in the requirements file.
- Change the first line of the python code to #!/path-to-python executable.
- Start the python backend with runserver.sh

## Brief
- The project demonstrates aspects of fault tolerance in distributed systems mainly:-
### Failure Detection
- Demonstrated by use of timeouts.
- In this project timeouts are used to detect a response faiure.
### Failure Recovery
- Demonstrated by use of retries after timeouts.
- Demonstrated also by use of replication for process resilience.


