
import pytest

from sorter import sort, PackageStacks, PackageSorterWrongTypeError, PackageSorterValueError

@pytest.mark.parametrize("width, height, length, mass, expected_stack", [
    (1, 2, 3, 4, PackageStacks.STANDARD.value),
    (1.5, 2.5, 3.5, 4.5, PackageStacks.STANDARD.value),
    (1.5, 2.5, 3, 4, PackageStacks.STANDARD.value),
    (1, 2, 3, 20, PackageStacks.SPECIAL.value),
    (1, 2, 3, 25, PackageStacks.SPECIAL.value),
    (200, 10, 10, 15, PackageStacks.SPECIAL.value),
    (10, 200, 10, 15, PackageStacks.SPECIAL.value),
    (10, 10, 200, 15, PackageStacks.SPECIAL.value),
    (1000, 1000, 1000, 15, PackageStacks.SPECIAL.value),
    (200, 10, 10, 30, PackageStacks.REJECTED.value),
    (10, 200, 10, 30, PackageStacks.REJECTED.value),
    (10, 10, 200, 30, PackageStacks.REJECTED.value),
    (1000, 1000, 1000, 30, PackageStacks.REJECTED.value),
])
def test_sort(width, height, length, mass, expected_stack):
    stack = sort(width, height, length, mass)
    assert stack == expected_stack

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
