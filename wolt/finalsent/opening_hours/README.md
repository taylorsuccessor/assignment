# Wolt: Task to Huminize opening hours json
- solution:
    - [Dataframe Solution](#dataframe-solution)
    - [Loop Solution](#loop-solution)
   
- How to install:
    - [How to install](#how-to-install) \
          - [Docker and docker-compose](#docker-and-docker-compose) \
          - [By virtual environment](#by-virtual-environment)  \
          - [By .pyenv](#by-pyenv) 

- Testing (the same test will test both solutions for same data):
    - [How to test](#how-to-test)
    
- Thoughts:
    - [My Thoughts In Data Format And Json Structure](#my-thoughts-in-data-format-and-json-structure)
 
The target of this task to convert json to readable text
We have Json data contains info about restaurant opening hours and we need to make these info readable for human.

for this task I've implemented two solutions.
1. * [Convert Json to Dataframe and order it then take every two lines](#dataframe-solution)
2. * [Sorting the Json and loop over it and colect the opening hours](#loop-solution)


## Dataframe solution

this solution is to convert the data to dataframe


| day_name  | day  | value | type |   
|-----------|------|-------|------|
|  sunday   |   7  |  4000 | open |
|  sunday   |   7  |  8000 | close|
|           |      |       |      |

we sort data by [day, value]
and loop by two rows so we have open -> close and open day

1. - if we start with close row we move it to the end
2. - if the number of rows not even the data not valid
3. - if we have two open after each other directly the data not valid



## Loop Solution

first, we sort the days by the pre defined Map we have (Monday: 1 ...) \
then we order the hours in the day using the ( value = hour ) UNIX time \
then we start loop: \
We save when it open in avariable and when it's closed we append to day data the open and the close hour \
we have to handle some spicial cases like if the week start with open and the close in the last day


# How to install


1. [Docker and docker-compose](#docker-and-docker-compose)
2. [By virtual environment](#by-virtual-environment)
3. [By .pyenv](#by-pyenv)

## Docker and docker-compose
Currently I'm using docker and docker-compose to save Python (3.9) version a  pip 21.3.1 version \
and this is the easest way 
1. [install docker](https://docs.docker.com/engine/install/ubuntu/) 
2. [install docker-compose](https://docs.docker.com/compose/install/)
3. unzip the the code file and cd inside the folder
4. run docker-compose up
5. go to your browser [http://localhost:8000/docs](http://localhost:8000/docs)

## By virtual environment

make sure you have Python 3.9 and Pip 21.3.1

1. [Install Python 3.9](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)
2. unzip code file
3. [install virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

        python3 -m pip install --user virtualenv
          
4. cd to your project and create virtual env by run
   
        python3 -m venv .venv
        
5. activate your environment
 
        source .venv/bin/activate
        
6. Make sure you have correct pip version

        pip install --upgrade pip==21.3.1
7. install project packages

        pip install -r requirements.txt

8. Run the server 
        
        uvicorn main:app --reload --host 0.0.0.0 --port 8000
9. Test your app

        pytest -vv

## By .pyenv

same as the last way of installation you can use \
[Install .pyenv](https://github.com/pyenv/pyenv)

you can install spicific version of python and follow [By virtual environment](#by-virtual-environment)


# How to Test

`he same test will test both solutions for same data`


  
    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 422

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 422



* for testing I've added  => RUN pytest -vv inside Dockerfile so the build will not success till the test success
* if you are using virtualenv just run >> pytest -vv
* you can also enter the docker container and run the test
cd to your project first
          
          docker-compose exec server /bin/bash
          pytest -vv


# My Thoughts in data format and JSON structure

If we look for the solution we always have to loop over the days and over the hour of the days \
from developer or (from code) side it's better for me to have more structured data or as a table like this

        [
          {"day": "sunday", "value": 4000, "type": "open"},
          {"day": "sunday", "value": 8000, "type": "close"}
        ]
or CSV file

| day_name  | value | type |   
|-----------|-------|------|
|  sunday   |  4000 | open |
|  sunday   |  8000 | close|


So we can easily convert it to Dataframe or sort it \
but for the human it's easier to have it group by day 

