import json


def save_contacts(contacts):
    with open('contacts_backup.json', 'w') as file:
        json.dump(contacts, file, indent=4)


def get_contacts(service):
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1000,
        personFields='names,emailAddresses').execute()
    return results.get('connections', [])
