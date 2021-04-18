from .addmission import AdmissionDataSource
from .graduates import GraduatesDataSource
from .students import StudentsDataSource


def get_data_sources():
    return [
        AdmissionDataSource(),
        StudentsDataSource(),
        GraduatesDataSource(),
    ]


def get_data_sources_dict():
    return {data_source.name: data_source for data_source in get_data_sources()}
