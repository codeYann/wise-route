import pytest
from pydantic import ValidationError

from coordinate import Coordinate


def make_coordinate(**overrides) -> dict:
    defaults = {
        "name": "Warehouse A",
        "lat": -23.5505,
        "lng": -46.6333,
    }
    return {**defaults, **overrides}


class TestCoordinateValidName:
    def test_valid_coordinate(self):
        coord = Coordinate(**make_coordinate())
        assert coord.name == "Warehouse A"
        assert coord.lat == -23.5505
        assert coord.lng == -46.6333

    def test_name_is_stripped(self):
        coord = Coordinate(**make_coordinate(name="  Depot  "))
        assert coord.name == "Depot"

    def test_empty_name_raises(self):
        with pytest.raises(ValidationError, match="Name cannot be empty"):
            Coordinate(**make_coordinate(name=""))

    def test_whitespace_only_name_raises(self):
        with pytest.raises(ValidationError, match="Name cannot be empty"):
            Coordinate(**make_coordinate(name="   "))


class TestCoordinateLatitude:
    def test_lat_at_lower_bound(self):
        coord = Coordinate(**make_coordinate(lat=-90.0))
        assert coord.lat == -90.0

    def test_lat_at_upper_bound(self):
        coord = Coordinate(**make_coordinate(lat=90.0))
        assert coord.lat == 90.0

    def test_lat_below_lower_bound_raises(self):
        with pytest.raises(
            ValidationError, match="Latitude must be between -90 and 90 degrees"
        ):
            Coordinate(**make_coordinate(lat=-90.1))

    def test_lat_above_upper_bound_raises(self):
        with pytest.raises(
            ValidationError, match="Latitude must be between -90 and 90 degrees"
        ):
            Coordinate(**make_coordinate(lat=90.1))


class TestCoordinateLongitude:
    def test_lng_at_lower_bound(self):
        coord = Coordinate(**make_coordinate(lng=-180.0))
        assert coord.lng == -180.0

    def test_lng_at_upper_bound(self):
        coord = Coordinate(**make_coordinate(lng=180.0))
        assert coord.lng == 180.0

    def test_lng_below_lower_bound_raises(self):
        with pytest.raises(
            ValidationError, match="Longitude must be between -180 and 180 degrees"
        ):
            Coordinate(**make_coordinate(lng=-180.1))

    def test_lng_above_upper_bound_raises(self):
        with pytest.raises(
            ValidationError, match="Longitude must be between -180 and 180 degrees"
        ):
            Coordinate(**make_coordinate(lng=180.1))
