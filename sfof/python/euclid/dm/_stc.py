# /home/sartor/pymodule/euclid/dm/_stc.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c85a7aef9dd35afb45dde402fdc86e2ca92a56ad
# Generated 2014-07-24 16:26:39.932475 by PyXB version 1.2.3
# Namespace http://euclid.esa.org/schema/bas/imp/stc [xmlns:stc]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:869ae486-133e-11e4-88d8-90b11c83965f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import euclid.dm._dtd as _ImportedBinding_euclid_dm__dtd
import euclid.dm._utd as _ImportedBinding_euclid_dm__utd

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/imp/stc', create_if_missing=True)
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


# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}hsOffsetType
class hsOffsetType (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hsOffsetType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 365, 1)
    _Documentation = None
hsOffsetType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=hsOffsetType, value=pyxb.binding.datatypes.double(1.0))
hsOffsetType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=hsOffsetType, value=pyxb.binding.datatypes.double(-1.0))
hsOffsetType._InitializeFacetMap(hsOffsetType._CF_maxInclusive,
   hsOffsetType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'hsOffsetType', hsOffsetType)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}redshiftFrameValue
class redshiftFrameValue (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'redshiftFrameValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 488, 1)
    _Documentation = None
redshiftFrameValue._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=redshiftFrameValue, enum_prefix=None)
redshiftFrameValue.VELOCITY = redshiftFrameValue._CF_enumeration.addEnumeration(unicode_value=u'VELOCITY', tag=u'VELOCITY')
redshiftFrameValue.REDSHIFT = redshiftFrameValue._CF_enumeration.addEnumeration(unicode_value=u'REDSHIFT', tag=u'REDSHIFT')
redshiftFrameValue._InitializeFacetMap(redshiftFrameValue._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'redshiftFrameValue', redshiftFrameValue)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}dopplerDefinition
class dopplerDefinition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The Doppler definition used: optical, radio, or pseudo-relativistic (i.e., how is a redshift converted to a velocity); the most common is optical, except when the reference is LSR (usually radio)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dopplerDefinition')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 507, 1)
    _Documentation = u'The Doppler definition used: optical, radio, or pseudo-relativistic (i.e., how is a redshift converted to a velocity); the most common is optical, except when the reference is LSR (usually radio)'
dopplerDefinition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dopplerDefinition, enum_prefix=None)
dopplerDefinition.OPTICAL = dopplerDefinition._CF_enumeration.addEnumeration(unicode_value=u'OPTICAL', tag=u'OPTICAL')
dopplerDefinition.RADIO = dopplerDefinition._CF_enumeration.addEnumeration(unicode_value=u'RADIO', tag=u'RADIO')
dopplerDefinition.RELATIVISTIC = dopplerDefinition._CF_enumeration.addEnumeration(unicode_value=u'RELATIVISTIC', tag=u'RELATIVISTIC')
dopplerDefinition._InitializeFacetMap(dopplerDefinition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dopplerDefinition', dopplerDefinition)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}referencePosition
class referencePosition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The list of referencePosition is derived from STC metadata Linear String Implementation V0.10. Either a "known place" such as geocenter or barycenter, or a position defined in a known coordinate system. TOPOCENTER : Location of the observer/telescope, BARYCENTER : Barycenter of the solar system HELIOCENTER : Center of the sun GEOCENTER : Center of the earth GALACTIC_CENTER : Center of the Galaxy LOCAL_GROUP_CENTER : Center of the Local Group MOON : Center of the Moon EMBARYCENTER : Barycenter of the Earth-Moon system MERCURY :  VENUS :  MARS : JUPITER : SATURN : URANUS : NEPTUNE : PLUTO : UNKNOWNRefPos : Unknown origin ; the producer is responsible for assigning a default"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'referencePosition')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 518, 1)
    _Documentation = u'The list of referencePosition is derived from STC metadata Linear String Implementation V0.10. Either a "known place" such as geocenter or barycenter, or a position defined in a known coordinate system. TOPOCENTER : Location of the observer/telescope, BARYCENTER : Barycenter of the solar system HELIOCENTER : Center of the sun GEOCENTER : Center of the earth GALACTIC_CENTER : Center of the Galaxy LOCAL_GROUP_CENTER : Center of the Local Group MOON : Center of the Moon EMBARYCENTER : Barycenter of the Earth-Moon system MERCURY :  VENUS :  MARS : JUPITER : SATURN : URANUS : NEPTUNE : PLUTO : UNKNOWNRefPos : Unknown origin ; the producer is responsible for assigning a default'
referencePosition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=referencePosition, enum_prefix=None)
referencePosition.TOPOCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'TOPOCENTER', tag=u'TOPOCENTER')
referencePosition.BARYCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'BARYCENTER', tag=u'BARYCENTER')
referencePosition.HELIOCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'HELIOCENTER', tag=u'HELIOCENTER')
referencePosition.GEOCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'GEOCENTER', tag=u'GEOCENTER')
referencePosition.GALACTIC_CENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'GALACTIC_CENTER', tag=u'GALACTIC_CENTER')
referencePosition.LOCAL_GROUP_CENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'LOCAL_GROUP_CENTER', tag=u'LOCAL_GROUP_CENTER')
referencePosition.MOON = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'MOON', tag=u'MOON')
referencePosition.EMBARYCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'EMBARYCENTER', tag=u'EMBARYCENTER')
referencePosition.MERCURY = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'MERCURY', tag=u'MERCURY')
referencePosition.VENUS = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'VENUS', tag=u'VENUS')
referencePosition.MARS = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'MARS', tag=u'MARS')
referencePosition.JUPITER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'JUPITER', tag=u'JUPITER')
referencePosition.SATURN = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'SATURN', tag=u'SATURN')
referencePosition.URANUS = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'URANUS', tag=u'URANUS')
referencePosition.NEPTUNE = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'NEPTUNE', tag=u'NEPTUNE')
referencePosition.PLUTO = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'PLUTO', tag=u'PLUTO')
referencePosition.UNKNOWNRefPos = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWNRefPos', tag=u'UNKNOWNRefPos')
referencePosition._InitializeFacetMap(referencePosition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'referencePosition', referencePosition)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}coordRefFrame
class coordRefFrame (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The different types of CoordRefFrame come from the list in STC ivoa V1.3. Sub list defined in 'STC-S metadata linear string implementation' is described here. Take care that for ICRS type : no equinox is required, FK[45] type  needs an equinox and  geodeticType refers to IAU 1976 reference spheroid . FK4  needs a Besselian epoch,  FK5 needs a Julian epoch, ECLIPTIC Ecliptic coordinates  shall be assumed to have an equinox of J2000 with respect to ICRS (to conform with common abuse, "J2000" and "FK5" will both be interpreted as "FK5 J2000" ; "B1950" and "FK4" will be interpreted  as "FK4 B1950",  GALACTIC : Galactic coordinates; first system, GALACTIC_II : Galactic coordinates; second system, SUPER_GALACTIC : SuperGalactic coordinates, GEO_C : The Geocentric (co-rotating) reference frame, GEO_D :  The Geodetic reference frame; semi-major axis and inverse flattening may be provided to define the reference spheroid; the default is the IAU 1976 reference spheroid, UNKNOWNFrame :  Unknown space reference frame; the producer is responsible for assigning a default"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coordRefFrame')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 563, 1)
    _Documentation = u'The different types of CoordRefFrame come from the list in STC ivoa V1.3. Sub list defined in \'STC-S metadata linear string implementation\' is described here. Take care that for ICRS type : no equinox is required, FK[45] type  needs an equinox and  geodeticType refers to IAU 1976 reference spheroid . FK4  needs a Besselian epoch,  FK5 needs a Julian epoch, ECLIPTIC Ecliptic coordinates  shall be assumed to have an equinox of J2000 with respect to ICRS (to conform with common abuse, "J2000" and "FK5" will both be interpreted as "FK5 J2000" ; "B1950" and "FK4" will be interpreted  as "FK4 B1950",  GALACTIC : Galactic coordinates; first system, GALACTIC_II : Galactic coordinates; second system, SUPER_GALACTIC : SuperGalactic coordinates, GEO_C : The Geocentric (co-rotating) reference frame, GEO_D :  The Geodetic reference frame; semi-major axis and inverse flattening may be provided to define the reference spheroid; the default is the IAU 1976 reference spheroid, UNKNOWNFrame :  Unknown space reference frame; the producer is responsible for assigning a default'
coordRefFrame._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=coordRefFrame, enum_prefix=None)
coordRefFrame.ICRS = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'ICRS', tag=u'ICRS')
coordRefFrame.FK4 = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'FK4', tag=u'FK4')
coordRefFrame.FK5 = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'FK5', tag=u'FK5')
coordRefFrame.J2000 = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'J2000', tag=u'J2000')
coordRefFrame.B1950 = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'B1950', tag=u'B1950')
coordRefFrame.ECLIPTIC = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'ECLIPTIC', tag=u'ECLIPTIC')
coordRefFrame.GALACTIC_I = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'GALACTIC_I', tag=u'GALACTIC_I')
coordRefFrame.GALACTIC_II = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'GALACTIC_II', tag=u'GALACTIC_II')
coordRefFrame.SUPER_GALACTIC = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'SUPER_GALACTIC', tag=u'SUPER_GALACTIC')
coordRefFrame.GEO_C = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'GEO_C', tag=u'GEO_C')
coordRefFrame.GEO_D = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'GEO_D', tag=u'GEO_D')
coordRefFrame.UNKNOWNFrame = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWNFrame', tag=u'UNKNOWNFrame')
coordRefFrame._InitializeFacetMap(coordRefFrame._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'coordRefFrame', coordRefFrame)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}coordNaxesValue
class coordNaxesValue (pyxb.binding.datatypes.short):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coordNaxesValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 583, 1)
    _Documentation = None
coordNaxesValue._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=coordNaxesValue, value=pyxb.binding.datatypes.short(3))
coordNaxesValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=coordNaxesValue, value=pyxb.binding.datatypes.short(1))
coordNaxesValue._InitializeFacetMap(coordNaxesValue._CF_maxInclusive,
   coordNaxesValue._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'coordNaxesValue', coordNaxesValue)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}handednessValue
class handednessValue (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'handednessValue')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 589, 1)
    _Documentation = None
handednessValue._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=handednessValue, enum_prefix=None)
handednessValue.left = handednessValue._CF_enumeration.addEnumeration(unicode_value=u'left', tag=u'left')
handednessValue.right = handednessValue._CF_enumeration.addEnumeration(unicode_value=u'right', tag=u'right')
handednessValue._InitializeFacetMap(handednessValue._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'handednessValue', handednessValue)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}projection
class projection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The spherical-to-cartesian or cartesian-to-cartesian projection to be used; c-to-c projections are marked as such, all others are to be interpreted as s-to-c"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'projection')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 630, 1)
    _Documentation = u'The spherical-to-cartesian or cartesian-to-cartesian projection to be used; c-to-c projections are marked as such, all others are to be interpreted as s-to-c'
projection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=projection, enum_prefix=None)
projection.emptyString = projection._CF_enumeration.addEnumeration(unicode_value=u'', tag='emptyString')
projection.LOG = projection._CF_enumeration.addEnumeration(unicode_value=u'LOG', tag=u'LOG')
projection.TAN = projection._CF_enumeration.addEnumeration(unicode_value=u'TAN', tag=u'TAN')
projection.SIN = projection._CF_enumeration.addEnumeration(unicode_value=u'SIN', tag=u'SIN')
projection.STG = projection._CF_enumeration.addEnumeration(unicode_value=u'STG', tag=u'STG')
projection.ARC = projection._CF_enumeration.addEnumeration(unicode_value=u'ARC', tag=u'ARC')
projection.ZEA = projection._CF_enumeration.addEnumeration(unicode_value=u'ZEA', tag=u'ZEA')
projection.AIR = projection._CF_enumeration.addEnumeration(unicode_value=u'AIR', tag=u'AIR')
projection.CEA = projection._CF_enumeration.addEnumeration(unicode_value=u'CEA', tag=u'CEA')
projection.CAR = projection._CF_enumeration.addEnumeration(unicode_value=u'CAR', tag=u'CAR')
projection.MER = projection._CF_enumeration.addEnumeration(unicode_value=u'MER', tag=u'MER')
projection.SFL = projection._CF_enumeration.addEnumeration(unicode_value=u'SFL', tag=u'SFL')
projection.PAR = projection._CF_enumeration.addEnumeration(unicode_value=u'PAR', tag=u'PAR')
projection.MOL = projection._CF_enumeration.addEnumeration(unicode_value=u'MOL', tag=u'MOL')
projection.AIT = projection._CF_enumeration.addEnumeration(unicode_value=u'AIT', tag=u'AIT')
projection.COE = projection._CF_enumeration.addEnumeration(unicode_value=u'COE', tag=u'COE')
projection.COD = projection._CF_enumeration.addEnumeration(unicode_value=u'COD', tag=u'COD')
projection.COO = projection._CF_enumeration.addEnumeration(unicode_value=u'COO', tag=u'COO')
projection.BON = projection._CF_enumeration.addEnumeration(unicode_value=u'BON', tag=u'BON')
projection.PCO = projection._CF_enumeration.addEnumeration(unicode_value=u'PCO', tag=u'PCO')
projection.TSC = projection._CF_enumeration.addEnumeration(unicode_value=u'TSC', tag=u'TSC')
projection.CSC = projection._CF_enumeration.addEnumeration(unicode_value=u'CSC', tag=u'CSC')
projection.QSC = projection._CF_enumeration.addEnumeration(unicode_value=u'QSC', tag=u'QSC')
projection._InitializeFacetMap(projection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'projection', projection)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}timeScale
class timeScale (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This type refers to : timeScaleType from stc IVOA.The actual time scale is derived from Representations of Time Coordinates in FITS Time and Relative Dimension in Space (V0.93) Astronomy and Astrophysics manuscript no. WCSPaperV0.93  ESO 2012 March 21, 2012. The original XML schema is derived from stc-v1.30 IVOA. TT Terrestrial Time; the basis for ephemerides, TDT Obsolete synonym for TT ET Ephemeris Time; predecessor of, and continuous with, TT TDB Barycentric Dynamic Time:the independent variable in planetay ephemerides; time at the solar system barycenter synchronous with TT on an annual basis; sometimes called TEB Barycentric Ephemeris Time: time at the solar system barycenter synchronous with TT on an annual basis; a deprecated synonym of TDB.TCG Terrestrial Coordinate Time TAI International Atomic Time; runs 32.184 s behind TT  IAT Synonym for TAI UTC Coordinated Universal Time; currently (2006) runs 33 leapseconds behind TAI GPS Global Positioning System's time scale; runs 19 s behind TAI, 51.184 s behind TT LST Local Siderial Time; only for ground-based observations; note that the second is shorter GMST Greenwich Mean Siderial Time; only for ground-based observations; note that the second is shorter LOCAL Only to be used for simulations in conjunction with a relocatable spatial frame. The enumeration comes from paragraph 5-1 of STC-S metadata linear string implementation V0.10."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeScale')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 754, 1)
    _Documentation = u"This type refers to : timeScaleType from stc IVOA.The actual time scale is derived from Representations of Time Coordinates in FITS Time and Relative Dimension in Space (V0.93) Astronomy and Astrophysics manuscript no. WCSPaperV0.93  ESO 2012 March 21, 2012. The original XML schema is derived from stc-v1.30 IVOA. TT Terrestrial Time; the basis for ephemerides, TDT Obsolete synonym for TT ET Ephemeris Time; predecessor of, and continuous with, TT TDB Barycentric Dynamic Time:the independent variable in planetay ephemerides; time at the solar system barycenter synchronous with TT on an annual basis; sometimes called TEB Barycentric Ephemeris Time: time at the solar system barycenter synchronous with TT on an annual basis; a deprecated synonym of TDB.TCG Terrestrial Coordinate Time TAI International Atomic Time; runs 32.184 s behind TT  IAT Synonym for TAI UTC Coordinated Universal Time; currently (2006) runs 33 leapseconds behind TAI GPS Global Positioning System's time scale; runs 19 s behind TAI, 51.184 s behind TT LST Local Siderial Time; only for ground-based observations; note that the second is shorter GMST Greenwich Mean Siderial Time; only for ground-based observations; note that the second is shorter LOCAL Only to be used for simulations in conjunction with a relocatable spatial frame. The enumeration comes from paragraph 5-1 of STC-S metadata linear string implementation V0.10."
timeScale._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=timeScale, enum_prefix=None)
timeScale.TT = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TT', tag=u'TT')
timeScale.TDT = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TDT', tag=u'TDT')
timeScale.ET = timeScale._CF_enumeration.addEnumeration(unicode_value=u'ET', tag=u'ET')
timeScale.TDB = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TDB', tag=u'TDB')
timeScale.TEB = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TEB', tag=u'TEB')
timeScale.TCG = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TCG', tag=u'TCG')
timeScale.TCB = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TCB', tag=u'TCB')
timeScale.TAI = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TAI', tag=u'TAI')
timeScale.IAT = timeScale._CF_enumeration.addEnumeration(unicode_value=u'IAT', tag=u'IAT')
timeScale.UTC = timeScale._CF_enumeration.addEnumeration(unicode_value=u'UTC', tag=u'UTC')
timeScale.GPS = timeScale._CF_enumeration.addEnumeration(unicode_value=u'GPS', tag=u'GPS')
timeScale.LST = timeScale._CF_enumeration.addEnumeration(unicode_value=u'LST', tag=u'LST')
timeScale.GMST = timeScale._CF_enumeration.addEnumeration(unicode_value=u'GMST', tag=u'GMST')
timeScale.LOCAL = timeScale._CF_enumeration.addEnumeration(unicode_value=u'LOCAL', tag=u'LOCAL')
timeScale._InitializeFacetMap(timeScale._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'timeScale', timeScale)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}secDateTime
class secDateTime (pyxb.binding.datatypes.dateTime):

    """A date-time value with a precision of one second. This date-time format allows the definition of TAI date and UTC date. date-time value is restricted to the yyyy-mm-ddThh:mm:ss[Z] pattern and excluding thus : a fractional seconds definition (value has a precision of one second), a TimeZone definition."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'secDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 824, 1)
    _Documentation = u'A date-time value with a precision of one second. This date-time format allows the definition of TAI date and UTC date. date-time value is restricted to the yyyy-mm-ddThh:mm:ss[Z] pattern and excluding thus : a fractional seconds definition (value has a precision of one second), a TimeZone definition.'
secDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
secDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ?')
secDateTime._InitializeFacetMap(secDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'secDateTime', secDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}millisecDateTime
class millisecDateTime (pyxb.binding.datatypes.dateTime):

    """A date-time value with a precision of one millisecond. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sss[Z] pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'millisecDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 835, 1)
    _Documentation = u'A date-time value with a precision of one millisecond. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sss[Z] pattern'
millisecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
millisecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\dZ?')
millisecDateTime._InitializeFacetMap(millisecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'millisecDateTime', millisecDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}microsecDateTime
class microsecDateTime (pyxb.binding.datatypes.dateTime):

    """A date-time value with a precision of one microsecond. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss[Z] pattern."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'microsecDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 846, 1)
    _Documentation = u'A date-time value with a precision of one microsecond. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss[Z] pattern.'
microsecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
microsecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d\\d\\d\\dZ?')
microsecDateTime._InitializeFacetMap(microsecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'microsecDateTime', microsecDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}dateTime
class dateTime (pyxb.binding.datatypes.dateTime):

    """A date-time value. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss[.sss][Z] pattern and excluding thus a TimeZone definition."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 857, 1)
    _Documentation = u'A date-time value. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss[.sss][Z] pattern and excluding thus a TimeZone definition.'
dateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
dateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d(\\.\\d+)?Z?')
dateTime._InitializeFacetMap(dateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'dateTime', dateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}TAIMicrosecDateTime
class TAIMicrosecDateTime (pyxb.binding.datatypes.dateTime):

    """An non UTC date-time value with a precision of one microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TAIMicrosecDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 868, 1)
    _Documentation = u'An non UTC date-time value with a precision of one microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss pattern'
TAIMicrosecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
TAIMicrosecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d\\d\\d\\d')
TAIMicrosecDateTime._InitializeFacetMap(TAIMicrosecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'TAIMicrosecDateTime', TAIMicrosecDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}TAIMillisecsecDateTime
class TAIMillisecsecDateTime (pyxb.binding.datatypes.dateTime):

    """An non UTC date-time value with a precision of one millisecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TAIMillisecsecDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 878, 1)
    _Documentation = u'An non UTC date-time value with a precision of one millisecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss pattern'
TAIMillisecsecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
TAIMillisecsecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d')
TAIMillisecsecDateTime._InitializeFacetMap(TAIMillisecsecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'TAIMillisecsecDateTime', TAIMillisecsecDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}UTCDateTime
class UTCDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value. date-time value restricted to the
						yyyy-mm-ddThh:mm:ss(.sss) Z pattern. Z character is mandatory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 899, 1)
    _Documentation = u'An UTC date-time value. date-time value restricted to the\n\t\t\t\t\t\tyyyy-mm-ddThh:mm:ss(.sss) Z pattern. Z character is mandatory.'
UTCDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d(\\.\\d+)?Z')
UTCDateTime._InitializeFacetMap(UTCDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCDateTime', UTCDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}UTCMicrosecDateTime
class UTCMicrosecDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value with a precision of one microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssssZ pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCMicrosecDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 921, 1)
    _Documentation = u'An UTC date-time value with a precision of one microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssssZ pattern'
UTCMicrosecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCMicrosecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d.\\d\\d\\d\\d\\d\\d?Z')
UTCMicrosecDateTime._InitializeFacetMap(UTCMicrosecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCMicrosecDateTime', UTCMicrosecDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}UTCMillisecDateTime
class UTCMillisecDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value with a precision of one millisecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssZ pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCMillisecDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 942, 1)
    _Documentation = u'An UTC date-time value with a precision of one millisecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssZ pattern'
UTCMillisecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCMillisecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d?Z')
UTCMillisecDateTime._InitializeFacetMap(UTCMillisecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCMillisecDateTime', UTCMillisecDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}UTCSecDateTime
class UTCSecDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value with a precision of one second. date-time value restricted to the yyyy-mm-ddThh:mm:ssZ pattern and excluding thus :a fractional seconds definition (value has a precision of one second), a TimeZone definition. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCSecDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 963, 1)
    _Documentation = u'An UTC date-time value with a precision of one second. date-time value restricted to the yyyy-mm-ddThh:mm:ssZ pattern and excluding thus :a fractional seconds definition (value has a precision of one second), a TimeZone definition. '
UTCSecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCSecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d?Z')
UTCSecDateTime._InitializeFacetMap(UTCSecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCSecDateTime', UTCSecDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}UTCTenthMicrosecDateTime
class UTCTenthMicrosecDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value with a precision of one tenth-of-a-microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssssssZ pattern."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCTenthMicrosecDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 994, 1)
    _Documentation = u'An UTC date-time value with a precision of one tenth-of-a-microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssssssZ pattern.'
UTCTenthMicrosecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCTenthMicrosecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d\\d\\d\\d\\d?Z')
UTCTenthMicrosecDateTime._InitializeFacetMap(UTCTenthMicrosecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCTenthMicrosecDateTime', UTCTenthMicrosecDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}nonUTCTenthMicrosecDateTime
class nonUTCTenthMicrosecDateTime (pyxb.binding.datatypes.dateTime):

    """A non UTC (a TAI) date-time value with a precision of one tenth-of-a-microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssssss pattern."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nonUTCTenthMicrosecDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 1005, 1)
    _Documentation = u'A non UTC (a TAI) date-time value with a precision of one tenth-of-a-microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssssss pattern.'
nonUTCTenthMicrosecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
nonUTCTenthMicrosecDateTime._CF_pattern.addPattern(pattern=u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.\\d{7}')
nonUTCTenthMicrosecDateTime._InitializeFacetMap(nonUTCTenthMicrosecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'nonUTCTenthMicrosecDateTime', nonUTCTenthMicrosecDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/bas/imp/stc}secDuration
class secDuration (pyxb.binding.datatypes.string):

    """Duration in seconds. Accuracy is microsec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'secDuration')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 1016, 1)
    _Documentation = u'Duration in seconds. Accuracy is microsec.'
secDuration._CF_pattern = pyxb.binding.facets.CF_pattern()
secDuration._CF_pattern.addPattern(pattern=u'\\d(\\.\\d{0,6})')
secDuration._InitializeFacetMap(secDuration._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'secDuration', secDuration)

# Complex type {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType with content type ELEMENT_ONLY
class coordScalarIntervalType (pyxb.binding.basis.complexTypeDefinition):
    """Scalar coordinate interval type defined by the sequence :  Lower bound of interval, limit included. Upper bound of interval, limit included. Two optional attributes are : Fraction of interval that is occupied by data and frameId."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coordScalarIntervalType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 122, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LoLimit uses Python identifier LoLimit
    __LoLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'LoLimit'), 'LoLimit', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_LoLimit', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3), )

    
    LoLimit = property(__LoLimit.value, __LoLimit.set, None, u'Lower bound of interval.')

    
    # Element HiLimit uses Python identifier HiLimit
    __HiLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'HiLimit'), 'HiLimit', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_HiLimit', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3), )

    
    HiLimit = property(__HiLimit.value, __HiLimit.set, None, u'Upper bound of interval.')

    
    # Attribute lo_include uses Python identifier lo_include
    __lo_include = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lo_include'), 'lo_include', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_lo_include', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    __lo_include._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 138, 2)
    __lo_include._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 138, 2)
    
    lo_include = property(__lo_include.value, __lo_include.set, None, u'Limit to be included, if true lo limit is included.')

    
    # Attribute hi_include uses Python identifier hi_include
    __hi_include = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hi_include'), 'hi_include', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_hi_include', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    __hi_include._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 143, 2)
    __hi_include._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 143, 2)
    
    hi_include = property(__hi_include.value, __hi_include.set, None, u'Limit to be included, if true hi limit is included.')

    
    # Attribute fill_factor uses Python identifier fill_factor
    __fill_factor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fill_factor'), 'fill_factor', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_fill_factor', pyxb.binding.datatypes.float, unicode_default=u'1.0')
    __fill_factor._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 148, 2)
    __fill_factor._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 148, 2)
    
    fill_factor = property(__fill_factor.value, __fill_factor.set, None, u'Fraction of interval that is occupied by data.')

    
    # Attribute FrameId uses Python identifier FrameId
    __FrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'FrameId'), 'FrameId', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_FrameId', pyxb.binding.datatypes.string)
    __FrameId._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 153, 2)
    __FrameId._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 153, 2)
    
    FrameId = property(__FrameId.value, __FrameId.set, None, None)

    _ElementMap.update({
        __LoLimit.name() : __LoLimit,
        __HiLimit.name() : __HiLimit
    })
    _AttributeMap.update({
        __lo_include.name() : __lo_include,
        __hi_include.name() : __hi_include,
        __fill_factor.name() : __fill_factor,
        __FrameId.name() : __FrameId
    })
Namespace.addCategoryObject('typeBinding', u'coordScalarIntervalType', coordScalarIntervalType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}coord2VecIntervalType with content type ELEMENT_ONLY
class coord2VecIntervalType (pyxb.binding.basis.complexTypeDefinition):
    """2-D coordinate interval type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coord2VecIntervalType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 156, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LoLimit2Vec uses Python identifier LoLimit2Vec
    __LoLimit2Vec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'LoLimit2Vec'), 'LoLimit2Vec', '__httpeuclid_esa_orgschemabasimpstc_coord2VecIntervalType_LoLimit2Vec', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 161, 3), )

    
    LoLimit2Vec = property(__LoLimit2Vec.value, __LoLimit2Vec.set, None, None)

    
    # Element HiLimit2Vec uses Python identifier HiLimit2Vec
    __HiLimit2Vec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'HiLimit2Vec'), 'HiLimit2Vec', '__httpeuclid_esa_orgschemabasimpstc_coord2VecIntervalType_HiLimit2Vec', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 162, 3), )

    
    HiLimit2Vec = property(__HiLimit2Vec.value, __HiLimit2Vec.set, None, None)

    
    # Attribute fill_factor uses Python identifier fill_factor
    __fill_factor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fill_factor'), 'fill_factor', '__httpeuclid_esa_orgschemabasimpstc_coord2VecIntervalType_fill_factor', pyxb.binding.datatypes.float, unicode_default=u'1.0')
    __fill_factor._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 164, 2)
    __fill_factor._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 164, 2)
    
    fill_factor = property(__fill_factor.value, __fill_factor.set, None, u'Fraction of interval that is occupied by data')

    
    # Attribute FrameId uses Python identifier FrameId
    __FrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'FrameId'), 'FrameId', '__httpeuclid_esa_orgschemabasimpstc_coord2VecIntervalType_FrameId', pyxb.binding.datatypes.string)
    __FrameId._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 169, 2)
    __FrameId._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 169, 2)
    
    FrameId = property(__FrameId.value, __FrameId.set, None, None)

    _ElementMap.update({
        __LoLimit2Vec.name() : __LoLimit2Vec,
        __HiLimit2Vec.name() : __HiLimit2Vec
    })
    _AttributeMap.update({
        __fill_factor.name() : __fill_factor,
        __FrameId.name() : __FrameId
    })
Namespace.addCategoryObject('typeBinding', u'coord2VecIntervalType', coord2VecIntervalType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}coord3VecIntervalType with content type ELEMENT_ONLY
class coord3VecIntervalType (pyxb.binding.basis.complexTypeDefinition):
    """3-D coordinate interval type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coord3VecIntervalType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 172, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LoLimit3Vec uses Python identifier LoLimit3Vec
    __LoLimit3Vec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'LoLimit3Vec'), 'LoLimit3Vec', '__httpeuclid_esa_orgschemabasimpstc_coord3VecIntervalType_LoLimit3Vec', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 177, 3), )

    
    LoLimit3Vec = property(__LoLimit3Vec.value, __LoLimit3Vec.set, None, None)

    
    # Element HiLimit3Vec uses Python identifier HiLimit3Vec
    __HiLimit3Vec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'HiLimit3Vec'), 'HiLimit3Vec', '__httpeuclid_esa_orgschemabasimpstc_coord3VecIntervalType_HiLimit3Vec', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 178, 3), )

    
    HiLimit3Vec = property(__HiLimit3Vec.value, __HiLimit3Vec.set, None, None)

    
    # Attribute fill_factor uses Python identifier fill_factor
    __fill_factor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fill_factor'), 'fill_factor', '__httpeuclid_esa_orgschemabasimpstc_coord3VecIntervalType_fill_factor', pyxb.binding.datatypes.float, unicode_default=u'1.0')
    __fill_factor._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 180, 2)
    __fill_factor._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 180, 2)
    
    fill_factor = property(__fill_factor.value, __fill_factor.set, None, u'Fraction of interval that is occupied by data')

    
    # Attribute FrameId uses Python identifier FrameId
    __FrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'FrameId'), 'FrameId', '__httpeuclid_esa_orgschemabasimpstc_coord3VecIntervalType_FrameId', pyxb.binding.datatypes.string)
    __FrameId._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 185, 2)
    __FrameId._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 185, 2)
    
    FrameId = property(__FrameId.value, __FrameId.set, None, None)

    _ElementMap.update({
        __LoLimit3Vec.name() : __LoLimit3Vec,
        __HiLimit3Vec.name() : __HiLimit3Vec
    })
    _AttributeMap.update({
        __fill_factor.name() : __fill_factor,
        __FrameId.name() : __FrameId
    })
Namespace.addCategoryObject('typeBinding', u'coord3VecIntervalType', coord3VecIntervalType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}allSkyType with content type EMPTY
class allSkyType (pyxb.binding.basis.complexTypeDefinition):
    """AllSky type: just a shape without any child elements"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'allSkyType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 239, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'allSkyType', allSkyType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}circleType with content type ELEMENT_ONLY
class circleType (pyxb.binding.basis.complexTypeDefinition):
    """Circle shape: center and radius"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'circleType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 245, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Center uses Python identifier Center
    __Center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Center'), 'Center', '__httpeuclid_esa_orgschemabasimpstc_circleType_Center', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 250, 3), )

    
    Center = property(__Center.value, __Center.set, None, u"The coordinates of the circle's center")

    
    # Element Radius uses Python identifier Radius
    __Radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Radius'), 'Radius', '__httpeuclid_esa_orgschemabasimpstc_circleType_Radius', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 255, 3), )

    
    Radius = property(__Radius.value, __Radius.set, None, u'The radius of the circle')

    _ElementMap.update({
        __Center.name() : __Center,
        __Radius.name() : __Radius
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'circleType', circleType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}ellipseType with content type ELEMENT_ONLY
class ellipseType (pyxb.binding.basis.complexTypeDefinition):
    """Ellipse shape: center, semi-major, semi-minor axis and position angle; in spherical coordinates defined as the shape cut out of the sphere by a cone with elliptical cross-section"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ellipseType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 263, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Center uses Python identifier Center
    __Center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Center'), 'Center', '__httpeuclid_esa_orgschemabasimpstc_ellipseType_Center', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 268, 3), )

    
    Center = property(__Center.value, __Center.set, None, u"The coordinates of the circle's center")

    
    # Element SemiMajorAxis uses Python identifier SemiMajorAxis
    __SemiMajorAxis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SemiMajorAxis'), 'SemiMajorAxis', '__httpeuclid_esa_orgschemabasimpstc_ellipseType_SemiMajorAxis', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 273, 3), )

    
    SemiMajorAxis = property(__SemiMajorAxis.value, __SemiMajorAxis.set, None, u'The radius of the circle')

    
    # Element SemiMinorAxis uses Python identifier SemiMinorAxis
    __SemiMinorAxis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SemiMinorAxis'), 'SemiMinorAxis', '__httpeuclid_esa_orgschemabasimpstc_ellipseType_SemiMinorAxis', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 278, 3), )

    
    SemiMinorAxis = property(__SemiMinorAxis.value, __SemiMinorAxis.set, None, u'Half the minor axis of the ellipse, in radius_unit')

    
    # Element PosAngle uses Python identifier PosAngle
    __PosAngle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PosAngle'), 'PosAngle', '__httpeuclid_esa_orgschemabasimpstc_ellipseType_PosAngle', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 283, 3), )

    
    PosAngle = property(__PosAngle.value, __PosAngle.set, None, u'Position angle of major axis (Radius).')

    _ElementMap.update({
        __Center.name() : __Center,
        __SemiMajorAxis.name() : __SemiMajorAxis,
        __SemiMinorAxis.name() : __SemiMinorAxis,
        __PosAngle.name() : __PosAngle
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ellipseType', ellipseType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}smallCircleType with content type ELEMENT_ONLY
class smallCircleType (pyxb.binding.basis.complexTypeDefinition):
    """smallCircleType indicates in polygons that side is along small circle; with optional pole"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'smallCircleType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 292, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Pole uses Python identifier Pole
    __Pole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Pole'), 'Pole', '__httpeuclid_esa_orgschemabasimpstc_smallCircleType_Pole', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 297, 3), )

    
    Pole = property(__Pole.value, __Pole.set, None, None)

    _ElementMap.update({
        __Pole.name() : __Pole
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'smallCircleType', smallCircleType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}vertexType with content type ELEMENT_ONLY
class vertexType (pyxb.binding.basis.complexTypeDefinition):
    """Vertex is a position with optional SmallCircle element; the SmallCircle element indicates that the polygon side formed by that vertex and its predecessor vertex is a small circle, rather than a great circle; SmallCircle has no meaning in Cartesian coordinates"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'vertexType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 301, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Position'), 'Position', '__httpeuclid_esa_orgschemabasimpstc_vertexType_Position', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 306, 3), )

    
    Position = property(__Position.value, __Position.set, None, None)

    
    # Element SmallCircle uses Python identifier SmallCircle
    __SmallCircle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SmallCircle'), 'SmallCircle', '__httpeuclid_esa_orgschemabasimpstc_vertexType_SmallCircle', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 307, 3), )

    
    SmallCircle = property(__SmallCircle.value, __SmallCircle.set, None, None)

    _ElementMap.update({
        __Position.name() : __Position,
        __SmallCircle.name() : __SmallCircle
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'vertexType', vertexType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}polygonType with content type ELEMENT_ONLY
class polygonType (pyxb.binding.basis.complexTypeDefinition):
    """Polygon: one or more vertices; counter-clockwise (as seen from "inside" or from "top") encircled area is enclosed; sides should span less than 180 deg in each coordinate if spherical; a polygon may not intersect itself"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'polygonType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 311, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Vertex uses Python identifier Vertex
    __Vertex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Vertex'), 'Vertex', '__httpeuclid_esa_orgschemabasimpstc_polygonType_Vertex', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 316, 3), )

    
    Vertex = property(__Vertex.value, __Vertex.set, None, u'In order to form polygons, vertices are to be connected with straight line segments. In the case of spherical coordinates: greatcircle segments; if a smallCircle element si present, the vertex and its predecessor are to be connected with a smallcircle, by default in the CoordSys that is referenced; optionally, a pole may be specified (other than the CoordSys pole) that defines the smallcircle system')

    _ElementMap.update({
        __Vertex.name() : __Vertex
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'polygonType', polygonType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}boxType with content type ELEMENT_ONLY
class boxType (pyxb.binding.basis.complexTypeDefinition):
    """Box shape: a rectangle defined by its center and size on both dimensions; since it is a polygon, it is redundant, but simple rectangles with great circle sides are awkward to define in spherical coordinates"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'boxType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 324, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Center uses Python identifier Center
    __Center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Center'), 'Center', '__httpeuclid_esa_orgschemabasimpstc_boxType_Center', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 329, 3), )

    
    Center = property(__Center.value, __Center.set, None, u"The coordinates of the box's center")

    
    # Element Size uses Python identifier Size
    __Size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Size'), 'Size', '__httpeuclid_esa_orgschemabasimpstc_boxType_Size', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 334, 3), )

    
    Size = property(__Size.value, __Size.set, None, u"The lengths of the box's sides")

    _ElementMap.update({
        __Center.name() : __Center,
        __Size.name() : __Size
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'boxType', boxType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}sectorType with content type ELEMENT_ONLY
class sectorType (pyxb.binding.basis.complexTypeDefinition):
    """A sector is the counter-clockwise area between two half-lines"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sectorType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 342, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Position'), 'Position', '__httpeuclid_esa_orgschemabasimpstc_sectorType_Position', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 347, 3), )

    
    Position = property(__Position.value, __Position.set, None, u'The vertex position of the sector')

    
    # Element PosAngle1 uses Python identifier PosAngle1
    __PosAngle1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PosAngle1'), 'PosAngle1', '__httpeuclid_esa_orgschemabasimpstc_sectorType_PosAngle1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 352, 3), )

    
    PosAngle1 = property(__PosAngle1.value, __PosAngle1.set, None, u'The area cw from this position angle is included')

    
    # Element PosAngle2 uses Python identifier PosAngle2
    __PosAngle2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PosAngle2'), 'PosAngle2', '__httpeuclid_esa_orgschemabasimpstc_sectorType_PosAngle2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 357, 3), )

    
    PosAngle2 = property(__PosAngle2.value, __PosAngle2.set, None, u'The area cw from this position angle is included.')

    _ElementMap.update({
        __Position.name() : __Position,
        __PosAngle1.name() : __PosAngle1,
        __PosAngle2.name() : __PosAngle2
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sectorType', sectorType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}halfspaceType with content type ELEMENT_ONLY
class halfspaceType (pyxb.binding.basis.complexTypeDefinition):
    """An area on the unit sphere defined by the intersection with a plane"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'halfspaceType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 372, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Vector uses Python identifier Vector
    __Vector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Vector'), 'Vector', '__httpeuclid_esa_orgschemabasimpstc_halfspaceType_Vector', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 377, 3), )

    
    Vector = property(__Vector.value, __Vector.set, None, u'This needs to be a spherical coordinate vector; it is the unit vector that is normal to the plane that forms a constraint for a convex')

    
    # Element Offset uses Python identifier Offset
    __Offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Offset'), 'Offset', '__httpeuclid_esa_orgschemabasimpstc_halfspaceType_Offset', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 382, 3), )

    
    Offset = property(__Offset.value, __Offset.set, None, u'The distance along the normal vector where the constraint plane intersects that vector; if positive, the spherical sector on the far side (seen from the center) is selected; if negative, the point of intersection is in the opposite direction of the vector, resulting in more than a hemisphere; the valid range is -1.0 to +1.0')

    _ElementMap.update({
        __Vector.name() : __Vector,
        __Offset.name() : __Offset
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'halfspaceType', halfspaceType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}convexType with content type ELEMENT_ONLY
class convexType (pyxb.binding.basis.complexTypeDefinition):
    """A convex polygon defined by one or more Constraints"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'convexType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 390, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Halfspace uses Python identifier Halfspace
    __Halfspace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Halfspace'), 'Halfspace', '__httpeuclid_esa_orgschemabasimpstc_convexType_Halfspace', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 395, 3), )

    
    Halfspace = property(__Halfspace.value, __Halfspace.set, None, None)

    _ElementMap.update({
        __Halfspace.name() : __Halfspace
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'convexType', convexType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}unionType with content type ELEMENT_ONLY
class unionType (pyxb.binding.basis.complexTypeDefinition):
    """The union of two or more regions is a region"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 401, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Region uses Python identifier Region
    __Region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Region'), 'Region', '__httpeuclid_esa_orgschemabasimpstc_unionType_Region', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 406, 3), )

    
    Region = property(__Region.value, __Region.set, None, None)

    _ElementMap.update({
        __Region.name() : __Region
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'unionType', unionType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}intersectionType with content type ELEMENT_ONLY
class intersectionType (pyxb.binding.basis.complexTypeDefinition):
    """The intersection of two or more regions is a region"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'intersectionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 410, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Region uses Python identifier Region
    __Region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Region'), 'Region', '__httpeuclid_esa_orgschemabasimpstc_intersectionType_Region', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 415, 3), )

    
    Region = property(__Region.value, __Region.set, None, None)

    _ElementMap.update({
        __Region.name() : __Region
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'intersectionType', intersectionType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}negationType with content type ELEMENT_ONLY
class negationType (pyxb.binding.basis.complexTypeDefinition):
    """The negation of a region is a region"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'negationType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 419, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Region uses Python identifier Region
    __Region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Region'), 'Region', '__httpeuclid_esa_orgschemabasimpstc_negationType_Region', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 424, 3), )

    
    Region = property(__Region.value, __Region.set, None, None)

    _ElementMap.update({
        __Region.name() : __Region
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'negationType', negationType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}diffType with content type ELEMENT_ONLY
class diffType (pyxb.binding.basis.complexTypeDefinition):
    """The difference of two regions (Region1 minus Region2) is a region; it is equivalent to the intersection of Region1 with notRegion2"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'diffType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 428, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Region uses Python identifier Region
    __Region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Region'), 'Region', '__httpeuclid_esa_orgschemabasimpstc_diffType_Region', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 433, 3), )

    
    Region = property(__Region.value, __Region.set, None, None)

    
    # Element Region2 uses Python identifier Region2
    __Region2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Region2'), 'Region2', '__httpeuclid_esa_orgschemabasimpstc_diffType_Region2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 434, 3), )

    
    Region2 = property(__Region2.value, __Region2.set, None, None)

    _ElementMap.update({
        __Region.name() : __Region,
        __Region2.name() : __Region2
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'diffType', diffType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}astroCoordSystem with content type ELEMENT_ONLY
class astroCoordSystem (pyxb.binding.basis.complexTypeDefinition):
    """The coordinate system definition : spatial coordinate frame and reference position ; time frame and reference position ; the coordinate flavor ; the spectral frame and redshift/Doppler frame; and the planetary ephemeris ; an ID is required, since this is how coordinate elements are associated with their coordinate systems. This complexType should be embedded in the generic header of a whole data set. This complexType is derived from the STC - S metadata linear string implementation. We recap that this STC - S serialization don't support : generic coordinates (only : Time, Space, Spectral and Redshift), custom coordinate reference frames and custom refrence positions, spatial frames with offset positions, relocatable frames, planetary reference frames, geodetic reference spheroids other than IAU 1976. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'astroCoordSystem')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 439, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TimeFrame uses Python identifier TimeFrame
    __TimeFrame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TimeFrame'), 'TimeFrame', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_TimeFrame', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 444, 3), )

    
    TimeFrame = property(__TimeFrame.value, __TimeFrame.set, None, None)

    
    # Element SpaceFrame uses Python identifier SpaceFrame
    __SpaceFrame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SpaceFrame'), 'SpaceFrame', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_SpaceFrame', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 445, 3), )

    
    SpaceFrame = property(__SpaceFrame.value, __SpaceFrame.set, None, None)

    
    # Element SpectralFrame uses Python identifier SpectralFrame
    __SpectralFrame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SpectralFrame'), 'SpectralFrame', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_SpectralFrame', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 446, 3), )

    
    SpectralFrame = property(__SpectralFrame.value, __SpectralFrame.set, None, None)

    
    # Element RedshiftFrame uses Python identifier RedshiftFrame
    __RedshiftFrame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'RedshiftFrame'), 'RedshiftFrame', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_RedshiftFrame', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 447, 3), )

    
    RedshiftFrame = property(__RedshiftFrame.value, __RedshiftFrame.set, None, None)

    
    # Attribute AstroCoordSystemId uses Python identifier AstroCoordSystemId
    __AstroCoordSystemId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'AstroCoordSystemId'), 'AstroCoordSystemId', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_AstroCoordSystemId', pyxb.binding.datatypes.string, required=True)
    __AstroCoordSystemId._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 449, 2)
    __AstroCoordSystemId._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 449, 2)
    
    AstroCoordSystemId = property(__AstroCoordSystemId.value, __AstroCoordSystemId.set, None, None)

    _ElementMap.update({
        __TimeFrame.name() : __TimeFrame,
        __SpaceFrame.name() : __SpaceFrame,
        __SpectralFrame.name() : __SpectralFrame,
        __RedshiftFrame.name() : __RedshiftFrame
    })
    _AttributeMap.update({
        __AstroCoordSystemId.name() : __AstroCoordSystemId
    })
Namespace.addCategoryObject('typeBinding', u'astroCoordSystem', astroCoordSystem)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}timeFrame with content type ELEMENT_ONLY
class timeFrame (pyxb.binding.basis.complexTypeDefinition):
    """The time reference frame consists of a timescale, a reference position, and optionally a reference direction (needed when transformations have been applied). This type is derived from ivoa standards : STC V1.30. For simplification purpose and in order to get a better readability we met proposed simplifications from paragraph 5 timescale and refpos STC metadata linear string implementation V0.10. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeFrame')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 452, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_timeFrame_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 457, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element TimeScale uses Python identifier TimeScale
    __TimeScale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TimeScale'), 'TimeScale', '__httpeuclid_esa_orgschemabasimpstc_timeFrame_TimeScale', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 458, 3), )

    
    TimeScale = property(__TimeScale.value, __TimeScale.set, None, None)

    
    # Element ReferencePosition uses Python identifier ReferencePosition
    __ReferencePosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), 'ReferencePosition', '__httpeuclid_esa_orgschemabasimpstc_timeFrame_ReferencePosition', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 459, 3), )

    
    ReferencePosition = property(__ReferencePosition.value, __ReferencePosition.set, None, None)

    
    # Attribute TimeFrameId uses Python identifier TimeFrameId
    __TimeFrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'TimeFrameId'), 'TimeFrameId', '__httpeuclid_esa_orgschemabasimpstc_timeFrame_TimeFrameId', pyxb.binding.datatypes.string)
    __TimeFrameId._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 461, 2)
    __TimeFrameId._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 461, 2)
    
    TimeFrameId = property(__TimeFrameId.value, __TimeFrameId.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __TimeScale.name() : __TimeScale,
        __ReferencePosition.name() : __ReferencePosition
    })
    _AttributeMap.update({
        __TimeFrameId.name() : __TimeFrameId
    })
Namespace.addCategoryObject('typeBinding', u'timeFrame', timeFrame)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}spaceFrame with content type ELEMENT_ONLY
class spaceFrame (pyxb.binding.basis.complexTypeDefinition):
    """Coordinate reference frame : optional equinox with either a standard reference system (ICRS, FK5, FK4) and optional standard pole (equatorial, ecliptic, galactic, etc.), or a custom frame with pole (positive Z-axis) and positive X-axis direction.CoordFlavor provides the coordinate definitions: number of axes, SPHERICAL, CARTESIAN, UNITSPHERE, POLAR, or HEALPIX, presence of velocities. This type is derived from ivoa standards : STC V1.30."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spaceFrame')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 464, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 469, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element SpaceRefFrame uses Python identifier SpaceRefFrame
    __SpaceRefFrame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SpaceRefFrame'), 'SpaceRefFrame', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_SpaceRefFrame', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 470, 3), )

    
    SpaceRefFrame = property(__SpaceRefFrame.value, __SpaceRefFrame.set, None, None)

    
    # Element ReferencePosition uses Python identifier ReferencePosition
    __ReferencePosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), 'ReferencePosition', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_ReferencePosition', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 471, 3), )

    
    ReferencePosition = property(__ReferencePosition.value, __ReferencePosition.set, None, None)

    
    # Element CoordFlavor uses Python identifier CoordFlavor
    __CoordFlavor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'CoordFlavor'), 'CoordFlavor', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_CoordFlavor', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 472, 3), )

    
    CoordFlavor = property(__CoordFlavor.value, __CoordFlavor.set, None, None)

    
    # Attribute SpaceFrameId uses Python identifier SpaceFrameId
    __SpaceFrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SpaceFrameId'), 'SpaceFrameId', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_SpaceFrameId', pyxb.binding.datatypes.string)
    __SpaceFrameId._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 474, 2)
    __SpaceFrameId._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 474, 2)
    
    SpaceFrameId = property(__SpaceFrameId.value, __SpaceFrameId.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __SpaceRefFrame.name() : __SpaceRefFrame,
        __ReferencePosition.name() : __ReferencePosition,
        __CoordFlavor.name() : __CoordFlavor
    })
    _AttributeMap.update({
        __SpaceFrameId.name() : __SpaceFrameId
    })
Namespace.addCategoryObject('typeBinding', u'spaceFrame', spaceFrame)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}spectralFrame with content type ELEMENT_ONLY
class spectralFrame (pyxb.binding.basis.complexTypeDefinition):
    """Contains the spectral frame reference position. This type is derived from ivoa standards : STC V1.30."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectralFrame')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 477, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_spectralFrame_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 482, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element ReferencePosition uses Python identifier ReferencePosition
    __ReferencePosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), 'ReferencePosition', '__httpeuclid_esa_orgschemabasimpstc_spectralFrame_ReferencePosition', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 483, 3), )

    
    ReferencePosition = property(__ReferencePosition.value, __ReferencePosition.set, None, None)

    
    # Attribute SpectralFrameId uses Python identifier SpectralFrameId
    __SpectralFrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SpectralFrameId'), 'SpectralFrameId', '__httpeuclid_esa_orgschemabasimpstc_spectralFrame_SpectralFrameId', pyxb.binding.datatypes.string)
    __SpectralFrameId._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 485, 2)
    __SpectralFrameId._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 485, 2)
    
    SpectralFrameId = property(__SpectralFrameId.value, __SpectralFrameId.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __ReferencePosition.name() : __ReferencePosition
    })
    _AttributeMap.update({
        __SpectralFrameId.name() : __SpectralFrameId
    })
Namespace.addCategoryObject('typeBinding', u'spectralFrame', spectralFrame)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}redshiftFrame with content type ELEMENT_ONLY
class redshiftFrame (pyxb.binding.basis.complexTypeDefinition):
    """Contains the Doppler definitions, including whether the values are velocity or redshift (value). This type is derived from ivoa standards : STC V1.30."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'redshiftFrame')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 494, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 499, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_Value', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 500, 3), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element DopplerDefinition uses Python identifier DopplerDefinition
    __DopplerDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'DopplerDefinition'), 'DopplerDefinition', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_DopplerDefinition', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 501, 3), )

    
    DopplerDefinition = property(__DopplerDefinition.value, __DopplerDefinition.set, None, None)

    
    # Element ReferencePosition uses Python identifier ReferencePosition
    __ReferencePosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), 'ReferencePosition', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_ReferencePosition', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 502, 3), )

    
    ReferencePosition = property(__ReferencePosition.value, __ReferencePosition.set, None, None)

    
    # Attribute RedshiftFrameId uses Python identifier RedshiftFrameId
    __RedshiftFrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'RedshiftFrameId'), 'RedshiftFrameId', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_RedshiftFrameId', pyxb.binding.datatypes.string)
    __RedshiftFrameId._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 504, 2)
    __RedshiftFrameId._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 504, 2)
    
    RedshiftFrameId = property(__RedshiftFrameId.value, __RedshiftFrameId.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value,
        __DopplerDefinition.name() : __DopplerDefinition,
        __ReferencePosition.name() : __ReferencePosition
    })
    _AttributeMap.update({
        __RedshiftFrameId.name() : __RedshiftFrameId
    })
Namespace.addCategoryObject('typeBinding', u'redshiftFrame', redshiftFrame)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}spatialCoordDefType with content type ELEMENT_ONLY
class spatialCoordDefType (pyxb.binding.basis.complexTypeDefinition):
    """Provides the spatial coordinate representation either : SPHERICAL, CARTESIAN, UNITSPHERE, POLAR, or HEALPIX. SPHERICAL : Spherical 2-D (longitude, latitude) or 3-D (long, lat, radius/elevation) coordinates ; CARTESIAN : Cartesian 1-, 2-, or 3-D coordinates ; UNITSPHERE : 3-D Unit sphere coordinates (direction cosines); in (long,lat), X is in the direction (0,0), Y (pi/2,0), Z (0,pi/2) ; POLAR : 2-D polar coordinates (radius, posangle) ; CYLINDRICAL : 3-D cylindrical coordinates (radius, posangle, z) ; STRING : String coordinates (e.g., Stokes) ; HEALPIX : 2-D Healpix coordinates; defaults for H(4) and K(3). In STC metadata linear string implementation V0.10. the enumeration is more concise : SPHER2 for SPHERICAL 2-D, SPHER3 for SPHERICAL 3-D, CART1, CART2, CART 3 for CARTESIAN 1-2-or 3-D. We prefer maintain the STC full enumeration that embeds healpix flavor."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spatialCoordDefType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 603, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SPHERICAL uses Python identifier SPHERICAL
    __SPHERICAL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SPHERICAL'), 'SPHERICAL', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_SPHERICAL', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 608, 3), )

    
    SPHERICAL = property(__SPHERICAL.value, __SPHERICAL.set, None, None)

    
    # Element CARTESIAN uses Python identifier CARTESIAN
    __CARTESIAN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'CARTESIAN'), 'CARTESIAN', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_CARTESIAN', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 609, 3), )

    
    CARTESIAN = property(__CARTESIAN.value, __CARTESIAN.set, None, None)

    
    # Element UNITSPHERE uses Python identifier UNITSPHERE
    __UNITSPHERE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'UNITSPHERE'), 'UNITSPHERE', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_UNITSPHERE', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 610, 3), )

    
    UNITSPHERE = property(__UNITSPHERE.value, __UNITSPHERE.set, None, None)

    
    # Element POLAR uses Python identifier POLAR
    __POLAR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'POLAR'), 'POLAR', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_POLAR', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 611, 3), )

    
    POLAR = property(__POLAR.value, __POLAR.set, None, None)

    
    # Element CYLINDRICAL uses Python identifier CYLINDRICAL
    __CYLINDRICAL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'CYLINDRICAL'), 'CYLINDRICAL', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_CYLINDRICAL', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 612, 3), )

    
    CYLINDRICAL = property(__CYLINDRICAL.value, __CYLINDRICAL.set, None, None)

    
    # Element STRING uses Python identifier STRING
    __STRING = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'STRING'), 'STRING', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_STRING', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 613, 3), )

    
    STRING = property(__STRING.value, __STRING.set, None, None)

    
    # Element HEALPIX uses Python identifier HEALPIX
    __HEALPIX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'HEALPIX'), 'HEALPIX', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_HEALPIX', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 614, 3), )

    
    HEALPIX = property(__HEALPIX.value, __HEALPIX.set, None, None)

    _ElementMap.update({
        __SPHERICAL.name() : __SPHERICAL,
        __CARTESIAN.name() : __CARTESIAN,
        __UNITSPHERE.name() : __UNITSPHERE,
        __POLAR.name() : __POLAR,
        __CYLINDRICAL.name() : __CYLINDRICAL,
        __STRING.name() : __STRING,
        __HEALPIX.name() : __HEALPIX
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'spatialCoordDefType', spatialCoordDefType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}isoTime with content type SIMPLE
class isoTime (pyxb.binding.basis.complexTypeDefinition):
    """ISO8601 time; note: only a limited subset of ISO 8601 is allowed: yyyy-mm-ddThh:mm:ss.sss...; unfortunately, XSchema does not allow hh, mm, or ss to be optional, ".ss" is. This type is derived from IVOA STC V1.3."""
    _TypeDefinition = pyxb.binding.datatypes.dateTime
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'isoTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 777, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.dateTime
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'isoTime', isoTime)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}JDTime with content type SIMPLE
class JDTime (pyxb.binding.basis.complexTypeDefinition):
    """A decimal type for JD and MJD, with optional referencing."""
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'JDTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 786, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'JDTime', JDTime)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}MJDTime with content type SIMPLE
class MJDTime (pyxb.binding.basis.complexTypeDefinition):
    """MJD time (=JD - 2400000.5)"""
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MJDTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 795, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MJDTime', MJDTime)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}timeOffset with content type SIMPLE
class timeOffset (pyxb.binding.basis.complexTypeDefinition):
    """Actual elapsed time offset"""
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeOffset')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 804, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'timeOffset', timeOffset)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}astronTimeType with content type ELEMENT_ONLY
class astronTimeType (pyxb.binding.basis.complexTypeDefinition):
    """astronTime is the generalized astronomical time type and consists of one, two, or three elements: optional TimeScale, optional relative time offset, and an absolute time (ISO8601 or a decimal JD or MJD) ; TimeScale may be omitted only if the element is part of AstroCoords, referring to an AstroCoordSystem that specifies a TimeScale."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'astronTimeType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 813, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Timescale uses Python identifier Timescale
    __Timescale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Timescale'), 'Timescale', '__httpeuclid_esa_orgschemabasimpstc_astronTimeType_Timescale', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 818, 3), )

    
    Timescale = property(__Timescale.value, __Timescale.set, None, None)

    
    # Element TimeOffset uses Python identifier TimeOffset
    __TimeOffset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TimeOffset'), 'TimeOffset', '__httpeuclid_esa_orgschemabasimpstc_astronTimeType_TimeOffset', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 819, 3), )

    
    TimeOffset = property(__TimeOffset.value, __TimeOffset.set, None, None)

    
    # Element AbsoluteTime uses Python identifier AbsoluteTime
    __AbsoluteTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AbsoluteTime'), 'AbsoluteTime', '__httpeuclid_esa_orgschemabasimpstc_astronTimeType_AbsoluteTime', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 820, 3), )

    
    AbsoluteTime = property(__AbsoluteTime.value, __AbsoluteTime.set, None, None)

    _ElementMap.update({
        __Timescale.name() : __Timescale,
        __TimeOffset.name() : __TimeOffset,
        __AbsoluteTime.name() : __AbsoluteTime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'astronTimeType', astronTimeType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}TAIMillisecsecDateTimeRange with content type ELEMENT_ONLY
class TAIMillisecsecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    """An non UTC date-time range with a precision of one millisecond"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TAIMillisecsecDateTimeRange')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 889, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_TAIMillisecsecDateTimeRange_start', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 894, 3), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_TAIMillisecsecDateTimeRange_end', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 895, 3), )

    
    end = property(__end.value, __end.set, None, None)

    _ElementMap.update({
        __start.name() : __start,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'TAIMillisecsecDateTimeRange', TAIMillisecsecDateTimeRange)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}UTCDateTimeRange with content type ELEMENT_ONLY
class UTCDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    """An UTC date-time range"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCDateTimeRange')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 911, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCDateTimeRange_start', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 916, 3), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCDateTimeRange_end', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 917, 3), )

    
    end = property(__end.value, __end.set, None, None)

    _ElementMap.update({
        __start.name() : __start,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UTCDateTimeRange', UTCDateTimeRange)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}UTCMicrosecDateTimeRange with content type ELEMENT_ONLY
class UTCMicrosecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    """An UTC date-time range with a precision of one microsecond"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCMicrosecDateTimeRange')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 932, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCMicrosecDateTimeRange_start', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 937, 3), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCMicrosecDateTimeRange_end', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 938, 3), )

    
    end = property(__end.value, __end.set, None, None)

    _ElementMap.update({
        __start.name() : __start,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UTCMicrosecDateTimeRange', UTCMicrosecDateTimeRange)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}UTCMillisecDateTimeRange with content type ELEMENT_ONLY
class UTCMillisecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    """An UTC date-time range with a precision of one millisecond"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCMillisecDateTimeRange')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 953, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCMillisecDateTimeRange_start', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 958, 3), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCMillisecDateTimeRange_end', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 959, 3), )

    
    end = property(__end.value, __end.set, None, None)

    _ElementMap.update({
        __start.name() : __start,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UTCMillisecDateTimeRange', UTCMillisecDateTimeRange)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}UTCSecDateTimeRange with content type ELEMENT_ONLY
class UTCSecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    """An UTC date-time range with a precision of one second"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCSecDateTimeRange')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 974, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCSecDateTimeRange_start', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 979, 3), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCSecDateTimeRange_end', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 980, 3), )

    
    end = property(__end.value, __end.set, None, None)

    _ElementMap.update({
        __start.name() : __start,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UTCSecDateTimeRange', UTCSecDateTimeRange)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}UTCTenthMicrosecDateTimeRange with content type ELEMENT_ONLY
class UTCTenthMicrosecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    """An UTC date-time range with a precision of one tenth-of-a-microsecond"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCTenthMicrosecDateTimeRange')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 984, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCTenthMicrosecDateTimeRange_start', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 989, 3), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCTenthMicrosecDateTimeRange_end', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 990, 3), )

    
    end = property(__end.value, __end.set, None, None)

    _ElementMap.update({
        __start.name() : __start,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UTCTenthMicrosecDateTimeRange', UTCTenthMicrosecDateTimeRange)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}regionType with content type ELEMENT_ONLY
class regionType (coordScalarIntervalType):
    """A Region is a Shape or the result of a Region Operation involving one or more Regions"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'regionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 224, 1)
    _ElementMap = coordScalarIntervalType._ElementMap.copy()
    _AttributeMap = coordScalarIntervalType._AttributeMap.copy()
    # Base type is coordScalarIntervalType
    
    # Element LoLimit (LoLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element HiLimit (HiLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element Area uses Python identifier Area
    __Area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Area'), 'Area', '__httpeuclid_esa_orgschemabasimpstc_regionType_Area', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 231, 5), )

    
    Area = property(__Area.value, __Area.set, None, None)

    
    # Attribute lo_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute hi_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute fill_factor inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute FrameId inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute note uses Python identifier note
    __note = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'note'), 'note', '__httpeuclid_esa_orgschemabasimpstc_regionType_note', pyxb.binding.datatypes.string)
    __note._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 233, 4)
    __note._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 233, 4)
    
    note = property(__note.value, __note.set, None, None)

    
    # Attribute astroCoordSystem uses Python identifier astroCoordSystem
    __astroCoordSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'astroCoordSystem'), 'astroCoordSystem', '__httpeuclid_esa_orgschemabasimpstc_regionType_astroCoordSystem', pyxb.binding.datatypes.string)
    __astroCoordSystem._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 234, 4)
    __astroCoordSystem._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 234, 4)
    
    astroCoordSystem = property(__astroCoordSystem.value, __astroCoordSystem.set, None, None)

    _ElementMap.update({
        __Area.name() : __Area
    })
    _AttributeMap.update({
        __note.name() : __note,
        __astroCoordSystem.name() : __astroCoordSystem
    })
Namespace.addCategoryObject('typeBinding', u'regionType', regionType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}coordFlavorType with content type EMPTY
class coordFlavorType (pyxb.binding.basis.complexTypeDefinition):
    """Provides the characteristics of the spatial coordinate frame : number of axes, handedness."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coordFlavorType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 595, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute coord_naxes uses Python identifier coord_naxes
    __coord_naxes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'coord_naxes'), 'coord_naxes', '__httpeuclid_esa_orgschemabasimpstc_coordFlavorType_coord_naxes', coordNaxesValue, unicode_default=u'2')
    __coord_naxes._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 599, 2)
    __coord_naxes._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 599, 2)
    
    coord_naxes = property(__coord_naxes.value, __coord_naxes.set, None, None)

    
    # Attribute handedness uses Python identifier handedness
    __handedness = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'handedness'), 'handedness', '__httpeuclid_esa_orgschemabasimpstc_coordFlavorType_handedness', handednessValue)
    __handedness._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 600, 2)
    __handedness._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 600, 2)
    
    handedness = property(__handedness.value, __handedness.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __coord_naxes.name() : __coord_naxes,
        __handedness.name() : __handedness
    })
Namespace.addCategoryObject('typeBinding', u'coordFlavorType', coordFlavorType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}timeIntervalType with content type ELEMENT_ONLY
class timeIntervalType (coordScalarIntervalType):
    """The time interval needs to contain a start time and a stop time ; it needs to refer to a coordinate system; boundaries may or may not be inclusive. This type comes from STC ivoa schema, StartTime and StopTime are mandatory. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeIntervalType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 1027, 1)
    _ElementMap = coordScalarIntervalType._ElementMap.copy()
    _AttributeMap = coordScalarIntervalType._AttributeMap.copy()
    # Base type is coordScalarIntervalType
    
    # Element LoLimit (LoLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element HiLimit (HiLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'StartTime'), 'StartTime', '__httpeuclid_esa_orgschemabasimpstc_timeIntervalType_StartTime', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 1034, 5), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, u'astronTime may be expressed in ISO8601 or as a double relative to a reference time')

    
    # Element StopTime uses Python identifier StopTime
    __StopTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'StopTime'), 'StopTime', '__httpeuclid_esa_orgschemabasimpstc_timeIntervalType_StopTime', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 1039, 5), )

    
    StopTime = property(__StopTime.value, __StopTime.set, None, u'astronTime may be expressed in ISO8601 or as a double relative to a reference time')

    
    # Attribute lo_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute hi_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute fill_factor inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute FrameId inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    _ElementMap.update({
        __StartTime.name() : __StartTime,
        __StopTime.name() : __StopTime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'timeIntervalType', timeIntervalType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}basicCoordinateType with content type ELEMENT_ONLY
class basicCoordinateType (pyxb.binding.basis.complexTypeDefinition):
    """Basic scalar coordinate type. Single Error, Resolution, Size, PixSize elements indicate definite values ; pairs indicate ranges."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'basicCoordinateType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 16, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 21, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Value', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 22, 3), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element Error uses Python identifier Error
    __Error = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Error'), 'Error', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Error', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 23, 3), )

    
    Error = property(__Error.value, __Error.set, None, None)

    
    # Element Resolution uses Python identifier Resolution
    __Resolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Resolution'), 'Resolution', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Resolution', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 24, 3), )

    
    Resolution = property(__Resolution.value, __Resolution.set, None, None)

    
    # Element Size uses Python identifier Size
    __Size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Size'), 'Size', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Size', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 25, 3), )

    
    Size = property(__Size.value, __Size.set, None, None)

    
    # Element PixSize uses Python identifier PixSize
    __PixSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PixSize'), 'PixSize', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_PixSize', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 26, 3), )

    
    PixSize = property(__PixSize.value, __PixSize.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_CoordUnit', _ImportedBinding_euclid_dm__utd.unit)
    __CoordUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 28, 2)
    __CoordUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 28, 2)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value,
        __Error.name() : __Error,
        __Resolution.name() : __Resolution,
        __Size.name() : __Size,
        __PixSize.name() : __PixSize
    })
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit
    })
Namespace.addCategoryObject('typeBinding', u'basicCoordinateType', basicCoordinateType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}pixelVector1CoordinateType with content type ELEMENT_ONLY
class pixelVector1CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    """Scalar pixel coordinate type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelVector1CoordinateType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 31, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_pixelVector1CoordinateType_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 36, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasimpstc_pixelVector1CoordinateType_Value', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 37, 3), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_pixelVector1CoordinateType_CoordUnit', _ImportedBinding_euclid_dm__utd.unit)
    __CoordUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 39, 2)
    __CoordUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 39, 2)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit
    })
Namespace.addCategoryObject('typeBinding', u'pixelVector1CoordinateType', pixelVector1CoordinateType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}timeCoordinateType with content type ELEMENT_ONLY
class timeCoordinateType (pyxb.binding.basis.complexTypeDefinition):
    """Time coordinate type; sibling of basicCoordinateTypeSingle Error, Resolution, Size, PixSize elements indicate definite values ; pairs indicate ranges."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeCoordinateType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 42, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 48, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element TimeInstant uses Python identifier TimeInstant
    __TimeInstant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TimeInstant'), 'TimeInstant', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_TimeInstant', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 49, 3), )

    
    TimeInstant = property(__TimeInstant.value, __TimeInstant.set, None, None)

    
    # Element Error uses Python identifier Error
    __Error = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Error'), 'Error', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_Error', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 50, 3), )

    
    Error = property(__Error.value, __Error.set, None, None)

    
    # Element Resolution uses Python identifier Resolution
    __Resolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Resolution'), 'Resolution', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_Resolution', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 51, 3), )

    
    Resolution = property(__Resolution.value, __Resolution.set, None, None)

    
    # Element Size uses Python identifier Size
    __Size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Size'), 'Size', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_Size', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 52, 3), )

    
    Size = property(__Size.value, __Size.set, None, None)

    
    # Element PixSize uses Python identifier PixSize
    __PixSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PixSize'), 'PixSize', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_PixSize', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 53, 3), )

    
    PixSize = property(__PixSize.value, __PixSize.set, None, None)

    
    # Attribute AstroCoordSystemId uses Python identifier AstroCoordSystemId
    __AstroCoordSystemId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'AstroCoordSystemId'), 'AstroCoordSystemId', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_AstroCoordSystemId', pyxb.binding.datatypes.string)
    __AstroCoordSystemId._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 55, 2)
    __AstroCoordSystemId._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 55, 2)
    
    AstroCoordSystemId = property(__AstroCoordSystemId.value, __AstroCoordSystemId.set, None, None)

    
    # Attribute TimeUnit uses Python identifier TimeUnit
    __TimeUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'TimeUnit'), 'TimeUnit', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_TimeUnit', _ImportedBinding_euclid_dm__utd.unit)
    __TimeUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 56, 2)
    __TimeUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 56, 2)
    
    TimeUnit = property(__TimeUnit.value, __TimeUnit.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __TimeInstant.name() : __TimeInstant,
        __Error.name() : __Error,
        __Resolution.name() : __Resolution,
        __Size.name() : __Size,
        __PixSize.name() : __PixSize
    })
    _AttributeMap.update({
        __AstroCoordSystemId.name() : __AstroCoordSystemId,
        __TimeUnit.name() : __TimeUnit
    })
Namespace.addCategoryObject('typeBinding', u'timeCoordinateType', timeCoordinateType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}vector2CoordinateType with content type ELEMENT_ONLY
class vector2CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    """2-D coordinate typeSingle Error2, Resolution2, Size2, PixSize2 elements indicate definite values ; pairs indicate ranges."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'vector2CoordinateType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 60, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name1 uses Python identifier Name1
    __Name1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name1'), 'Name1', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Name1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 66, 3), )

    
    Name1 = property(__Name1.value, __Name1.set, None, None)

    
    # Element Name2 uses Python identifier Name2
    __Name2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name2'), 'Name2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Name2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 67, 3), )

    
    Name2 = property(__Name2.value, __Name2.set, None, None)

    
    # Element Value2 uses Python identifier Value2
    __Value2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Value2'), 'Value2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Value2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 68, 3), )

    
    Value2 = property(__Value2.value, __Value2.set, None, None)

    
    # Element Error2 uses Python identifier Error2
    __Error2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Error2'), 'Error2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Error2', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 69, 3), )

    
    Error2 = property(__Error2.value, __Error2.set, None, None)

    
    # Element Resolution2 uses Python identifier Resolution2
    __Resolution2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Resolution2'), 'Resolution2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Resolution2', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 70, 3), )

    
    Resolution2 = property(__Resolution2.value, __Resolution2.set, None, None)

    
    # Element Size2 uses Python identifier Size2
    __Size2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Size2'), 'Size2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Size2', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 71, 3), )

    
    Size2 = property(__Size2.value, __Size2.set, None, None)

    
    # Element PixSize2 uses Python identifier PixSize2
    __PixSize2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PixSize2'), 'PixSize2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_PixSize2', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 72, 3), )

    
    PixSize2 = property(__PixSize2.value, __PixSize2.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_CoordUnit', _ImportedBinding_euclid_dm__utd.unit)
    __CoordUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 74, 2)
    __CoordUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 74, 2)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    _ElementMap.update({
        __Name1.name() : __Name1,
        __Name2.name() : __Name2,
        __Value2.name() : __Value2,
        __Error2.name() : __Error2,
        __Resolution2.name() : __Resolution2,
        __Size2.name() : __Size2,
        __PixSize2.name() : __PixSize2
    })
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit
    })
Namespace.addCategoryObject('typeBinding', u'vector2CoordinateType', vector2CoordinateType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}pixelVector2CoordinateType with content type ELEMENT_ONLY
class pixelVector2CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    """2-D pixel coordinate type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelVector2CoordinateType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 77, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name1 uses Python identifier Name1
    __Name1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name1'), 'Name1', '__httpeuclid_esa_orgschemabasimpstc_pixelVector2CoordinateType_Name1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 82, 3), )

    
    Name1 = property(__Name1.value, __Name1.set, None, None)

    
    # Element Name2 uses Python identifier Name2
    __Name2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name2'), 'Name2', '__httpeuclid_esa_orgschemabasimpstc_pixelVector2CoordinateType_Name2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 83, 3), )

    
    Name2 = property(__Name2.value, __Name2.set, None, None)

    
    # Element Value2 uses Python identifier Value2
    __Value2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Value2'), 'Value2', '__httpeuclid_esa_orgschemabasimpstc_pixelVector2CoordinateType_Value2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 84, 3), )

    
    Value2 = property(__Value2.value, __Value2.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_pixelVector2CoordinateType_CoordUnit', _ImportedBinding_euclid_dm__utd.unit)
    __CoordUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 86, 2)
    __CoordUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 86, 2)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    _ElementMap.update({
        __Name1.name() : __Name1,
        __Name2.name() : __Name2,
        __Value2.name() : __Value2
    })
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit
    })
Namespace.addCategoryObject('typeBinding', u'pixelVector2CoordinateType', pixelVector2CoordinateType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}vector3CoordinateType with content type ELEMENT_ONLY
class vector3CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    """3-D coordinate typeSingle Error3, Resolution3, Size3, PixSize3 elements indicate definite values ; pairs indicate ranges."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'vector3CoordinateType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 90, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name1 uses Python identifier Name1
    __Name1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name1'), 'Name1', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Name1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 96, 3), )

    
    Name1 = property(__Name1.value, __Name1.set, None, None)

    
    # Element Name2 uses Python identifier Name2
    __Name2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name2'), 'Name2', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Name2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 97, 3), )

    
    Name2 = property(__Name2.value, __Name2.set, None, None)

    
    # Element Name3 uses Python identifier Name3
    __Name3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name3'), 'Name3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Name3', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 98, 3), )

    
    Name3 = property(__Name3.value, __Name3.set, None, None)

    
    # Element Value3 uses Python identifier Value3
    __Value3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Value3'), 'Value3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Value3', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 99, 3), )

    
    Value3 = property(__Value3.value, __Value3.set, None, None)

    
    # Element Error3 uses Python identifier Error3
    __Error3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Error3'), 'Error3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Error3', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 100, 3), )

    
    Error3 = property(__Error3.value, __Error3.set, None, None)

    
    # Element Resolution3 uses Python identifier Resolution3
    __Resolution3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Resolution3'), 'Resolution3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Resolution3', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 101, 3), )

    
    Resolution3 = property(__Resolution3.value, __Resolution3.set, None, None)

    
    # Element Size3 uses Python identifier Size3
    __Size3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Size3'), 'Size3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Size3', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 102, 3), )

    
    Size3 = property(__Size3.value, __Size3.set, None, None)

    
    # Element PixSize3 uses Python identifier PixSize3
    __PixSize3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PixSize3'), 'PixSize3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_PixSize3', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 103, 3), )

    
    PixSize3 = property(__PixSize3.value, __PixSize3.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_CoordUnit', _ImportedBinding_euclid_dm__utd.unit)
    __CoordUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 105, 2)
    __CoordUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 105, 2)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    _ElementMap.update({
        __Name1.name() : __Name1,
        __Name2.name() : __Name2,
        __Name3.name() : __Name3,
        __Value3.name() : __Value3,
        __Error3.name() : __Error3,
        __Resolution3.name() : __Resolution3,
        __Size3.name() : __Size3,
        __PixSize3.name() : __PixSize3
    })
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit
    })
Namespace.addCategoryObject('typeBinding', u'vector3CoordinateType', vector3CoordinateType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}pixelVector3CoordinateType with content type ELEMENT_ONLY
class pixelVector3CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    """3-D pixel coordinate type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelVector3CoordinateType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 108, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name1 uses Python identifier Name1
    __Name1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name1'), 'Name1', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_Name1', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 113, 3), )

    
    Name1 = property(__Name1.value, __Name1.set, None, None)

    
    # Element Name2 uses Python identifier Name2
    __Name2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name2'), 'Name2', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_Name2', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 114, 3), )

    
    Name2 = property(__Name2.value, __Name2.set, None, None)

    
    # Element Name3 uses Python identifier Name3
    __Name3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name3'), 'Name3', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_Name3', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 115, 3), )

    
    Name3 = property(__Name3.value, __Name3.set, None, None)

    
    # Element Value3 uses Python identifier Value3
    __Value3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Value3'), 'Value3', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_Value3', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 116, 3), )

    
    Value3 = property(__Value3.value, __Value3.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_CoordUnit', _ImportedBinding_euclid_dm__utd.unit)
    __CoordUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 118, 2)
    __CoordUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 118, 2)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    _ElementMap.update({
        __Name1.name() : __Name1,
        __Name2.name() : __Name2,
        __Name3.name() : __Name3,
        __Value3.name() : __Value3
    })
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit
    })
Namespace.addCategoryObject('typeBinding', u'pixelVector3CoordinateType', pixelVector3CoordinateType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}spectralIntervalType with content type ELEMENT_ONLY
class spectralIntervalType (coordScalarIntervalType):
    """Contains a 1-D spectral interval"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectralIntervalType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 188, 1)
    _ElementMap = coordScalarIntervalType._ElementMap.copy()
    _AttributeMap = coordScalarIntervalType._AttributeMap.copy()
    # Base type is coordScalarIntervalType
    
    # Element LoLimit (LoLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element HiLimit (HiLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute lo_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute hi_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute fill_factor inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute FrameId inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute SpectralUnit uses Python identifier SpectralUnit
    __SpectralUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SpectralUnit'), 'SpectralUnit', '__httpeuclid_esa_orgschemabasimpstc_spectralIntervalType_SpectralUnit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __SpectralUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 194, 4)
    __SpectralUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 194, 4)
    
    SpectralUnit = property(__SpectralUnit.value, __SpectralUnit.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __SpectralUnit.name() : __SpectralUnit
    })
Namespace.addCategoryObject('typeBinding', u'spectralIntervalType', spectralIntervalType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}redshiftIntervalType with content type ELEMENT_ONLY
class redshiftIntervalType (coordScalarIntervalType):
    """Contains a 1-D redshift interval; position and velocity units are required if redshifts are expressed as Doppler velocities"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'redshiftIntervalType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 199, 1)
    _ElementMap = coordScalarIntervalType._ElementMap.copy()
    _AttributeMap = coordScalarIntervalType._AttributeMap.copy()
    # Base type is coordScalarIntervalType
    
    # Element LoLimit (LoLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element HiLimit (HiLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute lo_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute hi_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute fill_factor inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute FrameId inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_redshiftIntervalType_CoordUnit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __CoordUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 205, 4)
    __CoordUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 205, 4)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    
    # Attribute RedshiftUnit uses Python identifier RedshiftUnit
    __RedshiftUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'RedshiftUnit'), 'RedshiftUnit', '__httpeuclid_esa_orgschemabasimpstc_redshiftIntervalType_RedshiftUnit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __RedshiftUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 206, 4)
    __RedshiftUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 206, 4)
    
    RedshiftUnit = property(__RedshiftUnit.value, __RedshiftUnit.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit,
        __RedshiftUnit.name() : __RedshiftUnit
    })
Namespace.addCategoryObject('typeBinding', u'redshiftIntervalType', redshiftIntervalType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}regionAreaType with content type SIMPLE
class regionAreaType (pyxb.binding.basis.complexTypeDefinition):
    """Element to hold the area of a Region, once calculated; the element holds the actual area, linearAreaUnit the linear units of the of the area (i.e., it should be squared to get the proper units of the area), and validArea indicates whether the area has been calculated properly."""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'regionAreaType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 212, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute linearAreaUnit uses Python identifier linearAreaUnit
    __linearAreaUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'linearAreaUnit'), 'linearAreaUnit', '__httpeuclid_esa_orgschemabasimpstc_regionAreaType_linearAreaUnit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __linearAreaUnit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 218, 4)
    __linearAreaUnit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 218, 4)
    
    linearAreaUnit = property(__linearAreaUnit.value, __linearAreaUnit.set, None, None)

    
    # Attribute validArea uses Python identifier validArea
    __validArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'validArea'), 'validArea', '__httpeuclid_esa_orgschemabasimpstc_regionAreaType_validArea', pyxb.binding.datatypes.boolean, required=True)
    __validArea._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 219, 4)
    __validArea._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 219, 4)
    
    validArea = property(__validArea.value, __validArea.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __linearAreaUnit.name() : __linearAreaUnit,
        __validArea.name() : __validArea
    })
Namespace.addCategoryObject('typeBinding', u'regionAreaType', regionAreaType)


# Complex type {http://euclid.esa.org/schema/bas/imp/stc}healpixType with content type EMPTY
class healpixType (coordFlavorType):
    """2-D Healpix coordinates; defaults for H(4) and K(3)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'healpixType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 618, 1)
    _ElementMap = coordFlavorType._ElementMap.copy()
    _AttributeMap = coordFlavorType._AttributeMap.copy()
    # Base type is coordFlavorType
    
    # Attribute coord_naxes inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordFlavorType
    
    # Attribute handedness inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordFlavorType
    
    # Attribute healpix_H uses Python identifier healpix_H
    __healpix_H = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'healpix_H'), 'healpix_H', '__httpeuclid_esa_orgschemabasimpstc_healpixType_healpix_H', pyxb.binding.datatypes.short, unicode_default=u'4')
    __healpix_H._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 624, 4)
    __healpix_H._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 624, 4)
    
    healpix_H = property(__healpix_H.value, __healpix_H.set, None, None)

    
    # Attribute healpix_K uses Python identifier healpix_K
    __healpix_K = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'healpix_K'), 'healpix_K', '__httpeuclid_esa_orgschemabasimpstc_healpixType_healpix_K', pyxb.binding.datatypes.short, unicode_default=u'3')
    __healpix_K._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 625, 4)
    __healpix_K._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 625, 4)
    
    healpix_K = property(__healpix_K.value, __healpix_K.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __healpix_H.name() : __healpix_H,
        __healpix_K.name() : __healpix_K
    })
Namespace.addCategoryObject('typeBinding', u'healpixType', healpixType)




coordScalarIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LoLimit'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=coordScalarIntervalType, documentation=u'Lower bound of interval.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3)))

coordScalarIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'HiLimit'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=coordScalarIntervalType, documentation=u'Upper bound of interval.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(coordScalarIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(coordScalarIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
coordScalarIntervalType._Automaton = _BuildAutomaton()




coord2VecIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LoLimit2Vec'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=coord2VecIntervalType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 161, 3)))

coord2VecIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'HiLimit2Vec'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=coord2VecIntervalType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 162, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 161, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 162, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(coord2VecIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit2Vec')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 161, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(coord2VecIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit2Vec')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 162, 3))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
coord2VecIntervalType._Automaton = _BuildAutomaton_()




coord3VecIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LoLimit3Vec'), _ImportedBinding_euclid_dm__dtd.double3Type, scope=coord3VecIntervalType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 177, 3)))

coord3VecIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'HiLimit3Vec'), _ImportedBinding_euclid_dm__dtd.double3Type, scope=coord3VecIntervalType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 178, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 177, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 178, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(coord3VecIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit3Vec')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 177, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(coord3VecIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit3Vec')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 178, 3))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
coord3VecIntervalType._Automaton = _BuildAutomaton_2()




circleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Center'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=circleType, documentation=u"The coordinates of the circle's center", location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 250, 3)))

circleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Radius'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=circleType, documentation=u'The radius of the circle', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 255, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(circleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Center')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 250, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(circleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Radius')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 255, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
circleType._Automaton = _BuildAutomaton_3()




ellipseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Center'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=ellipseType, documentation=u"The coordinates of the circle's center", location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 268, 3)))

ellipseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SemiMajorAxis'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=ellipseType, documentation=u'The radius of the circle', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 273, 3)))

ellipseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SemiMinorAxis'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=ellipseType, documentation=u'Half the minor axis of the ellipse, in radius_unit', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 278, 3)))

ellipseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PosAngle'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=ellipseType, documentation=u'Position angle of major axis (Radius).', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 283, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ellipseType._UseForTag(pyxb.namespace.ExpandedName(None, u'Center')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 268, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ellipseType._UseForTag(pyxb.namespace.ExpandedName(None, u'SemiMajorAxis')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 273, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ellipseType._UseForTag(pyxb.namespace.ExpandedName(None, u'SemiMinorAxis')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 278, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ellipseType._UseForTag(pyxb.namespace.ExpandedName(None, u'PosAngle')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 283, 3))
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
ellipseType._Automaton = _BuildAutomaton_4()




smallCircleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Pole'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=smallCircleType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 297, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 297, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(smallCircleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Pole')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 297, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
smallCircleType._Automaton = _BuildAutomaton_5()




vertexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Position'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=vertexType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 306, 3)))

vertexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SmallCircle'), smallCircleType, scope=vertexType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 307, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 307, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(vertexType._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 306, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vertexType._UseForTag(pyxb.namespace.ExpandedName(None, u'SmallCircle')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 307, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
vertexType._Automaton = _BuildAutomaton_6()




polygonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Vertex'), vertexType, scope=polygonType, documentation=u'In order to form polygons, vertices are to be connected with straight line segments. In the case of spherical coordinates: greatcircle segments; if a smallCircle element si present, the vertex and its predecessor are to be connected with a smallcircle, by default in the CoordSys that is referenced; optionally, a pole may be specified (other than the CoordSys pole) that defines the smallcircle system', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 316, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=100L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 316, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(polygonType._UseForTag(pyxb.namespace.ExpandedName(None, u'Vertex')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 316, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
polygonType._Automaton = _BuildAutomaton_7()




boxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Center'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=boxType, documentation=u"The coordinates of the box's center", location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 329, 3)))

boxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=boxType, documentation=u"The lengths of the box's sides", location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 334, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(boxType._UseForTag(pyxb.namespace.ExpandedName(None, u'Center')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 329, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(boxType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 334, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
boxType._Automaton = _BuildAutomaton_8()




sectorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Position'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=sectorType, documentation=u'The vertex position of the sector', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 347, 3)))

sectorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PosAngle1'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=sectorType, documentation=u'The area cw from this position angle is included', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 352, 3)))

sectorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PosAngle2'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=sectorType, documentation=u'The area cw from this position angle is included.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 357, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(sectorType._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 347, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(sectorType._UseForTag(pyxb.namespace.ExpandedName(None, u'PosAngle1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 352, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(sectorType._UseForTag(pyxb.namespace.ExpandedName(None, u'PosAngle2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 357, 3))
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
sectorType._Automaton = _BuildAutomaton_9()




halfspaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Vector'), _ImportedBinding_euclid_dm__dtd.double3Type, scope=halfspaceType, documentation=u'This needs to be a spherical coordinate vector; it is the unit vector that is normal to the plane that forms a constraint for a convex', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 377, 3)))

halfspaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Offset'), hsOffsetType, scope=halfspaceType, documentation=u'The distance along the normal vector where the constraint plane intersects that vector; if positive, the spherical sector on the far side (seen from the center) is selected; if negative, the point of intersection is in the opposite direction of the vector, resulting in more than a hemisphere; the valid range is -1.0 to +1.0', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 382, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(halfspaceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Vector')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 377, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(halfspaceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Offset')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 382, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
halfspaceType._Automaton = _BuildAutomaton_10()




convexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Halfspace'), halfspaceType, scope=convexType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 395, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=100L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 395, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(convexType._UseForTag(pyxb.namespace.ExpandedName(None, u'Halfspace')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 395, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
convexType._Automaton = _BuildAutomaton_11()




unionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region'), regionType, scope=unionType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 406, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2L, max=100L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 406, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(unionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 406, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
unionType._Automaton = _BuildAutomaton_12()




intersectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region'), regionType, scope=intersectionType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 415, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2L, max=100L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 415, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(intersectionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 415, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
intersectionType._Automaton = _BuildAutomaton_13()




negationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region'), regionType, scope=negationType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 424, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(negationType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 424, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
negationType._Automaton = _BuildAutomaton_14()




diffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region'), regionType, scope=diffType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 433, 3)))

diffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region2'), regionType, scope=diffType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 434, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(diffType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 433, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(diffType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 434, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
diffType._Automaton = _BuildAutomaton_15()




astroCoordSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TimeFrame'), timeFrame, scope=astroCoordSystem, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 444, 3)))

astroCoordSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SpaceFrame'), spaceFrame, scope=astroCoordSystem, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 445, 3)))

astroCoordSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SpectralFrame'), spectralFrame, scope=astroCoordSystem, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 446, 3)))

astroCoordSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'RedshiftFrame'), redshiftFrame, scope=astroCoordSystem, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 447, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 444, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 445, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 446, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 447, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(astroCoordSystem._UseForTag(pyxb.namespace.ExpandedName(None, u'TimeFrame')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 444, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(astroCoordSystem._UseForTag(pyxb.namespace.ExpandedName(None, u'SpaceFrame')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 445, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(astroCoordSystem._UseForTag(pyxb.namespace.ExpandedName(None, u'SpectralFrame')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 446, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(astroCoordSystem._UseForTag(pyxb.namespace.ExpandedName(None, u'RedshiftFrame')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 447, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
astroCoordSystem._Automaton = _BuildAutomaton_16()




timeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=timeFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 457, 3)))

timeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TimeScale'), timeScale, scope=timeFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 458, 3)))

timeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), referencePosition, scope=timeFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 459, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(timeFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 457, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(timeFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'TimeScale')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 458, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(timeFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferencePosition')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 459, 3))
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
timeFrame._Automaton = _BuildAutomaton_17()




spaceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=spaceFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 469, 3)))

spaceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SpaceRefFrame'), coordRefFrame, scope=spaceFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 470, 3)))

spaceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), referencePosition, scope=spaceFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 471, 3)))

spaceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CoordFlavor'), coordFlavorType, scope=spaceFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 472, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(spaceFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 469, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(spaceFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'SpaceRefFrame')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 470, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(spaceFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferencePosition')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 471, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spaceFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'CoordFlavor')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 472, 3))
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
spaceFrame._Automaton = _BuildAutomaton_18()




spectralFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=spectralFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 482, 3)))

spectralFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), referencePosition, scope=spectralFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 483, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(spectralFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 482, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spectralFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferencePosition')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 483, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
spectralFrame._Automaton = _BuildAutomaton_19()




redshiftFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=redshiftFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 499, 3)))

redshiftFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), redshiftFrameValue, scope=redshiftFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 500, 3)))

redshiftFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'DopplerDefinition'), dopplerDefinition, scope=redshiftFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 501, 3)))

redshiftFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), referencePosition, scope=redshiftFrame, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 502, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(redshiftFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 499, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(redshiftFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 500, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(redshiftFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'DopplerDefinition')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 501, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(redshiftFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferencePosition')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 502, 3))
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
redshiftFrame._Automaton = _BuildAutomaton_20()




spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SPHERICAL'), coordFlavorType, scope=spatialCoordDefType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 608, 3)))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CARTESIAN'), coordFlavorType, scope=spatialCoordDefType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 609, 3)))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'UNITSPHERE'), coordFlavorType, scope=spatialCoordDefType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 610, 3)))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'POLAR'), coordFlavorType, scope=spatialCoordDefType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 611, 3)))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CYLINDRICAL'), coordFlavorType, scope=spatialCoordDefType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 612, 3)))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'STRING'), coordFlavorType, scope=spatialCoordDefType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 613, 3)))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'HEALPIX'), healpixType, scope=spatialCoordDefType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 614, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'SPHERICAL')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 608, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'CARTESIAN')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 609, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'UNITSPHERE')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 610, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'POLAR')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 611, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'CYLINDRICAL')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 612, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'STRING')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 613, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'HEALPIX')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 614, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
spatialCoordDefType._Automaton = _BuildAutomaton_21()




astronTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Timescale'), timeScale, scope=astronTimeType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 818, 3)))

astronTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TimeOffset'), timeOffset, scope=astronTimeType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 819, 3)))

astronTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AbsoluteTime'), isoTime, scope=astronTimeType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 820, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 818, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 819, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(astronTimeType._UseForTag(pyxb.namespace.ExpandedName(None, u'Timescale')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 818, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(astronTimeType._UseForTag(pyxb.namespace.ExpandedName(None, u'TimeOffset')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 819, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(astronTimeType._UseForTag(pyxb.namespace.ExpandedName(None, u'AbsoluteTime')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 820, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
astronTimeType._Automaton = _BuildAutomaton_22()




TAIMillisecsecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), TAIMillisecsecDateTime, scope=TAIMillisecsecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 894, 3)))

TAIMillisecsecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), TAIMillisecsecDateTime, scope=TAIMillisecsecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 895, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAIMillisecsecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 894, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TAIMillisecsecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 895, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TAIMillisecsecDateTimeRange._Automaton = _BuildAutomaton_23()




UTCDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCDateTime, scope=UTCDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 916, 3)))

UTCDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCDateTime, scope=UTCDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 917, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UTCDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 916, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UTCDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 917, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UTCDateTimeRange._Automaton = _BuildAutomaton_24()




UTCMicrosecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCMicrosecDateTime, scope=UTCMicrosecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 937, 3)))

UTCMicrosecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCMicrosecDateTime, scope=UTCMicrosecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 938, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UTCMicrosecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 937, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UTCMicrosecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 938, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UTCMicrosecDateTimeRange._Automaton = _BuildAutomaton_25()




UTCMillisecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCMillisecDateTime, scope=UTCMillisecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 958, 3)))

UTCMillisecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCMillisecDateTime, scope=UTCMillisecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 959, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UTCMillisecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 958, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UTCMillisecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 959, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UTCMillisecDateTimeRange._Automaton = _BuildAutomaton_26()




UTCSecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCSecDateTime, scope=UTCSecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 979, 3)))

UTCSecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCSecDateTime, scope=UTCSecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 980, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UTCSecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 979, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UTCSecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 980, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UTCSecDateTimeRange._Automaton = _BuildAutomaton_27()




UTCTenthMicrosecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCTenthMicrosecDateTime, scope=UTCTenthMicrosecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 989, 3)))

UTCTenthMicrosecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCTenthMicrosecDateTime, scope=UTCTenthMicrosecDateTimeRange, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 990, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UTCTenthMicrosecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 989, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UTCTenthMicrosecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 990, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UTCTenthMicrosecDateTimeRange._Automaton = _BuildAutomaton_28()




regionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Area'), regionAreaType, scope=regionType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 231, 5)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 231, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(regionType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(regionType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(regionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Area')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
regionType._Automaton = _BuildAutomaton_29()




timeIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'StartTime'), astronTimeType, nillable=pyxb.binding.datatypes.boolean(1), scope=timeIntervalType, documentation=u'astronTime may be expressed in ISO8601 or as a double relative to a reference time', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 1034, 5)))

timeIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'StopTime'), astronTimeType, nillable=pyxb.binding.datatypes.boolean(1), scope=timeIntervalType, documentation=u'astronTime may be expressed in ISO8601 or as a double relative to a reference time', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 1039, 5)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(timeIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(timeIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(timeIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'StartTime')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 1034, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(timeIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'StopTime')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 1039, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
timeIntervalType._Automaton = _BuildAutomaton_30()




basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=basicCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 21, 3)))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=basicCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 22, 3)))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Error'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=basicCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 23, 3)))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Resolution'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=basicCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 24, 3)))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=basicCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 25, 3)))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PixSize'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=basicCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 26, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 21, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 22, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 23, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 24, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 25, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 26, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 21, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 22, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Error')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 23, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Resolution')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 24, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 25, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'PixSize')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 26, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
basicCoordinateType._Automaton = _BuildAutomaton_31()




pixelVector1CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=pixelVector1CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 36, 3)))

pixelVector1CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=pixelVector1CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 37, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 36, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 37, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pixelVector1CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pixelVector1CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 37, 3))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pixelVector1CoordinateType._Automaton = _BuildAutomaton_32()




timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=timeCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 48, 3)))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TimeInstant'), astronTimeType, scope=timeCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 49, 3)))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Error'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=timeCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 50, 3)))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Resolution'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=timeCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 51, 3)))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=timeCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 52, 3)))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PixSize'), _ImportedBinding_euclid_dm__dtd.double1Type, scope=timeCoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 53, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 48, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 49, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 50, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 51, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 52, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 53, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 48, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'TimeInstant')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 49, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Error')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 50, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Resolution')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 51, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 52, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'PixSize')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 53, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
timeCoordinateType._Automaton = _BuildAutomaton_33()




vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name1'), pyxb.binding.datatypes.string, scope=vector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 66, 3)))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name2'), pyxb.binding.datatypes.string, scope=vector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 67, 3)))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value2'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=vector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 68, 3)))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Error2'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=vector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 69, 3)))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Resolution2'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=vector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 70, 3)))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size2'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=vector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 71, 3)))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PixSize2'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=vector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 72, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 66, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 67, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 68, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 69, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 70, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 71, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 72, 3))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 66, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 67, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 68, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Error2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 69, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Resolution2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 70, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 71, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'PixSize2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 72, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
vector2CoordinateType._Automaton = _BuildAutomaton_34()




pixelVector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name1'), pyxb.binding.datatypes.string, scope=pixelVector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 82, 3)))

pixelVector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name2'), pyxb.binding.datatypes.string, scope=pixelVector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 83, 3)))

pixelVector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value2'), _ImportedBinding_euclid_dm__dtd.double2Type, scope=pixelVector2CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 84, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 82, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 83, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 84, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pixelVector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 82, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pixelVector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 83, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pixelVector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 84, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pixelVector2CoordinateType._Automaton = _BuildAutomaton_35()




vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name1'), pyxb.binding.datatypes.string, scope=vector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 96, 3)))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name2'), pyxb.binding.datatypes.string, scope=vector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 97, 3)))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name3'), pyxb.binding.datatypes.string, scope=vector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 98, 3)))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value3'), _ImportedBinding_euclid_dm__dtd.double3Type, scope=vector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 99, 3)))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Error3'), _ImportedBinding_euclid_dm__dtd.double3Type, scope=vector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 100, 3)))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Resolution3'), _ImportedBinding_euclid_dm__dtd.double3Type, scope=vector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 101, 3)))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size3'), _ImportedBinding_euclid_dm__dtd.double3Type, scope=vector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 102, 3)))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PixSize3'), _ImportedBinding_euclid_dm__dtd.double3Type, scope=vector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 103, 3)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 96, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 97, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 98, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 99, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 100, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 101, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 102, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 103, 3))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 96, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 97, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 98, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 99, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Error3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 100, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Resolution3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 101, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 102, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'PixSize3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 103, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
vector3CoordinateType._Automaton = _BuildAutomaton_36()




pixelVector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name1'), pyxb.binding.datatypes.string, scope=pixelVector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 113, 3)))

pixelVector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name2'), pyxb.binding.datatypes.string, scope=pixelVector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 114, 3)))

pixelVector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name3'), pyxb.binding.datatypes.string, scope=pixelVector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 115, 3)))

pixelVector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value3'), _ImportedBinding_euclid_dm__dtd.double3Type, scope=pixelVector3CoordinateType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 116, 3)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 113, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 114, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 115, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 116, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pixelVector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name1')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 113, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pixelVector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name2')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 114, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pixelVector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 115, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pixelVector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value3')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 116, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pixelVector3CoordinateType._Automaton = _BuildAutomaton_37()




def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(spectralIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(spectralIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
spectralIntervalType._Automaton = _BuildAutomaton_38()




def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(redshiftIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 127, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(redshiftIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/imp/stc/euc-test-stc.xsd', 132, 3))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
redshiftIntervalType._Automaton = _BuildAutomaton_39()

