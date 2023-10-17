from io import StringIO
import pytest
from factor import factorial_calculation

@pytest.mark.parametrize("user_input, expected_output", [("5\n", "Enter a number: The factorial of 5 is 120\n")])
def test_factorial_calculation(capfd, monkeypatch, user_input, expected_output):
    # Simulate user input
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Call the factorial_calculation function
    factorial_calculation()

    # Capture the output
    out, err = capfd.readouterr()

    # Check if the output matches the expected output
    assert out == expected_output