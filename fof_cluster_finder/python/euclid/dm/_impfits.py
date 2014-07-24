# /home/sartor/pymodule/euclid/dm/_impfits.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:95932c6e7cbd7814eb20271e660263f6bcf8ffdc
# Generated 2014-07-23 16:11:22.132194 by PyXB version 1.2.3
# Namespace http://euclid.esa.org/schema/bas/imp/fits [xmlns:impfits]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:392da7a4-1273-11e4-a458-90b11c83965f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import euclid.dm._dtd as _ImportedBinding_euclid_dm__dtd

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/imp/fits', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}stringKeywordValue
class stringKeywordValue (pyxb.binding.datatypes.string):

    """Describes the allowed values of a string type HDU header keyword. It allows for up to 68 ASCII text characters (decimal 32 through 126). Note that the single quote characters used in the FITS file should NOT be included in this string."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'stringKeywordValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 14, 4)
    _Documentation = u'Describes the allowed values of a string type HDU header keyword. It allows for up to 68 ASCII text characters (decimal 32 through 126). Note that the single quote characters used in the FITS file should NOT be included in this string.'
stringKeywordValue._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(68L))
stringKeywordValue._CF_pattern = pyxb.binding.facets.CF_pattern()
stringKeywordValue._CF_pattern.addPattern(pattern=u'([ -~])*')
stringKeywordValue._InitializeFacetMap(stringKeywordValue._CF_maxLength,
   stringKeywordValue._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'stringKeywordValue', stringKeywordValue)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}logicalKeywordValue
class logicalKeywordValue (pyxb.binding.datatypes.boolean):

    """Describes the allowed values of a logical type HDU header keyword. It takes the values "true" and "false" as they are defined by the XSL Schema boolean type and NOT the "T" and "F" defined in the FITS specification. This is done to make easier the implementation of the different parsers."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'logicalKeywordValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 24, 4)
    _Documentation = u'Describes the allowed values of a logical type HDU header keyword. It takes the values "true" and "false" as they are defined by the XSL Schema boolean type and NOT the "T" and "F" defined in the FITS specification. This is done to make easier the implementation of the different parsers.'
logicalKeywordValue._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'logicalKeywordValue', logicalKeywordValue)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}integerKeywordValue
class integerKeywordValue (pyxb.binding.datatypes.long):

    """Describes the allowed values of an integer type HDU header keyword. It can be any 64 bit integer, as defined by the XML Schema."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'integerKeywordValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 31, 4)
    _Documentation = u'Describes the allowed values of an integer type HDU header keyword. It can be any 64 bit integer, as defined by the XML Schema.'
integerKeywordValue._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'integerKeywordValue', integerKeywordValue)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}doubleKeywordValue
class doubleKeywordValue (pyxb.binding.datatypes.double):

    """Describes the allowed values of a floating point type HDU header keyword. It can be any 64 bit double, as defined by the XML Schema. Note that this definition is more strict than the FITS definition, but this is necessary to achieve a unique interpretation of the number between different systems."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'doubleKeywordValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 38, 4)
    _Documentation = u'Describes the allowed values of a floating point type HDU header keyword. It can be any 64 bit double, as defined by the XML Schema. Note that this definition is more strict than the FITS definition, but this is necessary to achieve a unique interpretation of the number between different systems.'
doubleKeywordValue._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'doubleKeywordValue', doubleKeywordValue)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}headerKeywordName
class headerKeywordName (pyxb.binding.datatypes.string):

    """Describes the format allowed for header keyword names. It allows for strings up to 8 characters long, composed only of digits, upper case letters, the underscore ('_') and the hyphen ('-')."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerKeywordName')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 63, 4)
    _Documentation = u"Describes the format allowed for header keyword names. It allows for strings up to 8 characters long, composed only of digits, upper case letters, the underscore ('_') and the hyphen ('-')."
headerKeywordName._CF_pattern = pyxb.binding.facets.CF_pattern()
headerKeywordName._CF_pattern.addPattern(pattern=u'[-A-Z0-9_]{1,8}')
headerKeywordName._InitializeFacetMap(headerKeywordName._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'headerKeywordName', headerKeywordName)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}binaryTableColumnFormat
class binaryTableColumnFormat (pyxb.binding.datatypes.string):

    """Describes the different formats allowed for a column of a FITS binary table. It is equivalent with the TFORMn FITS keyword. The format is "rT". The repeat count "r" is a non-negative integer specifying the number of elements of type "T". It can take the value 0 and if it is absent it defaults to 1. The type "T" can take the following values:
                L - Logical (1 byte)
                X - Bit (1bit)
                B - Unsigned byte (1 byte)
                I - 16-bit integer (2 byte)
                J - 32-bit integer (4 byte)
                K - 64-bit integer (8 byte)
                A - Character (1 byte)
                E - Single precision floating point (4 byte)
                D - Double precision floating poin (8 byte)
                C - Single precision complex (8 byte)
                M - Double precision complex (16byte)
                P - Array Descriptor (32-bit) (8 byte)
                Q - Array Descriptor (64-bit) (16 byte)
                For more information please refer to the FITS standard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'binaryTableColumnFormat')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 72, 4)
    _Documentation = u'Describes the different formats allowed for a column of a FITS binary table. It is equivalent with the TFORMn FITS keyword. The format is "rT". The repeat count "r" is a non-negative integer specifying the number of elements of type "T". It can take the value 0 and if it is absent it defaults to 1. The type "T" can take the following values:\n                L - Logical (1 byte)\n                X - Bit (1bit)\n                B - Unsigned byte (1 byte)\n                I - 16-bit integer (2 byte)\n                J - 32-bit integer (4 byte)\n                K - 64-bit integer (8 byte)\n                A - Character (1 byte)\n                E - Single precision floating point (4 byte)\n                D - Double precision floating poin (8 byte)\n                C - Single precision complex (8 byte)\n                M - Double precision complex (16byte)\n                P - Array Descriptor (32-bit) (8 byte)\n                Q - Array Descriptor (64-bit) (16 byte)\n                For more information please refer to the FITS standard.'
binaryTableColumnFormat._CF_pattern = pyxb.binding.facets.CF_pattern()
binaryTableColumnFormat._CF_pattern.addPattern(pattern=u'([0-9])*[LXBIJKAEDCMPQ]')
binaryTableColumnFormat._InitializeFacetMap(binaryTableColumnFormat._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'binaryTableColumnFormat', binaryTableColumnFormat)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}binaryTableColumnName
class binaryTableColumnName (pyxb.binding.datatypes.string):

    """Describes the format allowed for binary table column names. Note that currently any string of maximum length 68 characters is allowed. The recomendation (be composed only of upper and lower case letters, digits and the underscore '_') is not forced for compatibility with software which does not follows it."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'binaryTableColumnName')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 95, 4)
    _Documentation = u"Describes the format allowed for binary table column names. Note that currently any string of maximum length 68 characters is allowed. The recomendation (be composed only of upper and lower case letters, digits and the underscore '_') is not forced for compatibility with software which does not follows it."
binaryTableColumnName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
binaryTableColumnName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(68L))
binaryTableColumnName._InitializeFacetMap(binaryTableColumnName._CF_minLength,
   binaryTableColumnName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'binaryTableColumnName', binaryTableColumnName)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}arrayNumberOfDimensions
class arrayNumberOfDimensions (pyxb.binding.datatypes.unsignedShort):

    """Describes the allowed number of dimensions of a FITS array. It can get any value between 0 and 999 (inclusive) and it maps to the FITS keyword NAXIS.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'arrayNumberOfDimensions')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 105, 4)
    _Documentation = u'Describes the allowed number of dimensions of a FITS array. It can get any value between 0 and 999 (inclusive) and it maps to the FITS keyword NAXIS.\n            '
arrayNumberOfDimensions._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=arrayNumberOfDimensions, value=pyxb.binding.datatypes.unsignedShort(999L))
arrayNumberOfDimensions._InitializeFacetMap(arrayNumberOfDimensions._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', u'arrayNumberOfDimensions', arrayNumberOfDimensions)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}arrayFormat
class arrayFormat (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Describes the different formats of the array values. It maps to the FITS keyword BITPIX. It can be one of the following:
                8 - Character or unsigned binary integer (1 byte)
                16 - 16-bit integer (2 bytes)
                32 - 32-bit integer (4 bytes)
                64 - 64-bit integer (8 bytes)
                -32 - single precision floating point (4 bytes)
                -64 - double precision floating point (8 bytes)
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'arrayFormat')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 115, 4)
    _Documentation = u'Describes the different formats of the array values. It maps to the FITS keyword BITPIX. It can be one of the following:\n                8 - Character or unsigned binary integer (1 byte)\n                16 - 16-bit integer (2 bytes)\n                32 - 32-bit integer (4 bytes)\n                64 - 64-bit integer (8 bytes)\n                -32 - single precision floating point (4 bytes)\n                -64 - double precision floating point (8 bytes)\n            '
arrayFormat._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=arrayFormat, enum_prefix=None)
arrayFormat._CF_enumeration.addEnumeration(unicode_value=u'8', tag=None)
arrayFormat._CF_enumeration.addEnumeration(unicode_value=u'16', tag=None)
arrayFormat._CF_enumeration.addEnumeration(unicode_value=u'32', tag=None)
arrayFormat._CF_enumeration.addEnumeration(unicode_value=u'64', tag=None)
arrayFormat._CF_enumeration.addEnumeration(unicode_value=u'-32', tag=None)
arrayFormat._CF_enumeration.addEnumeration(unicode_value=u'-64', tag=None)
arrayFormat._InitializeFacetMap(arrayFormat._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'arrayFormat', arrayFormat)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}wcsIdentifier
class wcsIdentifier (pyxb.binding.datatypes.string):

    """Describes the possible identifiers for a WCS. These identifiers are mapped to the alphabetic code alpha postfixed to the WCS FITS keywords. It can be any upper case letter (A-Z), which defines an alternative WCS representation, or empty, which defines the primary representation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsIdentifier')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 136, 4)
    _Documentation = u'Describes the possible identifiers for a WCS. These identifiers are mapped to the alphabetic code alpha postfixed to the WCS FITS keywords. It can be any upper case letter (A-Z), which defines an alternative WCS representation, or empty, which defines the primary representation.'
wcsIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
wcsIdentifier._CF_pattern.addPattern(pattern=u'[A-Z]?')
wcsIdentifier._InitializeFacetMap(wcsIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'wcsIdentifier', wcsIdentifier)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}wcsName
class wcsName (pyxb.binding.datatypes.string):

    """Describes the possible names for WCS (FITS keyword WCSNAMEa). It allows for upper and lower case letters, digits and the underscore ('_') character."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsName')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 145, 4)
    _Documentation = u"Describes the possible names for WCS (FITS keyword WCSNAMEa). It allows for upper and lower case letters, digits and the underscore ('_') character."
wcsName._CF_pattern = pyxb.binding.facets.CF_pattern()
wcsName._CF_pattern.addPattern(pattern=u'[a-zA-Z0-9_]*')
wcsName._InitializeFacetMap(wcsName._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'wcsName', wcsName)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}wcsAxisType
class wcsAxisType (pyxb.binding.datatypes.string):

    """Describes the allowed values for an WCS axis type. The allowed values is a string up to 4 characters consisting of uper case letters, numbers and the underscore "_". The empty string means a linear undefined axis."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsAxisType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 154, 4)
    _Documentation = u'Describes the allowed values for an WCS axis type. The allowed values is a string up to 4 characters consisting of uper case letters, numbers and the underscore "_". The empty string means a linear undefined axis.'
wcsAxisType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
wcsAxisType._CF_pattern = pyxb.binding.facets.CF_pattern()
wcsAxisType._CF_pattern.addPattern(pattern=u'[A-Z0-9_]*')
wcsAxisType._InitializeFacetMap(wcsAxisType._CF_maxLength,
   wcsAxisType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'wcsAxisType', wcsAxisType)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}wcsAxisName
class wcsAxisName (pyxb.binding.datatypes.string):

    """Represens the name of an WCS axis (FITS keyword CNAMEia. It allows for upper and lower case letters, digits and the underscore ('_') character."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsAxisName')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 164, 4)
    _Documentation = u"Represens the name of an WCS axis (FITS keyword CNAMEia. It allows for upper and lower case letters, digits and the underscore ('_') character."
wcsAxisName._CF_pattern = pyxb.binding.facets.CF_pattern()
wcsAxisName._CF_pattern.addPattern(pattern=u'[a-zA-Z0-9_]*')
wcsAxisName._InitializeFacetMap(wcsAxisName._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'wcsAxisName', wcsAxisName)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/fits}wcsAxisProjectionAlgorithm
class wcsAxisProjectionAlgorithm (pyxb.binding.datatypes.string):

    """Describes the allowed values for an WCS axis projection algorithm. It allows for a 3 character string consisting of uper case leters, numbers and the underscore.The empty string means a linear projection. Note that non linear projection algorithms can be used only for specific celestial coordinate system axis and for specific spectral axis, as described in the FITS specification."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsAxisProjectionAlgorithm')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 173, 4)
    _Documentation = u'Describes the allowed values for an WCS axis projection algorithm. It allows for a 3 character string consisting of uper case leters, numbers and the underscore.The empty string means a linear projection. Note that non linear projection algorithms can be used only for specific celestial coordinate system axis and for specific spectral axis, as described in the FITS specification.'
wcsAxisProjectionAlgorithm._CF_pattern = pyxb.binding.facets.CF_pattern()
wcsAxisProjectionAlgorithm._CF_pattern.addPattern(pattern=u'[A-Z0-9_]{3}|')
wcsAxisProjectionAlgorithm._InitializeFacetMap(wcsAxisProjectionAlgorithm._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'wcsAxisProjectionAlgorithm', wcsAxisProjectionAlgorithm)

# List simple type: {http://euclid.esa.org/schema/bas/imp/fits}complexIntegerKeywordValue
# superclasses _ImportedBinding_euclid_dm__dtd.listOfInteger8
class complexIntegerKeywordValue (pyxb.binding.basis.STD_list):

    """Describes the allowed values of a complex integer type HDU header keyword. It is represented as two 64 bit integers seperated by one or more spaces, being the real and imaginary part of the complex number respectively."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'complexIntegerKeywordValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 45, 4)
    _Documentation = u'Describes the allowed values of a complex integer type HDU header keyword. It is represented as two 64 bit integers seperated by one or more spaces, being the real and imaginary part of the complex number respectively.'

    _ItemType = pyxb.binding.datatypes.long
complexIntegerKeywordValue._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
complexIntegerKeywordValue._InitializeFacetMap(complexIntegerKeywordValue._CF_length)
Namespace.addCategoryObject('typeBinding', u'complexIntegerKeywordValue', complexIntegerKeywordValue)

# List simple type: {http://euclid.esa.org/schema/bas/imp/fits}complexDoubleKeywordValue
# superclasses _ImportedBinding_euclid_dm__dtd.listOfDouble
class complexDoubleKeywordValue (pyxb.binding.basis.STD_list):

    """Describes the allowed values of a complex floating point type HDU header keyword. It is represented as two 64 bit doubles seperated by one or more spaces, being the real and imaginary part of the complex number respectively."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'complexDoubleKeywordValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/fits/euc-test-fits.xsd', 54, 4)
    _Documentation = u'Describes the allowed values of a complex floating point type HDU header keyword. It is represented as two 64 bit doubles seperated by one or more spaces, being the real and imaginary part of the complex number respectively.'

    _ItemType = pyxb.binding.datatypes.double
complexDoubleKeywordValue._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
complexDoubleKeywordValue._InitializeFacetMap(complexDoubleKeywordValue._CF_length)
Namespace.addCategoryObject('typeBinding', u'complexDoubleKeywordValue', complexDoubleKeywordValue)
