from typing import List, Dict, Any

import glob
import json
import os

os.chdir(os.path.dirname(__file__))


def load_zone() -> Dict:
    json_zones = {}
    zone_files = glob.glob('zones/*.zone')
    for zone in zone_files:
        with open(zone) as zone_data:
            data = json.load(zone_data)
            zone_name = data["$origin"]
            json_zones[zone_name] = data
    return json_zones


zone_data = load_zone()


def get_zone(domain: List) -> Dict[str, Any]:
    global zone_data

    zone_name = '.'.join(domain)
    return zone_data[zone_name]
