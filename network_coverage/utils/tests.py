import pytest

from utils.tools import gps_cord_from_Lambert93, get_city_by_gps_cord, Coordinates


@pytest.mark.parametrize(
    "x, y, gps_cord",
    [
        (102980, 6847973, (-5.0888561153013425, 48.4565745588153)),
        (102980, 6847973, (-5.0888561153013425, 48.4565745588153)),
    ],
)
def test_gps_cord_from_Lambert93(x, y, gps_cord):
    gps_cord_result = gps_cord_from_Lambert93(x=x, y=y)
    print(f"Result: {gps_cord_result}")
    assert set(gps_cord) & set(gps_cord_result)


@pytest.mark.parametrize(
    "latitude, longitude, city", [(48.4565745588153, -5.0888561153013425, "Ouessant"),],
)
def test_get_city_by_gps_cord(latitude, longitude, city):
    result_city = get_city_by_gps_cord(Coordinates(latitude=latitude, longitude=longitude))
    print(f"Result city: {result_city}")
    assert result_city == city
