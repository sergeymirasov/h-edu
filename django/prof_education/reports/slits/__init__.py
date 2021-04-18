from .education_direction import EducationDirectionSlit
from .region import RegionSlit
from .total import TotalSlit


def get_slits():
    return [
        EducationDirectionSlit(),
        TotalSlit(),
        RegionSlit(),
    ]


def get_slits_dict():
    return {slit.name: slit for slit in get_slits()}
