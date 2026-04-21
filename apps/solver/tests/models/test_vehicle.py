import pytest
from pydantic import ValidationError

from vehicle import Vehicle


class TestVehicleMaxCapacity:
    def test_valid_vehicle(self):
        vehicle = Vehicle(max_capacity=100)
        assert vehicle.max_capacity == 100

    def test_zero_max_capacity_raises(self):
        with pytest.raises(
            ValidationError, match="max_capacity must be a positive integer"
        ):
            Vehicle(max_capacity=0)

    def test_negative_max_capacity_raises(self):
        with pytest.raises(
            ValidationError, match="max_capacity must be a positive integer"
        ):
            Vehicle(max_capacity=-10)
