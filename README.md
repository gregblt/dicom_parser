[![Documentation Status](https://readthedocs.org/projects/dicom-parser/badge/?version=latest)](http://dicom-parser.readthedocs.io/?badge=latest)
[![PyPI version](https://img.shields.io/pypi/v/dicom_parser.svg)](https://pypi.python.org/pypi/pylabber/)
[![PyPI status](https://img.shields.io/pypi/status/dicom_parser.svg)](https://pypi.python.org/pypi/pylabber/)
![Coverage](coverage.svg)

# dicom_parser

*dicom_parser* is a utility python package meant to facilitate access to
[DICOM](https://www.dicomstandard.org/) header information by extending the functionality of
*[pydicom]*.

Essentially, *dicom_parser* uses [DICOM](https://www.dicomstandard.org/)'s
[data-element](https://northstar-www.dartmouth.edu/doc/idl/html_6.2/DICOM_Attributes.html)
[value-representation (VR)](http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html),
as well as prior knowledge on vendor-specific private tags or encoding schemes,
in order to transform them to more "pythonic" data structures when possible.

For more information, please see
[the documentation](http://dicom-parser.readthedocs.io/?badge=latest).

---

## Installation

To install the latest version of `dicom_parser`, simply run:

```shell
    pip install dicom_parser
```

---

## Quickstart

The most basic usage case is reading a single DICOM image (*.dcm* file) as
an [Image](https://dicom-parser.readthedocs.io/en/latest/modules/dicom_parser.html#dicom_parser.image.Image)
instance.

```python
    from dicom_parser import Image

    # Create a DICOM Image object
    image = Image('/path/to/dicom/file.dcm')
```


### Coversion to Python's native types

*dicom_parser* provides *dict*-like access to the parsed values of the
[header](https://dcm4che.atlassian.net/wiki/spaces/d2/pages/1835038/A+Very+Basic+DICOM+Introduction)'s
data-elements. The raw values as read by *[pydicom]* remain accessible through the *raw* attribute.

#### Examples

Decimal String (DS) to *float* using the [Header] class's
[get](https://dicom-parser.readthedocs.io/en/latest/modules/dicom_parser.html#dicom_parser.header.Header.get)
method:

```python
    raw_value = image.header.raw['ImagingFrequency'].value
    raw_value
    >> "123.25993"
    type(raw_value)
    >> str

    parsed_value = image.header.get('ImagingFrequency')
    parsed_value
    >> 123.25993
    type(parsed_value)
    >> float
```

Age String (AS) to *float*:

```python
    raw_value = image.header.raw['PatientAge'].value
    raw_value
    >> "027Y"
    type(raw_value)
    >> str

    parsed_value = image.header.get('PatientAge')
    parsed_value
    >> 27.0
    type(parsed_value)
    >> float
```

Date String (DA) to *[datetime.date]* using the [Header] class's
indexing operator/subscript notation:

```python

    raw_value = image.header.raw['PatientBirthDate'].value
    raw_value
    >> "19901214"
    type(raw_value)
    >> str

    parsed_value = image.header['PatientBirthDate']
    parsed_value
    >> datetime.date(1990, 12, 14)
    type(parsed_value)
    >> datetime.date
```

Et cetera.

>   The *dict*-like functionality also includes safe getting:
>
>   ```python
>       image.header.get('MissingKey')
>       >> None
>       image.header.get('MissingKey', 'DefaultValue')
>       >> 'DefaultValue'
>   ```
>
>   As well as raising a KeyError for missing keys with the indexing operator:
>
>   ```python
>       image.header['MissingKey']
>       >> ...
>       >> KeyError: "The keyword: 'MissingKey' does not exist in the header!"
>   ```


### Read DICOM series directory as a [Series]


Another useful class this package offers is the [Series] class:

```python
    from dicom_parser import Series

    series = Series('/path/to/dicom/series/')

    # Read stacked pixel arrays as a 3D volume
    type(series.data)
    >>> numpy.ndarray
    series.data.shape
    >> (224, 224, 208)

    # Access the underlying Image instances
    series.images[6].header.get('InstanceNumber')
    >> 7    # instance numbers are 1-indexed
```

[datetime.date]: https://docs.python.org/3/library/datetime.html#available-types
[Header]: https://dicom-parser.readthedocs.io/en/latest/modules/dicom_parser.html#dicom_parser.header.Header
[pydicom]: https://pydicom.github.io/
[Series]: https://dicom-parser.readthedocs.io/en/latest/modules/dicom_parser.html#dicom_parser.series.Series