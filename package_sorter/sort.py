from typing import Union
from enum import Enum

class PackageStacks(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def _is_bulky(
        width_in_cm: Union[int, float],
        height_in_cm: Union[int, float],
        length_in_cm: Union[int, float]) -> bool:
    """
    A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ 
    or when one of its dimensions is greater or equal to 150 cm
    """
    
    for dimension in [width_in_cm, height_in_cm, length_in_cm]:
        if dimension >= 150:
            return True
    
    volume = width_in_cm * height_in_cm * length_in_cm
    return volume >= 1_000_000

def _is_heavy(weight_in_kg: Union[int, float]) -> bool:
    """ A package is heavy when its mass is greater or equal to 20 kg """
    return weight_in_kg >= 20

def sort(width: Union[int, float], height: Union[int, float], length: Union[int, float], mass: Union[int, float]) -> str:
    """
    Receives package data and determine which stack it should to go to:

    - **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
    - **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
    - **REJECTED**: packages that are **both** heavy and bulky are rejected.

    """

    is_bulky = _is_bulky(width, height, length)
    is_heavy = _is_heavy(mass)

    if is_bulky and is_heavy:
        return PackageStacks.REJECTED.value
    
    if is_bulky and is_heavy:
        return PackageStacks.SPECIAL.value
    
    return PackageStacks.STANDARD.value
    