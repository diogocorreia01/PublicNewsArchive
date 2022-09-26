import json

def dataPerYear(json_news, output_path):
    print('Opening Your Json File...')
    jsonFile = open(json_news, encoding="utf8")
    data = json.load(jsonFile)
    print('Done')

    # Data Analysis
    locations = []
    organizations = []
    people = []
    for i in data:
        locations.append(i['Locations'])
        organizations.append(i['Organizations'])
        people.append(i['People'])

    newLocations = []
    newOrganizations = []
    newPeople = []
    for location in locations:
        if location != ' ':
            newLocations.append(location)
    for organization in organizations:
        if organization != ' ':
            newOrganizations.append(organization)
    for person in people:
        if person != ' ':
            newPeople.append(person)

    noRepsLocations = []
    noRepsOrganizations = []
    noRepsPeople = []
    for location in newLocations:
        if location not in noRepsLocations:
            noRepsLocations.append(location)
    for organization in newOrganizations:
        if organization not in noRepsOrganizations:
            noRepsOrganizations.append(organization)
    for person in newPeople:
        if person not in noRepsPeople:
            noRepsPeople.append(person)

    countedLoc = []
    countedOrg = []
    countedPeo = []
    finalLocs = []
    finalOrg = []
    finalPeo = []
    for location in noRepsLocations:
        num = newLocations.count(location)
        countedLoc.append(num)
        finalLocs.append(location)
    for organization in noRepsOrganizations:
        num = newOrganizations.count(organization)
        countedOrg.append(num)
        finalOrg.append(organization)
    for person in noRepsPeople:
        num = newPeople.count(person)
        countedPeo.append(num)
        finalPeo.append(person)

    locations_dict = []
    organizations_dict = []
    people_dict = []
    for i in range(len(finalLocs)):
        locations_dict.append({
            "Location": finalLocs[i],
            "Count": countedLoc[i],
        })

    for i in range(len(finalOrg)):
        organizations_dict.append({
            "Organization": finalOrg[i],
            "Count": countedOrg[i]
        })

    for i in range(len(finalPeo)):
        people_dict.append({
            "Person": finalPeo[i],
            "Count": countedPeo[i]
        })

    # Output Locations Json File
    with open(f'{output_path}_Locations.json', 'w', encoding='utf8') as fp:
        json.dump(sorted(locations_dict, reverse=True, key=lambda x:x['Count']), fp, indent=4, sort_keys=True,
                  ensure_ascii=False)
    print('Your Locations Json File is Ready!')

    # Output Organizations Json File
    with open(f'{output_path}_Organizations.json', 'w', encoding='utf8') as fp:
        json.dump(sorted(organizations_dict, reverse=True, key=lambda x: x['Count']), fp, indent=4, sort_keys=True,
                  ensure_ascii=False)
    print('Your Organizations Json File is Ready!')

    # Output People Json File
    with open(f'{output_path}_People.json', 'w', encoding='utf8') as fp:
        json.dump(sorted(people_dict, reverse=True, key=lambda x: x['Count']), fp, indent=4, sort_keys=True,
                  ensure_ascii=False)
    print('Your People Json File is Ready!')





