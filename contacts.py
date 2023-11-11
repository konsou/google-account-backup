import json

# Checked 2023-11-11 from https://developers.google.com/people/api/rest/v1/people/get
VALID_PERSON_FIELDS = (
    "addresses",
    "ageRanges",
    "biographies",
    "birthdays",
    "calendarUrls",
    "clientData",
    "coverPhotos",
    "emailAddresses",
    "events",
    "externalIds",
    "genders",
    "imClients",
    "interests",
    "locales",
    "locations",
    "memberships",
    "metadata",
    "miscKeywords",
    "names",
    "nicknames",
    "occupations",
    "organizations",
    "phoneNumbers",
    "photos",
    "relations",
    "sipAddresses",
    "skills",
    "urls",
    "userDefined",
)


def save_contacts(contacts):
    with open('contacts_backup.json', 'w') as file:
        json.dump(contacts, file, indent=4)


def get_contacts(service):
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1000,
        personFields=','.join(VALID_PERSON_FIELDS)).execute()
    return results.get('connections', [])
