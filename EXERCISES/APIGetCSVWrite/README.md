# Isentia Exercises

 ```Project Description:```
 
    - Project have implementation to fetch results from a configurable api endpoint 
    - Validating the Response with all, possible status code.
    - Custom selection of reponse keys or columns 
    - Storing back the response output in a csv file.
    
  ```Project Component:```
  
    - Test Methods      : All test methods whcih are run against the helper methods   
                          - /tests/test_APIResponse.py
    - Helper Function   : The helper class file having the methods for fetching api data and stroing as a csv file 
                          - /src/APIHelper.py
    - constants         : Constants file have the details of all the constants of the project like the directories etc
                          - /constants.py
    - Output(csv files) : All the outputs are written to outputs direcrtory
                          - /outputs/
    - Log               : Logs are written to this direcvory 
                          - /logs/API.log
    - Data              : All input data  to be tried out by various trest methods woulbe be going into this directory 
                          - /data/
    - Conf              : All configuration data like the response keys which need to be fetched \
                          can be custom added to the conf file and placed under this directory  
                          - api.conf

      (Tried to implement the Decorator Log part but facing some issue as i am implementing this first time.
      Took Help from some online blog on this.)
      
  ```External Library:```
  
    requests
    csv
    logging
    inspect
  
  ```Execution:```
  
  Execute from test_APIResponse.TestAPI Module.
    