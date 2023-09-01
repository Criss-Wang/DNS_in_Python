from typing import List

import glob, json

def load_zone() -> dict:
    json_zones = {}

    zone_files = glob.glob('zones/*.zone')
    for zone in zone_files:
        with open(zone) as zone_data:
            data = json.load(zone_data)
            zone_name = data["$origin"]
            json_zones[zone_name] = data
    return json_zones


def get_zone(domain: List) -> str:
    global zone_data

    zone_name = '.'.join(domain)
    return zone_data[zone_name]

zone_data = load_zone()