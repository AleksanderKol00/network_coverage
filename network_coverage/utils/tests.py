import pytest

from utils.tools import gps_cord_from_Lambert93


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
