import pytest
from datetime import datetime, timedelta

from cooking_session import generate_unique_ids, is_session_valid

# Test generate_unique_ids function
def test_generate_unique_ids():
    # Define test data
    test_data = {
        'Customer_id': '1234567',
        'Meter_id': 'KE01234567',
        'Start_time': 1616060332  # Example Unix timestamp
    }
    
    # Expected result
    expected_result = '1234567KE012345671616060332'
    
    # Call the function and check the result
    result = generate_unique_ids(test_data)
    assert result == expected_result


# Test is_session_valid function
def test_is_session_valid_within_validity_period():
    # Define test data within validity period
    test_data_valid = {
        'Received_on': datetime.now(),
        'Start_time': (datetime.now() - timedelta(days=2)).timestamp()  # Within validity period
    }
    
    # Call the function and check the result
    result = is_session_valid(test_data_valid)
    assert result is True


def test_is_session_valid_outside_validity_period():
    # Define test data outside validity period
    test_data_invalid = {
        'Received_on': datetime.now(),
        'Start_time': (datetime.now() - timedelta(days=4)).timestamp()  # Outside validity period
    }
    
    # Call the function and check the result
    result = is_session_valid(test_data_invalid)
    assert result is False
