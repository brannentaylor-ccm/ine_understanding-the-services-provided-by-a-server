#!/usr/bin/python3
import requests
from time import sleep

""""""

def get_url(schema:str = '', domain:str = '', port:int = 80, endpoint:str = ''):
    if not schema:
        schema = 'http://'
    if not domain:
        domain = '127.0.0.1'
    if port != 80 or port != 443:
        port = str(':5009')
    if not endpoint:
        endpoint = '/Slow-NASA'
    return schema + domain + port + endpoint

def main():

    # url = "http://127.0.0.1:5009/NASA"
    url = get_url()
    print(url)
    # input()

    types_ = set()
    sleeptimer = 0
    for _ in range(25):
        try:
            r = requests.get(url, verify=False)
            # content_type = r.headers.get("Content-Type")
            # types_.add(content_type)
            # print(_+1, r.status_code, r.headers.get("Content-Type"), sleeptimer)
            if r.status_code != 200:
                sleeptimer += 1
                print(f"{_} Server is tired.  Sleeping for {sleeptimer} seconds.")
                sleep(sleeptimer)
            else:
                print(f"{_} Server is awake.  Returning: {r.headers.get("Content-Type")}")
                sleeptimer = 0


        except Exception as e:
            print(f"Error msg:\n{e}")

    msg = f"\nThere are {len(types_)} types of files on the webpage.  They are:"
    print(f"{msg}\n{'-'*len(msg)}")
    for _ in types_:
        print(_)            
    print()
if __name__ == "__main__":
    main()