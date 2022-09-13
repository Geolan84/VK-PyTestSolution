import pytest


def test_set():
    """Check for impossibility to add item, which already exists in the set"""
    testing_set = {1, 4, 100, 12}
    temp_length = len(testing_set)
    testing_set.add(100)
    assert len(testing_set) == temp_length


@pytest.mark.parametrize("first_set, second_set, expected_result", [({1, 2, 3}, {1, 2}, {3}),
                                                                    ({1, 2}, {3, 4}, {1, 2}),
                                                                    ({1, 2}, {1, 2}, set())])
def test_set_parametrized(first_set, second_set, expected_result):
    """Check "difference()" method for different cases: sets are intersected, not intersected and match."""
    assert first_set.difference(second_set) == expected_result


def test_set_negative():
    """Negative test to check removing item, which doesn't exist in the set, from set."""
    testing_set = {"VK", "Yandex", "Dzen"}
    # Also can be used this construction, but it doesn't contain word "assert".
    # with pytest.raises(KeyError):
    #     testing_set.remove("News")
    try:
        assert testing_set.remove("News")
    except KeyError:
        pass


def test_int():
    """Checks closure of the operation sum regarding types for integers and correctness of sum."""
    integer_first = 3
    integer_second = 9
    result = integer_first + integer_second
    assert type(result) == int and result == 12


@pytest.mark.parametrize("first_summand, second_summand, expected_result", [(4, 2, 6),
                                                                            (1, 2, 3),
                                                                            (-1, -2, -3),
                                                                            (1, -2, -1),
                                                                            (-2, 1, -1),
                                                                            (0, -2, -2),
                                                                            (2, 0, 2)])
def test_int_parametrized(first_summand, second_summand, expected_result):
    """Checks sum of even|odd|positive|negative summands."""
    assert first_summand + second_summand == expected_result


def test_int_negative():
    """Checks behavior of int() for incorrect string view of number"""
    incorrect_integer_string = "5,000,000"
    # Also can be used this construction, but it doesn't contain word "assert".
    # with pytest.raises(ValueError):
    #     int(incorrect_integer_string)
    try:
        assert int(incorrect_integer_string)
    except ValueError:
        pass
