#!/usr/bin/python3
import requests
import pprint

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = input("Please enter a start date in format YYYY-MM-DD: ").strip("\n")

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
#    print(neodata)

    for x in neodata["near_earth_objects"].keys():
        for aster in neodata["near_earth_objects"][x]:
           pprint.pprint(aster["name"], ["size"])

    # print(aster["name"] + "\n")

if __name__ == "__main__":
    main()

