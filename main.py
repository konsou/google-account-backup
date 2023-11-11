from googleapiclient.discovery import build

from contacts import get_contacts, save_contacts
from credentials import get_credentials


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
