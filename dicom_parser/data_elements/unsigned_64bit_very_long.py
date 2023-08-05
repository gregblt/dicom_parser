from dicom_parser.data_element import DataElement
from dicom_parser.utils.value_representation import ValueRepresentation


class Unsigned64bitVeryLong(DataElement):
    VALUE_REPRESENTATION = ValueRepresentation.UV
