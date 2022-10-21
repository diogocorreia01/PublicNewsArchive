import json

def computeTopNERs(input_filename, output_filename):
    def computeTopNERs(input_filename, output_filename):

        from collections import Counter
        path = "data/"
        jsonFile = open(path + input_filename, encoding="utf8")
        data = json.load(jsonFile)

        Locations = []
        Organizations = []
        People = []

        for newsarticle in data:
            for location in newsarticle['Locations']:
                Locations.append(location.lower())
            for organization in newsarticle['Organizations']:
                Organizations.append(organization.lower())
            for people in newsarticle['People']:
                People.append(people.lower())

        # Count
        counter_locations = Counter(Locations)
        counter_locations_sorted = sorted(counter_locations.items(), key=lambda pair: pair[1], reverse=True)

        counter_organizations = Counter(Organizations)
        counter_organizations_sorted = sorted(counter_organizations.items(), key=lambda pair: pair[1], reverse=True)

        counter_people = Counter(People)
        counter_people_sorted = sorted(counter_people.items(), key=lambda pair: pair[1], reverse=True)

        # Output Locations Json File

        with open(f'{path + output_filename}_Locations.json', 'w', encoding='utf8') as fp:
            json.dump(counter_locations_sorted, fp, ensure_ascii=False)

        with open(f'{path + output_filename}_Organizations.json', 'w', encoding='utf8') as fp:
            json.dump(counter_organizations_sorted, fp, indent=4, ensure_ascii=False)

        with open(f'{path + output_filename}_People.json', 'w', encoding='utf8') as fp:
            json.dump(counter_people_sorted, fp, indent=4, ensure_ascii=False)





