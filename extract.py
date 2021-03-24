"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Load NEO data from the given CSV file.
    neo_collection = list()
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)

        for elem in reader:
            if elem["pha"] == "Y":
                hza = True
            else:
                hza = False

            if elem["diameter"] != '':
                neo_collection.append(NearEarthObject(
                    elem["pdes"], elem["name"], hza, float(elem["diameter"])))
            else:
                neo_collection.append(NearEarthObject(
                    elem["pdes"], elem["name"], hza))

    return neo_collection

# print(load_neos('./data/neos.csv'))


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # Load close approach data from the given JSON file.
    ca_collection = list()
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)

        for key in contents["data"]:
            pdes = key[0]
            time = key[3]
            distance = key[4]
            velocity = key[7]

            ca_collection.append(CloseApproach(pdes, time, distance, velocity))

    return ca_collection

# print(load_approaches('./data/cad.json'))
