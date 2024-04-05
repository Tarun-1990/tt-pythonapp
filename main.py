from google.cloud import secretmanager
import google_crc32c
import json, datetime
from google.cloud import storage 
from google.oauth2 import service_account

def read_credentials():
    print('Inside read credentials function')

def main():
    read_credentials()
    total = 10
    for counter in range(total):
        print(f'Processing {counter} folder')
        for prefix in range(total):
            print(f'Factoring {prefix} destination')

if __name__ == "__main__":
    main()
