import pytest

def test_complex_number_equality():
    complex_number_one = ComplexNumber(3, 5)
    complex_number_two = ComplexNumber(3, 5)

    assert complex_number_one == complex_number_two