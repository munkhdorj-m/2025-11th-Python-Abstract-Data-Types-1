import pytest
from assignment import decimal_to_binary, bank_simulation, Stack, Queue

@pytest.mark.parametrize("num,expected", [
    (0, "0"),
    (1, "1"),
    (4, "100"),
    (7, "111"),
    (13, "1101"),
    (32, "100000"),
])
def test_decimal_to_binary(num, expected):
    assert decimal_to_binary(num).strip() == expected.strip()

def test_bank_simulation():
    customers = ["Alice", "Bob", "Charlie"]
    expected = "Serving: Alice\nServing: Bob\nServing: Charlie"
    assert bank_simulation(customers).strip() == expected.strip()


@pytest.mark.parametrize("customers,expected", [
    (["A"], "Serving: A"),
    (["X", "Y"], "Serving: X\nServing: Y"),
    ([], ""),   # empty queue
])
def test_bank_simulation_param(customers, expected):
    assert bank_simulation(customers).strip() == expected.strip()
