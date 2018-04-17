# the name of this file is not permanent just saving my creativity for design
import csv

def csv_extractor(filename):
    people = []
    with open(filename, 'rb') as csvfile:
        ledger = csv.reader(csvfile, delimiter=',', quotechar='|')
        people = [line for line in ledger]
    return people

# create a class with the attributes/functionality from the index.py module
class person:
    firstname = 'no_name_set'
    lastname = 'no_name_set'
    email = 'no_email_set'
    bucket_location = 'no_location_set'
    photo_locations = []
    photo_count = 0
    def person_from_csvline(self, line):
        self.firstname,self.lastname,self.email,self.bucket_location = line

    # person attribute extraction function -- will need resources to handle CSV files
    # in this method try and extract information from the bucket if the folder/path doesn't
    # exist then create it
    # --------------------
if __name__ == '__main__':
    filename = 'example_csvfile.csv'
    people = csv_extractor(filename)
    i = 0
    a_person = []
    for line in people:
        a_person.append(person())
        a_person[i].person_from_csvline(line)
        i = i + 1
    for persons in a_person:
        print persons.firstname
