import json

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


def get_credentials():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def save_contacts(contacts):
    with open('contacts_backup.json', 'w') as file:
        json.dump(contacts, file, indent=4)


def get_contacts(service):
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1000,
        personFields='names,emailAddresses').execute()
    return results.get('connections', [])


def main():
    creds = get_credentials()
    service = build('people', 'v1', credentials=creds)
    contacts = get_contacts(service)
    save_contacts(contacts)

    # Process the contacts as needed
    # For example, print out the names of the contacts
    for contact in contacts:
        names = contact.get('names', [])
        if names:
            name = names[0].get('displayName')
            print(name)


if __name__ == '__main__':
    main()
