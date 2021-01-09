from urllib.parse import urljoin

import pyproj
import requests
from attr import dataclass

from utils.static import API_ADDRESS_URL


@dataclass
class Coordinates:
    latitude: float
    longitude: float


def gps_cord_from_Lambert93(x: int, y: int) -> Coordinates:
    lambert = pyproj.Proj(
        "+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs"
    )
    wgs84 = pyproj.Proj("+proj=longlat +ellps=WGS84 +datum=WGS84 + no_defs")
    long, lat = pyproj.transform(lambert, wgs84, x, y)
    return Coordinates(longitude=long, latitude=lat)


def get_city_by_gps_cord(cords: Coordinates) -> str:
    response = requests.get(urljoin(API_ADDRESS_URL, "reverse"), params={"lon": cords.longitude, "lat": cords.latitude})
    city = ""
    if len(response.json()["features"]) > 1:
        raise RuntimeError # TODO
    elif response.json()["features"]:
        city = response.json()["features"][0]["properties"]["city"]
        print(city+"\n") #TODO
    return city
