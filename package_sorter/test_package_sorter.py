
import pytest

from sorter import sort, PackageSorterWrongTypeError, PackageSorterValueError

@pytest.mark.parametrize("width, height, length, mass, expected_error", [
    ("1", 2, 3, 4.5, "Parameter width should be one of: int, float. Received <class 'str'>"),
    (1, "2", 3, 4.5, "Parameter height should be one of: int, float. Received <class 'str'>"),
    (1, 2, "3", 4.5, "Parameter length should be one of: int, float. Received <class 'str'>"),
    (1, 2, 3, "4.5", "Parameter mass should be one of: int, float. Received <class 'str'>"),
    (None, 2, 3, 4.5, "Parameter width should be one of: int, float. Received <class 'NoneType'>"),
    (1, [2], 3, 4.5, "Parameter height should be one of: int, float. Received <class 'list'>"),
    (1, 2, (3,), 4.5, "Parameter length should be one of: int, float. Received <class 'tuple'>"),
    (1, 2, 3, {}, "Parameter mass should be one of: int, float. Received <class 'dict'>"),
])
def test_sort_wrong_type_error(width, height, length, mass, expected_error):
    with pytest.raises(PackageSorterWrongTypeError) as e_info:
        _ = sort(width, height, length, mass)
    
    assert expected_error in str(e_info)

@pytest.mark.parametrize("width, height, length, mass, expected_error", [
    (0, 2, 3, 4.5, "Parameter width should be higher than zero. Received 0"),
    (1, 0, 3, 4.5, "Parameter height should be higher than zero. Received 0"),
    (1, 2, 0, 4.5, "Parameter length should be higher than zero. Received 0"),
    (1, 2, 3, 0.0, "Parameter mass should be higher than zero. Received 0.0"),
    (-5, 2, 3, 4.5, "Parameter width should be higher than zero. Received -5"),
    (1, -5, 3, 4.5, "Parameter height should be higher than zero. Received -5"),
    (1, 2, -5, 4.5, "Parameter length should be higher than zero. Received -5"),
    (1, 2, 3, -5.0, "Parameter mass should be higher than zero. Received -5.0"),
])
def test_sort_value_error(width, height, length, mass, expected_error):
    with pytest.raises(PackageSorterValueError) as e_info:
        _ = sort(width, height, length, mass)
    
    assert expected_error in str(e_info)
