import pytest
from pydantic import ValidationError

from models.delivery_point import DeliveryPoint


def make_delivery_point(**overrides) -> dict:
    defaults = {
        "name": "Customer 1",
        "lat": -23.5505,
        "lng": -46.6333,
        "cargo_weight": 5,
    }
    return {**defaults, **overrides}


class TestDeliveryPointInheritance:
    def test_valid_delivery_point(self):
        dp = DeliveryPoint(**make_delivery_point())
        assert dp.name == "Customer 1"
        assert dp.cargo_weight == 5
        assert dp.lat == -23.5505
        assert dp.lng == -46.6333

    def test_inherits_name_strip(self):
        dp = DeliveryPoint(**make_delivery_point(name="  Stop 1  "))
        assert dp.name == "Stop 1"

    def test_inherits_empty_name_validation(self):
        with pytest.raises(ValidationError, match="Name cannot be empty"):
            DeliveryPoint(**make_delivery_point(name=""))

    def test_inherits_lat_validation(self):
        with pytest.raises(
            ValidationError, match="Latitude must be between -90 and 90 degrees"
        ):
            DeliveryPoint(**make_delivery_point(lat=91.0))

    def test_inherits_lng_validation(self):
        with pytest.raises(
            ValidationError, match="Longitude must be between -180 and 180 degrees"
        ):
            DeliveryPoint(**make_delivery_point(lng=-181.0))


class TestDeliveryPointCargoWeight:
    def test_zero_cargo_weight_is_valid(self):
        dp = DeliveryPoint(**make_delivery_point(cargo_weight=0))
        assert dp.cargo_weight == 0

    def test_positive_cargo_weight_is_valid(self):
        dp = DeliveryPoint(**make_delivery_point(cargo_weight=50))
        assert dp.cargo_weight == 50

    def test_negative_cargo_weight_raises(self):
        with pytest.raises(ValidationError, match="Cargo weight cannot be negative"):
            DeliveryPoint(**make_delivery_point(cargo_weight=-1))
