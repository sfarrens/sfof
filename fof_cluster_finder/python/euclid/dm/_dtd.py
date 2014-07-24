# /home/sartor/pymodule/euclid/dm/_dtd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b271ffc25c73f887dbff4e054cfd41e733c35b7f
# Generated 2014-07-23 16:11:22.131998 by PyXB version 1.2.3
# Namespace http://euclid.esa.org/schema/bas/dtd [xmlns:dtd]

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
import euclid.dm._utd as _ImportedBinding_euclid_dm__utd

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/dtd', create_if_missing=True)
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


# List simple type: {http://euclid.esa.org/schema/bas/dtd}listOfDouble
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfDouble (pyxb.binding.basis.STD_list):

    """An unbounded list of doubles (space separated). Used for tabulated data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfDouble')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 15, 1)
    _Documentation = u'An unbounded list of doubles (space separated). Used for tabulated data.'

    _ItemType = pyxb.binding.datatypes.double
listOfDouble._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfDouble', listOfDouble)

# List simple type: {http://euclid.esa.org/schema/bas/dtd}listOfFloat
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfFloat (pyxb.binding.basis.STD_list):

    """An unbounded list of float. Used for tabulated data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfFloat')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 45, 1)
    _Documentation = u'An unbounded list of float. Used for tabulated data.'

    _ItemType = pyxb.binding.datatypes.float
listOfFloat._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfFloat', listOfFloat)

# List simple type: {http://euclid.esa.org/schema/bas/dtd}listOfInteger1
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfInteger1 (pyxb.binding.basis.STD_list):

    """An unbounded list of one Byte Integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfInteger1')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 51, 1)
    _Documentation = u'An unbounded list of one Byte Integer.'

    _ItemType = pyxb.binding.datatypes.byte
listOfInteger1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfInteger1', listOfInteger1)

# List simple type: {http://euclid.esa.org/schema/bas/dtd}listOfInteger2
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfInteger2 (pyxb.binding.basis.STD_list):

    """An unbounded list of two Bytes (short) Integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfInteger2')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 57, 1)
    _Documentation = u'An unbounded list of two Bytes (short) Integer.'

    _ItemType = pyxb.binding.datatypes.short
listOfInteger2._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfInteger2', listOfInteger2)

# List simple type: {http://euclid.esa.org/schema/bas/dtd}listOfInteger4
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfInteger4 (pyxb.binding.basis.STD_list):

    """An unbounded list of 4  Bytes (int) Integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfInteger4')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 63, 1)
    _Documentation = u'An unbounded list of 4  Bytes (int) Integer.'

    _ItemType = pyxb.binding.datatypes.int
listOfInteger4._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfInteger4', listOfInteger4)

# List simple type: {http://euclid.esa.org/schema/bas/dtd}listOfInteger8
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfInteger8 (pyxb.binding.basis.STD_list):

    """An unbounded list of 8  Bytes (int) Integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfInteger8')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 69, 1)
    _Documentation = u'An unbounded list of 8  Bytes (int) Integer.'

    _ItemType = pyxb.binding.datatypes.long
listOfInteger8._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfInteger8', listOfInteger8)

# Atomic simple type: {http://euclid.esa.org/schema/bas/dtd}hexaString
class hexaString (pyxb.binding.datatypes.string):

    """An hexadecimal number."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hexaString')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 75, 1)
    _Documentation = u'An hexadecimal number.'
hexaString._CF_pattern = pyxb.binding.facets.CF_pattern()
hexaString._CF_pattern.addPattern(pattern=u'[0-9,A-F,a-f]*')
hexaString._InitializeFacetMap(hexaString._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'hexaString', hexaString)

# Atomic simple type: {http://euclid.esa.org/schema/bas/dtd}var64String
class var64String (pyxb.binding.datatypes.string):

    """Character string : exact length 64"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'var64String')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 83, 1)
    _Documentation = u'Character string : exact length 64'
var64String._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
var64String._InitializeFacetMap(var64String._CF_length)
Namespace.addCategoryObject('typeBinding', u'var64String', var64String)

# Atomic simple type: {http://euclid.esa.org/schema/bas/dtd}positiveDouble
class positiveDouble (pyxb.binding.datatypes.double):

    """Double between 0 (inclusive) and infinity"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positiveDouble')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 91, 1)
    _Documentation = u'Double between 0 (inclusive) and infinity'
positiveDouble._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveDouble, value=pyxb.binding.datatypes.double(0.0))
positiveDouble._InitializeFacetMap(positiveDouble._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'positiveDouble', positiveDouble)

# Atomic simple type: {http://euclid.esa.org/schema/bas/dtd}negativeDouble
class negativeDouble (pyxb.binding.datatypes.double):

    """Double between  infinity and O (inclusive)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'negativeDouble')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 99, 1)
    _Documentation = u'Double between  infinity and O (inclusive)'
negativeDouble._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=negativeDouble, value=pyxb.binding.datatypes.double(0.0))
negativeDouble._InitializeFacetMap(negativeDouble._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', u'negativeDouble', negativeDouble)

# Atomic simple type: {http://euclid.esa.org/schema/bas/dtd}percentValue
class percentValue (pyxb.binding.datatypes.double):

    """Double between  0 and 100 inclusive"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'percentValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 107, 1)
    _Documentation = u'Double between  0 and 100 inclusive'
percentValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=percentValue, value=pyxb.binding.datatypes.double(0.0))
percentValue._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=percentValue, value=pyxb.binding.datatypes.double(100.0))
percentValue._InitializeFacetMap(percentValue._CF_minInclusive,
   percentValue._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', u'percentValue', percentValue)

# Atomic simple type: {http://euclid.esa.org/schema/bas/dtd}degAngle
class degAngle (pyxb.binding.datatypes.double):

    """Angle in degrees between -180 and 360		"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'degAngle')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 139, 1)
    _Documentation = u'Angle in degrees between -180 and 360\t\t'
degAngle._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes.anySimpleType(u'360.0'))
degAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=degAngle, value=pyxb.binding.datatypes.double(-180.0))
degAngle._InitializeFacetMap(degAngle._CF_maxExclusive,
   degAngle._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'degAngle', degAngle)

# Atomic simple type: {http://euclid.esa.org/schema/bas/dtd}nameRestriction
class nameRestriction (pyxb.binding.datatypes.string):

    """Basic naming convention: length between 4 and 100 characters, white spaces collapsed"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameRestriction')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 148, 1)
    _Documentation = u'Basic naming convention: length between 4 and 100 characters, white spaces collapsed'
nameRestriction._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
nameRestriction._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
nameRestriction._InitializeFacetMap(nameRestriction._CF_minLength,
   nameRestriction._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'nameRestriction', nameRestriction)

# Atomic simple type: {http://euclid.esa.org/schema/bas/dtd}curveShape
class curveShape (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The position of the points connecting the vertices (or end points) of a polygon in space (so on a sphere) may be a large circle (or geodesic) or a line (iso coordinate on an axis)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'curveShape')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 260, 1)
    _Documentation = u'The position of the points connecting the vertices (or end points) of a polygon in space (so on a sphere) may be a large circle (or geodesic) or a line (iso coordinate on an axis).'
curveShape._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=curveShape, enum_prefix=None)
curveShape.line = curveShape._CF_enumeration.addEnumeration(unicode_value=u'line', tag=u'line')
curveShape.great_circle = curveShape._CF_enumeration.addEnumeration(unicode_value=u'great circle', tag=u'great_circle')
curveShape._InitializeFacetMap(curveShape._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'curveShape', curveShape)

# List simple type: {http://euclid.esa.org/schema/bas/dtd}listOf2Double
# superclasses listOfDouble
class listOf2Double (pyxb.binding.basis.STD_list):

    """Space separated list of 2 double values, used for array2D."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOf2Double')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 21, 1)
    _Documentation = u'Space separated list of 2 double values, used for array2D.'

    _ItemType = pyxb.binding.datatypes.double
listOf2Double._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
listOf2Double._InitializeFacetMap(listOf2Double._CF_length)
Namespace.addCategoryObject('typeBinding', u'listOf2Double', listOf2Double)

# List simple type: {http://euclid.esa.org/schema/bas/dtd}listOf3Double
# superclasses listOfDouble
class listOf3Double (pyxb.binding.basis.STD_list):

    """Space separated list of 3 double values, used for matrix or Array3D."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOf3Double')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 29, 1)
    _Documentation = u'Space separated list of 3 double values, used for matrix or Array3D.'

    _ItemType = pyxb.binding.datatypes.double
listOf3Double._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
listOf3Double._InitializeFacetMap(listOf3Double._CF_length)
Namespace.addCategoryObject('typeBinding', u'listOf3Double', listOf3Double)

# List simple type: {http://euclid.esa.org/schema/bas/dtd}listOf6Double
# superclasses listOfDouble
class listOf6Double (pyxb.binding.basis.STD_list):

    """Space separated list of 6 double values, used for matrix."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOf6Double')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 37, 1)
    _Documentation = u'Space separated list of 6 double values, used for matrix.'

    _ItemType = pyxb.binding.datatypes.double
listOf6Double._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(6L))
listOf6Double._InitializeFacetMap(listOf6Double._CF_length)
Namespace.addCategoryObject('typeBinding', u'listOf6Double', listOf6Double)

# Complex type {http://euclid.esa.org/schema/bas/dtd}matrixDouble3x3 with content type ELEMENT_ONLY
class matrixDouble3x3 (pyxb.binding.basis.complexTypeDefinition):
    """A 3x3 double matrix"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'matrixDouble3x3')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 116, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element row1 uses Python identifier row1
    __row1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'row1'), 'row1', '__httpeuclid_esa_orgschemabasdtd_matrixDouble3x3_row1', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 121, 3), )

    
    row1 = property(__row1.value, __row1.set, None, None)

    
    # Element row2 uses Python identifier row2
    __row2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'row2'), 'row2', '__httpeuclid_esa_orgschemabasdtd_matrixDouble3x3_row2', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 122, 3), )

    
    row2 = property(__row2.value, __row2.set, None, None)

    
    # Element row3 uses Python identifier row3
    __row3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'row3'), 'row3', '__httpeuclid_esa_orgschemabasdtd_matrixDouble3x3_row3', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 123, 3), )

    
    row3 = property(__row3.value, __row3.set, None, None)

    _ElementMap.update({
        __row1.name() : __row1,
        __row2.name() : __row2,
        __row3.name() : __row3
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'matrixDouble3x3', matrixDouble3x3)


# Complex type {http://euclid.esa.org/schema/bas/dtd}matrixDouble6x6 with content type ELEMENT_ONLY
class matrixDouble6x6 (pyxb.binding.basis.complexTypeDefinition):
    """A 6x6 double matrix"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'matrixDouble6x6')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 126, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element row1 uses Python identifier row1
    __row1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'row1'), 'row1', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 131, 3), )

    
    row1 = property(__row1.value, __row1.set, None, None)

    
    # Element row2 uses Python identifier row2
    __row2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'row2'), 'row2', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 132, 3), )

    
    row2 = property(__row2.value, __row2.set, None, None)

    
    # Element row3 uses Python identifier row3
    __row3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'row3'), 'row3', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row3', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 133, 3), )

    
    row3 = property(__row3.value, __row3.set, None, None)

    
    # Element row4 uses Python identifier row4
    __row4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'row4'), 'row4', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row4', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 134, 3), )

    
    row4 = property(__row4.value, __row4.set, None, None)

    
    # Element row5 uses Python identifier row5
    __row5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'row5'), 'row5', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row5', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 135, 3), )

    
    row5 = property(__row5.value, __row5.set, None, None)

    
    # Element row6 uses Python identifier row6
    __row6 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'row6'), 'row6', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row6', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 136, 3), )

    
    row6 = property(__row6.value, __row6.set, None, None)

    _ElementMap.update({
        __row1.name() : __row1,
        __row2.name() : __row2,
        __row3.name() : __row3,
        __row4.name() : __row4,
        __row5.name() : __row5,
        __row6.name() : __row6
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'matrixDouble6x6', matrixDouble6x6)


# Complex type {http://euclid.esa.org/schema/bas/dtd}doubleUnit with content type ELEMENT_ONLY
class doubleUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://euclid.esa.org/schema/bas/dtd}doubleUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'doubleUnit')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 269, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasdtd_doubleUnit_Value', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 271, 3), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabasdtd_doubleUnit_Unit', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 272, 3), )

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value,
        __Unit.name() : __Unit
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'doubleUnit', doubleUnit)


# Complex type {http://euclid.esa.org/schema/bas/dtd}curve2Type with content type ELEMENT_ONLY
class curve2Type (pyxb.binding.basis.complexTypeDefinition):
    """A curve in 2-D space, defined by its end points and a shape attribute (default: line or great circle)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'curve2Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 240, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element P1 uses Python identifier P1
    __P1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'P1'), 'P1', '__httpeuclid_esa_orgschemabasdtd_curve2Type_P1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 245, 3), )

    
    P1 = property(__P1.value, __P1.set, None, None)

    
    # Element P2 uses Python identifier P2
    __P2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'P2'), 'P2', '__httpeuclid_esa_orgschemabasdtd_curve2Type_P2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 246, 3), )

    
    P2 = property(__P2.value, __P2.set, None, None)

    
    # Attribute CurveShape uses Python identifier CurveShape
    __CurveShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CurveShape'), 'CurveShape', '__httpeuclid_esa_orgschemabasdtd_curve2Type_CurveShape', curveShape)
    __CurveShape._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 248, 2)
    __CurveShape._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 248, 2)
    
    CurveShape = property(__CurveShape.value, __CurveShape.set, None, None)

    _ElementMap.update({
        __P1.name() : __P1,
        __P2.name() : __P2
    })
    _AttributeMap.update({
        __CurveShape.name() : __CurveShape
    })
Namespace.addCategoryObject('typeBinding', u'curve2Type', curve2Type)


# Complex type {http://euclid.esa.org/schema/bas/dtd}curve3Type with content type ELEMENT_ONLY
class curve3Type (pyxb.binding.basis.complexTypeDefinition):
    """A curve in 3-D space, defined by its end points and a shape attribute (default: line or great circle)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'curve3Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 250, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element P1 uses Python identifier P1
    __P1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'P1'), 'P1', '__httpeuclid_esa_orgschemabasdtd_curve3Type_P1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 255, 3), )

    
    P1 = property(__P1.value, __P1.set, None, None)

    
    # Element P2 uses Python identifier P2
    __P2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'P2'), 'P2', '__httpeuclid_esa_orgschemabasdtd_curve3Type_P2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 256, 3), )

    
    P2 = property(__P2.value, __P2.set, None, None)

    
    # Attribute CurveShape uses Python identifier CurveShape
    __CurveShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CurveShape'), 'CurveShape', '__httpeuclid_esa_orgschemabasdtd_curve3Type_CurveShape', curveShape)
    __CurveShape._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 258, 2)
    __CurveShape._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 258, 2)
    
    CurveShape = property(__CurveShape.value, __CurveShape.set, None, None)

    _ElementMap.update({
        __P1.name() : __P1,
        __P2.name() : __P2
    })
    _AttributeMap.update({
        __CurveShape.name() : __CurveShape
    })
Namespace.addCategoryObject('typeBinding', u'curve3Type', curve3Type)


# Complex type {http://euclid.esa.org/schema/bas/dtd}array2D with content type ELEMENT_ONLY
class array2D (pyxb.binding.basis.complexTypeDefinition):
    """A 2D array with X axis (specific unit), Y axis (specific unit), listOf2Double, optionnally size of the array is provided. This structure is used for describing Mission parameter database."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'array2D')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 157, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SizeOfArray uses Python identifier SizeOfArray
    __SizeOfArray = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SizeOfArray'), 'SizeOfArray', '__httpeuclid_esa_orgschemabasdtd_array2D_SizeOfArray', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 162, 3), )

    
    SizeOfArray = property(__SizeOfArray.value, __SizeOfArray.set, None, None)

    
    # Element PairedValues uses Python identifier PairedValues
    __PairedValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PairedValues'), 'PairedValues', '__httpeuclid_esa_orgschemabasdtd_array2D_PairedValues', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 163, 3), )

    
    PairedValues = property(__PairedValues.value, __PairedValues.set, None, None)

    
    # Attribute Xunit uses Python identifier Xunit
    __Xunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Xunit'), 'Xunit', '__httpeuclid_esa_orgschemabasdtd_array2D_Xunit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __Xunit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 165, 2)
    __Xunit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 165, 2)
    
    Xunit = property(__Xunit.value, __Xunit.set, None, None)

    
    # Attribute Yunit uses Python identifier Yunit
    __Yunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Yunit'), 'Yunit', '__httpeuclid_esa_orgschemabasdtd_array2D_Yunit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __Yunit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 166, 2)
    __Yunit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 166, 2)
    
    Yunit = property(__Yunit.value, __Yunit.set, None, None)

    _ElementMap.update({
        __SizeOfArray.name() : __SizeOfArray,
        __PairedValues.name() : __PairedValues
    })
    _AttributeMap.update({
        __Xunit.name() : __Xunit,
        __Yunit.name() : __Yunit
    })
Namespace.addCategoryObject('typeBinding', u'array2D', array2D)


# Complex type {http://euclid.esa.org/schema/bas/dtd}array3D with content type ELEMENT_ONLY
class array3D (pyxb.binding.basis.complexTypeDefinition):
    """A 3D array with X axis (specific unit), Y axis (specific unit), Z axis (specific unit) listOf3Double, optionnally size of the array is provided. This structure is used for describing Mission parameter database."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'array3D')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 168, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SizeOfArray uses Python identifier SizeOfArray
    __SizeOfArray = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SizeOfArray'), 'SizeOfArray', '__httpeuclid_esa_orgschemabasdtd_array3D_SizeOfArray', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 173, 3), )

    
    SizeOfArray = property(__SizeOfArray.value, __SizeOfArray.set, None, None)

    
    # Element TripletValues uses Python identifier TripletValues
    __TripletValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TripletValues'), 'TripletValues', '__httpeuclid_esa_orgschemabasdtd_array3D_TripletValues', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 174, 3), )

    
    TripletValues = property(__TripletValues.value, __TripletValues.set, None, None)

    
    # Attribute Xunit uses Python identifier Xunit
    __Xunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Xunit'), 'Xunit', '__httpeuclid_esa_orgschemabasdtd_array3D_Xunit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __Xunit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 176, 2)
    __Xunit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 176, 2)
    
    Xunit = property(__Xunit.value, __Xunit.set, None, None)

    
    # Attribute Yunit uses Python identifier Yunit
    __Yunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Yunit'), 'Yunit', '__httpeuclid_esa_orgschemabasdtd_array3D_Yunit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __Yunit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 177, 2)
    __Yunit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 177, 2)
    
    Yunit = property(__Yunit.value, __Yunit.set, None, None)

    
    # Attribute Zunit uses Python identifier Zunit
    __Zunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Zunit'), 'Zunit', '__httpeuclid_esa_orgschemabasdtd_array3D_Zunit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __Zunit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 178, 2)
    __Zunit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 178, 2)
    
    Zunit = property(__Zunit.value, __Zunit.set, None, None)

    _ElementMap.update({
        __SizeOfArray.name() : __SizeOfArray,
        __TripletValues.name() : __TripletValues
    })
    _AttributeMap.update({
        __Xunit.name() : __Xunit,
        __Yunit.name() : __Yunit,
        __Zunit.name() : __Zunit
    })
Namespace.addCategoryObject('typeBinding', u'array3D', array3D)


# Complex type {http://euclid.esa.org/schema/bas/dtd}double1Type with content type SIMPLE
class double1Type (pyxb.binding.basis.complexTypeDefinition):
    """A double with single unit attribute that could be any of the standard unit defined in bas/."""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double1Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 180, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpeuclid_esa_orgschemabasdtd_double1Type_unit', _ImportedBinding_euclid_dm__utd.unit)
    __unit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 186, 4)
    __unit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 186, 4)
    
    unit = property(__unit.value, __unit.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unit.name() : __unit
    })
Namespace.addCategoryObject('typeBinding', u'double1Type', double1Type)


# Complex type {http://euclid.esa.org/schema/bas/dtd}double2Type with content type ELEMENT_ONLY
class double2Type (pyxb.binding.basis.complexTypeDefinition):
    """A vector of 2 doubles ; components are separated.  Each component of the vector should have the same unit. This unit could be a velocity unit, time unit, position unit, angle unit, spectral unit depending on the semantics of the parameter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double2Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 190, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element C1 uses Python identifier C1
    __C1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'C1'), 'C1', '__httpeuclid_esa_orgschemabasdtd_double2Type_C1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 195, 3), )

    
    C1 = property(__C1.value, __C1.set, None, None)

    
    # Element C2 uses Python identifier C2
    __C2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'C2'), 'C2', '__httpeuclid_esa_orgschemabasdtd_double2Type_C2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 196, 3), )

    
    C2 = property(__C2.value, __C2.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasdtd_double2Type_CoordUnit', _ImportedBinding_euclid_dm__utd.unit)
    __CoordUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 198, 2)
    __CoordUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 198, 2)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    _ElementMap.update({
        __C1.name() : __C1,
        __C2.name() : __C2
    })
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit
    })
Namespace.addCategoryObject('typeBinding', u'double2Type', double2Type)


# Complex type {http://euclid.esa.org/schema/bas/dtd}double3Type with content type ELEMENT_ONLY
class double3Type (pyxb.binding.basis.complexTypeDefinition):
    """A vector of 3 doubles with separated components. Each component of the vector should have the same unit. This unit could be a velocity unit, time unit, position unit, angle unit, spectral unit depending on the semantics of the parameter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double3Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 200, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element C1 uses Python identifier C1
    __C1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'C1'), 'C1', '__httpeuclid_esa_orgschemabasdtd_double3Type_C1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 205, 3), )

    
    C1 = property(__C1.value, __C1.set, None, None)

    
    # Element C2 uses Python identifier C2
    __C2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'C2'), 'C2', '__httpeuclid_esa_orgschemabasdtd_double3Type_C2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 206, 3), )

    
    C2 = property(__C2.value, __C2.set, None, None)

    
    # Element C3 uses Python identifier C3
    __C3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'C3'), 'C3', '__httpeuclid_esa_orgschemabasdtd_double3Type_C3', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 207, 3), )

    
    C3 = property(__C3.value, __C3.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasdtd_double3Type_CoordUnit', _ImportedBinding_euclid_dm__utd.unit)
    __CoordUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 209, 2)
    __CoordUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 209, 2)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    _ElementMap.update({
        __C1.name() : __C1,
        __C2.name() : __C2,
        __C3.name() : __C3
    })
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit
    })
Namespace.addCategoryObject('typeBinding', u'double3Type', double3Type)


# Complex type {http://euclid.esa.org/schema/bas/dtd}double4Type with content type ELEMENT_ONLY
class double4Type (pyxb.binding.basis.complexTypeDefinition):
    """A vector of 4 doubles (2x2 matrix). Each component of the vector should have the same unit. This unit could be a velocity unit, time unit, position unit, angle unit, spectral unit depending on the semantics of the parameter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double4Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 211, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element M11 uses Python identifier M11
    __M11 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M11'), 'M11', '__httpeuclid_esa_orgschemabasdtd_double4Type_M11', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 216, 3), )

    
    M11 = property(__M11.value, __M11.set, None, None)

    
    # Element M12 uses Python identifier M12
    __M12 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M12'), 'M12', '__httpeuclid_esa_orgschemabasdtd_double4Type_M12', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 217, 3), )

    
    M12 = property(__M12.value, __M12.set, None, None)

    
    # Element M21 uses Python identifier M21
    __M21 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M21'), 'M21', '__httpeuclid_esa_orgschemabasdtd_double4Type_M21', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 218, 3), )

    
    M21 = property(__M21.value, __M21.set, None, None)

    
    # Element M22 uses Python identifier M22
    __M22 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M22'), 'M22', '__httpeuclid_esa_orgschemabasdtd_double4Type_M22', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 219, 3), )

    
    M22 = property(__M22.value, __M22.set, None, None)

    
    # Attribute MijUnit uses Python identifier MijUnit
    __MijUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'MijUnit'), 'MijUnit', '__httpeuclid_esa_orgschemabasdtd_double4Type_MijUnit', _ImportedBinding_euclid_dm__utd.unit)
    __MijUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 221, 2)
    __MijUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 221, 2)
    
    MijUnit = property(__MijUnit.value, __MijUnit.set, None, None)

    _ElementMap.update({
        __M11.name() : __M11,
        __M12.name() : __M12,
        __M21.name() : __M21,
        __M22.name() : __M22
    })
    _AttributeMap.update({
        __MijUnit.name() : __MijUnit
    })
Namespace.addCategoryObject('typeBinding', u'double4Type', double4Type)


# Complex type {http://euclid.esa.org/schema/bas/dtd}double9Type with content type ELEMENT_ONLY
class double9Type (pyxb.binding.basis.complexTypeDefinition):
    """A vector of 9 doubles (3x3 matrix). Each component of the vector should have the same unit. This unit could be a velocity unit, time unit, position unit, angle unit, spectral unit depending on the semantics of the parameter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double9Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 223, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element M11 uses Python identifier M11
    __M11 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M11'), 'M11', '__httpeuclid_esa_orgschemabasdtd_double9Type_M11', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 228, 3), )

    
    M11 = property(__M11.value, __M11.set, None, None)

    
    # Element M12 uses Python identifier M12
    __M12 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M12'), 'M12', '__httpeuclid_esa_orgschemabasdtd_double9Type_M12', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 229, 3), )

    
    M12 = property(__M12.value, __M12.set, None, None)

    
    # Element M13 uses Python identifier M13
    __M13 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M13'), 'M13', '__httpeuclid_esa_orgschemabasdtd_double9Type_M13', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 230, 3), )

    
    M13 = property(__M13.value, __M13.set, None, None)

    
    # Element M21 uses Python identifier M21
    __M21 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M21'), 'M21', '__httpeuclid_esa_orgschemabasdtd_double9Type_M21', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 231, 3), )

    
    M21 = property(__M21.value, __M21.set, None, None)

    
    # Element M22 uses Python identifier M22
    __M22 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M22'), 'M22', '__httpeuclid_esa_orgschemabasdtd_double9Type_M22', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 232, 3), )

    
    M22 = property(__M22.value, __M22.set, None, None)

    
    # Element M23 uses Python identifier M23
    __M23 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M23'), 'M23', '__httpeuclid_esa_orgschemabasdtd_double9Type_M23', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 233, 3), )

    
    M23 = property(__M23.value, __M23.set, None, None)

    
    # Element M31 uses Python identifier M31
    __M31 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M31'), 'M31', '__httpeuclid_esa_orgschemabasdtd_double9Type_M31', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 234, 3), )

    
    M31 = property(__M31.value, __M31.set, None, None)

    
    # Element M32 uses Python identifier M32
    __M32 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M32'), 'M32', '__httpeuclid_esa_orgschemabasdtd_double9Type_M32', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 235, 3), )

    
    M32 = property(__M32.value, __M32.set, None, None)

    
    # Element M33 uses Python identifier M33
    __M33 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'M33'), 'M33', '__httpeuclid_esa_orgschemabasdtd_double9Type_M33', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 236, 3), )

    
    M33 = property(__M33.value, __M33.set, None, None)

    
    # Attribute MijUnit uses Python identifier MijUnit
    __MijUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'MijUnit'), 'MijUnit', '__httpeuclid_esa_orgschemabasdtd_double9Type_MijUnit', _ImportedBinding_euclid_dm__utd.unit)
    __MijUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 238, 2)
    __MijUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 238, 2)
    
    MijUnit = property(__MijUnit.value, __MijUnit.set, None, None)

    _ElementMap.update({
        __M11.name() : __M11,
        __M12.name() : __M12,
        __M13.name() : __M13,
        __M21.name() : __M21,
        __M22.name() : __M22,
        __M23.name() : __M23,
        __M31.name() : __M31,
        __M32.name() : __M32,
        __M33.name() : __M33
    })
    _AttributeMap.update({
        __MijUnit.name() : __MijUnit
    })
Namespace.addCategoryObject('typeBinding', u'double9Type', double9Type)




matrixDouble3x3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row1'), listOf3Double, scope=matrixDouble3x3, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 121, 3)))

matrixDouble3x3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row2'), listOf3Double, scope=matrixDouble3x3, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 122, 3)))

matrixDouble3x3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row3'), listOf3Double, scope=matrixDouble3x3, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 123, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3L, max=3L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 120, 2))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(matrixDouble3x3._UseForTag(pyxb.namespace.ExpandedName(None, u'row1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 121, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(matrixDouble3x3._UseForTag(pyxb.namespace.ExpandedName(None, u'row2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 122, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(matrixDouble3x3._UseForTag(pyxb.namespace.ExpandedName(None, u'row3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 123, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
matrixDouble3x3._Automaton = _BuildAutomaton()




matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row1'), listOf6Double, scope=matrixDouble6x6, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 131, 3)))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row2'), listOf6Double, scope=matrixDouble6x6, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 132, 3)))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row3'), listOf6Double, scope=matrixDouble6x6, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 133, 3)))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row4'), listOf6Double, scope=matrixDouble6x6, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 134, 3)))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row5'), listOf6Double, scope=matrixDouble6x6, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 135, 3)))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row6'), listOf6Double, scope=matrixDouble6x6, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 136, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 133, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row4')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 134, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row5')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 135, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row6')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 136, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
matrixDouble6x6._Automaton = _BuildAutomaton_()




doubleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), pyxb.binding.datatypes.double, scope=doubleUnit, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 271, 3)))

doubleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Unit'), _ImportedBinding_euclid_dm__utd.unit, scope=doubleUnit, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 272, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(doubleUnit._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 271, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(doubleUnit._UseForTag(pyxb.namespace.ExpandedName(None, u'Unit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 272, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
doubleUnit._Automaton = _BuildAutomaton_2()




curve2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'P1'), double2Type, scope=curve2Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 245, 3)))

curve2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'P2'), double2Type, scope=curve2Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 246, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(curve2Type._UseForTag(pyxb.namespace.ExpandedName(None, u'P1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 245, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(curve2Type._UseForTag(pyxb.namespace.ExpandedName(None, u'P2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 246, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
curve2Type._Automaton = _BuildAutomaton_3()




curve3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'P1'), double3Type, scope=curve3Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 255, 3)))

curve3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'P2'), double3Type, scope=curve3Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 256, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(curve3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'P1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 255, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(curve3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'P2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 256, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
curve3Type._Automaton = _BuildAutomaton_4()




array2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SizeOfArray'), pyxb.binding.datatypes.long, scope=array2D, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 162, 3)))

array2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PairedValues'), listOf2Double, scope=array2D, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 163, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 162, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(array2D._UseForTag(pyxb.namespace.ExpandedName(None, u'SizeOfArray')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 162, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(array2D._UseForTag(pyxb.namespace.ExpandedName(None, u'PairedValues')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 163, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
array2D._Automaton = _BuildAutomaton_5()




array3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SizeOfArray'), pyxb.binding.datatypes.long, scope=array3D, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 173, 3)))

array3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TripletValues'), listOf3Double, scope=array3D, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 174, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 173, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(array3D._UseForTag(pyxb.namespace.ExpandedName(None, u'SizeOfArray')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 173, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(array3D._UseForTag(pyxb.namespace.ExpandedName(None, u'TripletValues')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 174, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
array3D._Automaton = _BuildAutomaton_6()




double2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C1'), double1Type, scope=double2Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 195, 3)))

double2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C2'), double1Type, scope=double2Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 196, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double2Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 195, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(double2Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 196, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
double2Type._Automaton = _BuildAutomaton_7()




double3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C1'), double1Type, scope=double3Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 205, 3)))

double3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C2'), double1Type, scope=double3Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 206, 3)))

double3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C3'), double1Type, scope=double3Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 207, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 205, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 206, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(double3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 207, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
double3Type._Automaton = _BuildAutomaton_8()




double4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M11'), pyxb.binding.datatypes.double, scope=double4Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 216, 3)))

double4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M12'), pyxb.binding.datatypes.double, scope=double4Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 217, 3)))

double4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M21'), pyxb.binding.datatypes.double, scope=double4Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 218, 3)))

double4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M22'), pyxb.binding.datatypes.double, scope=double4Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 219, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double4Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M11')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 216, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double4Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M12')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 217, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double4Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M21')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 218, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(double4Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M22')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 219, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
double4Type._Automaton = _BuildAutomaton_9()




double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M11'), pyxb.binding.datatypes.double, scope=double9Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 228, 3)))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M12'), pyxb.binding.datatypes.double, scope=double9Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 229, 3)))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M13'), pyxb.binding.datatypes.double, scope=double9Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 230, 3)))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M21'), pyxb.binding.datatypes.double, scope=double9Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 231, 3)))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M22'), pyxb.binding.datatypes.double, scope=double9Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 232, 3)))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M23'), pyxb.binding.datatypes.double, scope=double9Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 233, 3)))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M31'), pyxb.binding.datatypes.double, scope=double9Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 234, 3)))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M32'), pyxb.binding.datatypes.double, scope=double9Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 235, 3)))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M33'), pyxb.binding.datatypes.double, scope=double9Type, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 236, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M11')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 228, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M12')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 229, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M13')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 230, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M21')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 231, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M22')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 232, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M23')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 233, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M31')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 234, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M32')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 235, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M33')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/dtd/euc-test-dtd.xsd', 236, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
double9Type._Automaton = _BuildAutomaton_10()

