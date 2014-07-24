# /home/sartor/pymodule/euclid/dm/_fit.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:975654cc63c7654a0853e9fafa22678e8820cfb9
# Generated 2014-07-24 16:26:39.932147 by PyXB version 1.2.3
# Namespace http://euclid.esa.org/schema/bas/fit [xmlns:fit]

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
import euclid.dm._dss as _ImportedBinding_euclid_dm__dss
import euclid.dm._utd as _ImportedBinding_euclid_dm__utd
import euclid.dm._impfits as _ImportedBinding_euclid_dm__impfits

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/fit', create_if_missing=True)
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


# Atomic simple type: {http://euclid.esa.org/schema/bas/fit}fitsFormatIdentifier
class fitsFormatIdentifier (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An identifier of a FITS format. Each Euclid metatada XML with a FITS file reference contains an instance of this identifier, which can be mapped to a FITS format description XML file in the Instances/fit directory of the Data Model. The format of the identifier is "ou_name.format_name", where ou_name is the name of the OU defining the FITS format (this is to avoid conflicts between OUs) and format_name is the identifier of the format. The CCB is responsible for validating that entries in this list of identifiers follow the correct format and the uniqueness of the format implementations in the Instances/fit directory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFormatIdentifier')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 19, 4)
    _Documentation = u'An identifier of a FITS format. Each Euclid metatada XML with a FITS file reference contains an instance of this identifier, which can be mapped to a FITS format description XML file in the Instances/fit directory of the Data Model. The format of the identifier is "ou_name.format_name", where ou_name is the name of the OU defining the FITS format (this is to avoid conflicts between OUs) and format_name is the identifier of the format. The CCB is responsible for validating that entries in this list of identifiers follow the correct format and the uniqueness of the format implementations in the Instances/fit directory.'
fitsFormatIdentifier._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fitsFormatIdentifier, enum_prefix=None)
fitsFormatIdentifier.sim_catalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.catalog', tag=u'sim_catalog')
fitsFormatIdentifier.sim_starCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.starCatalog', tag=u'sim_starCatalog')
fitsFormatIdentifier.sim_spectra = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.spectra', tag=u'sim_spectra')
fitsFormatIdentifier.sim_simulatedImage = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.simulatedImage', tag=u'sim_simulatedImage')
fitsFormatIdentifier.sim_spectrum = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.spectrum', tag=u'sim_spectrum')
fitsFormatIdentifier.sim_nipSimulatedImage = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.nipSimulatedImage', tag=u'sim_nipSimulatedImage')
fitsFormatIdentifier.sim_SEDLibrary = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.SEDLibrary', tag=u'sim_SEDLibrary')
fitsFormatIdentifier.sim_visOutCCD = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.visOutCCD', tag=u'sim_visOutCCD')
fitsFormatIdentifier.sim_visOutFPA = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.visOutFPA', tag=u'sim_visOutFPA')
fitsFormatIdentifier.sim_visOutQAD = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.visOutQAD', tag=u'sim_visOutQAD')
fitsFormatIdentifier.nis_pixelPsf = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.pixelPsf', tag=u'nis_pixelPsf')
fitsFormatIdentifier.nis_transmission = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.transmission', tag=u'nis_transmission')
fitsFormatIdentifier.nis_detectorQuantumEfficiencyMap = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.detectorQuantumEfficiencyMap', tag=u'nis_detectorQuantumEfficiencyMap')
fitsFormatIdentifier.nis_detectorQuantumEfficiencyCube = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.detectorQuantumEfficiencyCube', tag=u'nis_detectorQuantumEfficiencyCube')
fitsFormatIdentifier.nis_detectorReadoutNoiseMap = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.detectorReadoutNoiseMap', tag=u'nis_detectorReadoutNoiseMap')
fitsFormatIdentifier.nis_detectorDarkCurrentMap = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.detectorDarkCurrentMap', tag=u'nis_detectorDarkCurrentMap')
fitsFormatIdentifier.nis_cosmicRayMap = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.cosmicRayMap', tag=u'nis_cosmicRayMap')
fitsFormatIdentifier.sky_absorptionFactors = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sky.absorptionFactors', tag=u'sky_absorptionFactors')
fitsFormatIdentifier.spm_spectrum = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'spm.spectrum', tag=u'spm_spectrum')
fitsFormatIdentifier.le3_catalog_cluster = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.catalog.cluster', tag=u'le3_catalog_cluster')
fitsFormatIdentifier.le3_catalog_cluster_members = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.catalog.cluster_members', tag=u'le3_catalog_cluster_members')
fitsFormatIdentifier.le3_catalog_galaxy_specz = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.catalog.galaxy.specz', tag=u'le3_catalog_galaxy_specz')
fitsFormatIdentifier.le3_catalog_galaxy_photoz = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.catalog.galaxy.photoz', tag=u'le3_catalog_galaxy_photoz')
fitsFormatIdentifier.le3_catalog_galaxy_clustering = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.catalog.galaxy.clustering', tag=u'le3_catalog_galaxy_clustering')
fitsFormatIdentifier.le3_2ptcf_onedim = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.2ptcf.onedim', tag=u'le3_2ptcf_onedim')
fitsFormatIdentifier.le3_2ptcf_twodim = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.2ptcf.twodim', tag=u'le3_2ptcf_twodim')
fitsFormatIdentifier._InitializeFacetMap(fitsFormatIdentifier._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'fitsFormatIdentifier', fitsFormatIdentifier)

# Atomic simple type: {http://euclid.esa.org/schema/bas/fit}fitsFormatVersion
class fitsFormatVersion (pyxb.binding.datatypes.string):

    """The version of a FITS format. The version of a format (in the XML files) must be increased after any modification. Multiple versions of formats with the same identifier can coexist in the same version of the Data Model."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFormatVersion')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 53, 4)
    _Documentation = u'The version of a FITS format. The version of a format (in the XML files) must be increased after any modification. Multiple versions of formats with the same identifier can coexist in the same version of the Data Model.'
fitsFormatVersion._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'fitsFormatVersion', fitsFormatVersion)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 154, 12)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.int(1))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 159, 12)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.emptyString = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'*', tag='emptyString')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Union simple type: {http://euclid.esa.org/schema/bas/fit}hduMultiplicity
# superclasses pyxb.binding.datatypes.anySimpleType
class hduMultiplicity (pyxb.binding.basis.STD_union):

    """Defines the allowed values for the multiplicity of an HDU. It can be a positive integer, which specifies the number the HDUs following this format, or the '*' character, which specifies that the HDU format can be repeated an undefined number of times."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hduMultiplicity')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 148, 4)
    _Documentation = u"Defines the allowed values for the multiplicity of an HDU. It can be a positive integer, which specifies the number the HDUs following this format, or the '*' character, which specifies that the HDU format can be repeated an undefined number of times."

    _MemberTypes = ( STD_ANON, STD_ANON_, )
hduMultiplicity.emptyString = u'*'                # originally STD_ANON_.emptyString
hduMultiplicity._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'hduMultiplicity', hduMultiplicity)

# Complex type {http://euclid.esa.org/schema/bas/fit}headerKeywordList with content type ELEMENT_ONLY
class headerKeywordList (pyxb.binding.basis.complexTypeDefinition):
    """Defines a sequence of elements describing the EUCLID specific FITS header keywords (keywords not described in the FITS specification)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerKeywordList')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 132, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}UndefinedKeyword uses Python identifier UndefinedKeyword
    __UndefinedKeyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'UndefinedKeyword'), 'UndefinedKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitUndefinedKeyword', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 138, 12), )

    
    UndefinedKeyword = property(__UndefinedKeyword.value, __UndefinedKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}StringKeyword uses Python identifier StringKeyword
    __StringKeyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StringKeyword'), 'StringKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitStringKeyword', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 139, 12), )

    
    StringKeyword = property(__StringKeyword.value, __StringKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}LogicalKeyword uses Python identifier LogicalKeyword
    __LogicalKeyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'LogicalKeyword'), 'LogicalKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitLogicalKeyword', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 140, 12), )

    
    LogicalKeyword = property(__LogicalKeyword.value, __LogicalKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}IntegerKeyword uses Python identifier IntegerKeyword
    __IntegerKeyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IntegerKeyword'), 'IntegerKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitIntegerKeyword', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 141, 12), )

    
    IntegerKeyword = property(__IntegerKeyword.value, __IntegerKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}DoubleKeyword uses Python identifier DoubleKeyword
    __DoubleKeyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DoubleKeyword'), 'DoubleKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitDoubleKeyword', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 142, 12), )

    
    DoubleKeyword = property(__DoubleKeyword.value, __DoubleKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}ComplexIntegerKeyword uses Python identifier ComplexIntegerKeyword
    __ComplexIntegerKeyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ComplexIntegerKeyword'), 'ComplexIntegerKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitComplexIntegerKeyword', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 143, 12), )

    
    ComplexIntegerKeyword = property(__ComplexIntegerKeyword.value, __ComplexIntegerKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}ComplexDoubleKeyword uses Python identifier ComplexDoubleKeyword
    __ComplexDoubleKeyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ComplexDoubleKeyword'), 'ComplexDoubleKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitComplexDoubleKeyword', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 144, 12), )

    
    ComplexDoubleKeyword = property(__ComplexDoubleKeyword.value, __ComplexDoubleKeyword.set, None, None)

    _ElementMap.update({
        __UndefinedKeyword.name() : __UndefinedKeyword,
        __StringKeyword.name() : __StringKeyword,
        __LogicalKeyword.name() : __LogicalKeyword,
        __IntegerKeyword.name() : __IntegerKeyword,
        __DoubleKeyword.name() : __DoubleKeyword,
        __ComplexIntegerKeyword.name() : __ComplexIntegerKeyword,
        __ComplexDoubleKeyword.name() : __ComplexDoubleKeyword
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'headerKeywordList', headerKeywordList)


# Complex type {http://euclid.esa.org/schema/bas/fit}tableColumnList with content type ELEMENT_ONLY
class tableColumnList (pyxb.binding.basis.complexTypeDefinition):
    """Describes the list of columns of a binary table. The order of the columns is important and must match the order of the columns in the FITS file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'tableColumnList')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 189, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}Column uses Python identifier Column
    __Column = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Column'), 'Column', '__httpeuclid_esa_orgschemabasfit_tableColumnList_httpeuclid_esa_orgschemabasfitColumn', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 195, 12), )

    
    Column = property(__Column.value, __Column.set, None, None)

    _ElementMap.update({
        __Column.name() : __Column
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'tableColumnList', tableColumnList)


# Complex type {http://euclid.esa.org/schema/bas/fit}wcsAxesList with content type ELEMENT_ONLY
class wcsAxesList (pyxb.binding.basis.complexTypeDefinition):
    """The list of the axes of a WCS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsAxesList')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 235, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}Axis uses Python identifier Axis
    __Axis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Axis'), 'Axis', '__httpeuclid_esa_orgschemabasfit_wcsAxesList_httpeuclid_esa_orgschemabasfitAxis', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 241, 12), )

    
    Axis = property(__Axis.value, __Axis.set, None, None)

    _ElementMap.update({
        __Axis.name() : __Axis
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'wcsAxesList', wcsAxesList)


# Complex type {http://euclid.esa.org/schema/bas/fit}wcsList with content type ELEMENT_ONLY
class wcsList (pyxb.binding.basis.complexTypeDefinition):
    """The list of the WCS of an array HDU. Note that there should not be two WCS representations with the same identifier in the list and there should always be a representation with empty identifier (the primary representation)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsList')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 257, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}WCS uses Python identifier WCS
    __WCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'WCS'), 'WCS', '__httpeuclid_esa_orgschemabasfit_wcsList_httpeuclid_esa_orgschemabasfitWCS', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 263, 12), )

    
    WCS = property(__WCS.value, __WCS.set, None, None)

    _ElementMap.update({
        __WCS.name() : __WCS
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'wcsList', wcsList)


# Complex type {http://euclid.esa.org/schema/bas/fit}fitsFormatList with content type ELEMENT_ONLY
class fitsFormatList (pyxb.binding.basis.complexTypeDefinition):
    """Defines a list of FITS format definitions."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFormatList')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 296, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}FitsFormat uses Python identifier FitsFormat
    __FitsFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FitsFormat'), 'FitsFormat', '__httpeuclid_esa_orgschemabasfit_fitsFormatList_httpeuclid_esa_orgschemabasfitFitsFormat', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 302, 12), )

    
    FitsFormat = property(__FitsFormat.value, __FitsFormat.set, None, None)

    _ElementMap.update({
        __FitsFormat.name() : __FitsFormat
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'fitsFormatList', fitsFormatList)


# Complex type {http://euclid.esa.org/schema/bas/fit}fitsFile with content type ELEMENT_ONLY
class fitsFile (pyxb.binding.basis.complexTypeDefinition):
    """Defines the generic structure of a FITS file description. The data modelers should restrict this type in their product descriptions and set the format and version to fixed values, according the format of their product."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFile')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 59, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DataContainer uses Python identifier DataContainer
    __DataContainer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'DataContainer'), 'DataContainer', '__httpeuclid_esa_orgschemabasfit_fitsFile_DataContainer', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 64, 12), )

    
    DataContainer = property(__DataContainer.value, __DataContainer.set, None, None)

    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', fitsFormatIdentifier, required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 66, 8)
    __format._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 66, 8)
    
    format = property(__format.value, __format.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', fitsFormatVersion, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 67, 8)
    __version._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 67, 8)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __DataContainer.name() : __DataContainer
    })
    _AttributeMap.update({
        __format.name() : __format,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', u'fitsFile', fitsFile)


# Complex type {http://euclid.esa.org/schema/bas/fit}headerUndefinedKeyword with content type EMPTY
class headerUndefinedKeyword (pyxb.binding.basis.complexTypeDefinition):
    """Describes an undefined HDU header keyword. An undefined keyword does not have any value."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerUndefinedKeyword')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 70, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerUndefinedKeyword_name', _ImportedBinding_euclid_dm__impfits.headerKeywordName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 75, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 75, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'headerUndefinedKeyword', headerUndefinedKeyword)


# Complex type {http://euclid.esa.org/schema/bas/fit}headerStringKeyword with content type EMPTY
class headerStringKeyword (pyxb.binding.basis.complexTypeDefinition):
    """Describes a string type HDU header keyword."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerStringKeyword')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 78, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerStringKeyword_name', _ImportedBinding_euclid_dm__impfits.headerKeywordName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 83, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 83, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerStringKeyword_fixed', _ImportedBinding_euclid_dm__impfits.stringKeywordValue)
    __fixed._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 84, 8)
    __fixed._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 84, 8)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __fixed.name() : __fixed
    })
Namespace.addCategoryObject('typeBinding', u'headerStringKeyword', headerStringKeyword)


# Complex type {http://euclid.esa.org/schema/bas/fit}headerLogicalKeyword with content type EMPTY
class headerLogicalKeyword (pyxb.binding.basis.complexTypeDefinition):
    """Describes a logical type HDU header keyword."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerLogicalKeyword')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 87, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerLogicalKeyword_name', _ImportedBinding_euclid_dm__impfits.headerKeywordName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 92, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 92, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerLogicalKeyword_fixed', _ImportedBinding_euclid_dm__impfits.logicalKeywordValue)
    __fixed._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 93, 8)
    __fixed._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 93, 8)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __fixed.name() : __fixed
    })
Namespace.addCategoryObject('typeBinding', u'headerLogicalKeyword', headerLogicalKeyword)


# Complex type {http://euclid.esa.org/schema/bas/fit}headerIntegerKeyword with content type EMPTY
class headerIntegerKeyword (pyxb.binding.basis.complexTypeDefinition):
    """Describes an integer type HDU header keyword."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerIntegerKeyword')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 96, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerIntegerKeyword_name', _ImportedBinding_euclid_dm__impfits.headerKeywordName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 101, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 101, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerIntegerKeyword_fixed', _ImportedBinding_euclid_dm__impfits.integerKeywordValue)
    __fixed._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 102, 8)
    __fixed._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 102, 8)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __fixed.name() : __fixed
    })
Namespace.addCategoryObject('typeBinding', u'headerIntegerKeyword', headerIntegerKeyword)


# Complex type {http://euclid.esa.org/schema/bas/fit}headerDoubleKeyword with content type EMPTY
class headerDoubleKeyword (pyxb.binding.basis.complexTypeDefinition):
    """Describes a floating point type HDU header keyword."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerDoubleKeyword')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 105, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerDoubleKeyword_name', _ImportedBinding_euclid_dm__impfits.headerKeywordName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 110, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 110, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerDoubleKeyword_fixed', _ImportedBinding_euclid_dm__impfits.doubleKeywordValue)
    __fixed._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 111, 8)
    __fixed._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 111, 8)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __fixed.name() : __fixed
    })
Namespace.addCategoryObject('typeBinding', u'headerDoubleKeyword', headerDoubleKeyword)


# Complex type {http://euclid.esa.org/schema/bas/fit}wcsType with content type ELEMENT_ONLY
class wcsType (pyxb.binding.basis.complexTypeDefinition):
    """Describes a World Coordinate System (WCS) representation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 245, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}AxesList uses Python identifier AxesList
    __AxesList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AxesList'), 'AxesList', '__httpeuclid_esa_orgschemabasfit_wcsType_httpeuclid_esa_orgschemabasfitAxesList', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 251, 12), )

    
    AxesList = property(__AxesList.value, __AxesList.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_wcsType_name', _ImportedBinding_euclid_dm__impfits.wcsName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 253, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 253, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'identifier'), 'identifier', '__httpeuclid_esa_orgschemabasfit_wcsType_identifier', _ImportedBinding_euclid_dm__impfits.wcsIdentifier, required=True)
    __identifier._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 254, 8)
    __identifier._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 254, 8)
    
    identifier = property(__identifier.value, __identifier.set, None, None)

    _ElementMap.update({
        __AxesList.name() : __AxesList
    })
    _AttributeMap.update({
        __name.name() : __name,
        __identifier.name() : __identifier
    })
Namespace.addCategoryObject('typeBinding', u'wcsType', wcsType)


# Complex type {http://euclid.esa.org/schema/bas/fit}fitsFormat with content type ELEMENT_ONLY
class fitsFormat (pyxb.binding.basis.complexTypeDefinition):
    """Defines a FITS format. It has two attributes (id and version) for identifying the format and a list of elements representing the HDUs of the file. The order of the HDUs matters and must match the order in the FITS file. The attribute _multiplicity_ can be used for declaring consecutive HDUs with the same format. In the case the first HDU is a table, an empty generic HDU is assumed as the primary HDU of the file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFormat')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 282, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}GenericHDU uses Python identifier GenericHDU
    __GenericHDU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'GenericHDU'), 'GenericHDU', '__httpeuclid_esa_orgschemabasfit_fitsFormat_httpeuclid_esa_orgschemabasfitGenericHDU', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 288, 12), )

    
    GenericHDU = property(__GenericHDU.value, __GenericHDU.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}TableHDU uses Python identifier TableHDU
    __TableHDU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TableHDU'), 'TableHDU', '__httpeuclid_esa_orgschemabasfit_fitsFormat_httpeuclid_esa_orgschemabasfitTableHDU', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 289, 12), )

    
    TableHDU = property(__TableHDU.value, __TableHDU.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}ArrayHDU uses Python identifier ArrayHDU
    __ArrayHDU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ArrayHDU'), 'ArrayHDU', '__httpeuclid_esa_orgschemabasfit_fitsFormat_httpeuclid_esa_orgschemabasfitArrayHDU', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 290, 12), )

    
    ArrayHDU = property(__ArrayHDU.value, __ArrayHDU.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpeuclid_esa_orgschemabasfit_fitsFormat_id', fitsFormatIdentifier, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 292, 8)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 292, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFormat_version', fitsFormatVersion, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 293, 8)
    __version._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 293, 8)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __GenericHDU.name() : __GenericHDU,
        __TableHDU.name() : __TableHDU,
        __ArrayHDU.name() : __ArrayHDU
    })
    _AttributeMap.update({
        __id.name() : __id,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', u'fitsFormat', fitsFormat)


# Complex type {http://euclid.esa.org/schema/bas/fit}headerComplexIntegerKeyword with content type EMPTY
class headerComplexIntegerKeyword (pyxb.binding.basis.complexTypeDefinition):
    """Describes a complex integer type HDU header keyword."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerComplexIntegerKeyword')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 114, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerComplexIntegerKeyword_name', _ImportedBinding_euclid_dm__impfits.headerKeywordName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 119, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 119, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerComplexIntegerKeyword_fixed', _ImportedBinding_euclid_dm__impfits.complexIntegerKeywordValue)
    __fixed._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 120, 8)
    __fixed._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 120, 8)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __fixed.name() : __fixed
    })
Namespace.addCategoryObject('typeBinding', u'headerComplexIntegerKeyword', headerComplexIntegerKeyword)


# Complex type {http://euclid.esa.org/schema/bas/fit}headerComplexDoubleKeyword with content type EMPTY
class headerComplexDoubleKeyword (pyxb.binding.basis.complexTypeDefinition):
    """Describes a complex floating point type HDU header keyword."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerComplexDoubleKeyword')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 123, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerComplexDoubleKeyword_name', _ImportedBinding_euclid_dm__impfits.headerKeywordName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 128, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 128, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerComplexDoubleKeyword_fixed', _ImportedBinding_euclid_dm__impfits.complexDoubleKeywordValue)
    __fixed._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 129, 8)
    __fixed._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 129, 8)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __fixed.name() : __fixed
    })
Namespace.addCategoryObject('typeBinding', u'headerComplexDoubleKeyword', headerComplexDoubleKeyword)


# Complex type {http://euclid.esa.org/schema/bas/fit}genericHdu with content type ELEMENT_ONLY
class genericHdu (pyxb.binding.basis.complexTypeDefinition):
    """Defines the common generic part of all HDU types. This type can be used for defining HDUs containing only header keywords and no data or HDU types not explicitly specified here. To define table and array (or image) HDUs the types "fit:tableHdu" and "fit:arrayHdu" should be used."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'genericHdu')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 167, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}HeaderKeywordList uses Python identifier HeaderKeywordList
    __HeaderKeywordList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList'), 'HeaderKeywordList', '__httpeuclid_esa_orgschemabasfit_genericHdu_httpeuclid_esa_orgschemabasfitHeaderKeywordList', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 173, 12), )

    
    HeaderKeywordList = property(__HeaderKeywordList.value, __HeaderKeywordList.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_genericHdu_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 175, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 175, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute multiplicity uses Python identifier multiplicity
    __multiplicity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'multiplicity'), 'multiplicity', '__httpeuclid_esa_orgschemabasfit_genericHdu_multiplicity', hduMultiplicity)
    __multiplicity._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 176, 8)
    __multiplicity._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 176, 8)
    
    multiplicity = property(__multiplicity.value, __multiplicity.set, None, None)

    _ElementMap.update({
        __HeaderKeywordList.name() : __HeaderKeywordList
    })
    _AttributeMap.update({
        __name.name() : __name,
        __multiplicity.name() : __multiplicity
    })
Namespace.addCategoryObject('typeBinding', u'genericHdu', genericHdu)


# Complex type {http://euclid.esa.org/schema/bas/fit}binaryTableColumn with content type EMPTY
class binaryTableColumn (pyxb.binding.basis.complexTypeDefinition):
    """Describes a column of a FITS binary table. Each column is described by its name, its unit and its format. Implementations of FITS binary tables should contain an element of this type for each of their columns, restricting the different attributes to the required values."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'binaryTableColumn')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 179, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_binaryTableColumn_name', _ImportedBinding_euclid_dm__impfits.binaryTableColumnName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 184, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 184, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpeuclid_esa_orgschemabasfit_binaryTableColumn_unit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __unit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 185, 8)
    __unit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 185, 8)
    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_binaryTableColumn_format', _ImportedBinding_euclid_dm__impfits.binaryTableColumnFormat, required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 186, 8)
    __format._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 186, 8)
    
    format = property(__format.value, __format.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __unit.name() : __unit,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'binaryTableColumn', binaryTableColumn)


# Complex type {http://euclid.esa.org/schema/bas/fit}arrayInfo with content type EMPTY
class arrayInfo (pyxb.binding.basis.complexTypeDefinition):
    """Contains the information describing the format of a FITS array."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'arrayInfo')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 213, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute numberOfDimentions uses Python identifier numberOfDimentions
    __numberOfDimentions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numberOfDimentions'), 'numberOfDimentions', '__httpeuclid_esa_orgschemabasfit_arrayInfo_numberOfDimentions', _ImportedBinding_euclid_dm__impfits.arrayNumberOfDimensions, required=True)
    __numberOfDimentions._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 218, 8)
    __numberOfDimentions._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 218, 8)
    
    numberOfDimentions = property(__numberOfDimentions.value, __numberOfDimentions.set, None, None)

    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_arrayInfo_format', _ImportedBinding_euclid_dm__impfits.arrayFormat, required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 220, 8)
    __format._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 220, 8)
    
    format = property(__format.value, __format.set, None, None)

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpeuclid_esa_orgschemabasfit_arrayInfo_unit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __unit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 221, 8)
    __unit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 221, 8)
    
    unit = property(__unit.value, __unit.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __numberOfDimentions.name() : __numberOfDimentions,
        __format.name() : __format,
        __unit.name() : __unit
    })
Namespace.addCategoryObject('typeBinding', u'arrayInfo', arrayInfo)


# Complex type {http://euclid.esa.org/schema/bas/fit}wcsAxis with content type EMPTY
class wcsAxis (pyxb.binding.basis.complexTypeDefinition):
    """Describes an axis of a WCS. Each axis is described by its name, its unit, its type and, if a non linear projection, the projection algorithm. More information about the standarized type-algorithm pairs can be found in the FITS specification."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsAxis')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 224, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_wcsAxis_name', _ImportedBinding_euclid_dm__impfits.wcsAxisName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 229, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 229, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpeuclid_esa_orgschemabasfit_wcsAxis_unit', _ImportedBinding_euclid_dm__utd.unit, required=True)
    __unit._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 230, 8)
    __unit._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 230, 8)
    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpeuclid_esa_orgschemabasfit_wcsAxis_type', _ImportedBinding_euclid_dm__impfits.wcsAxisType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 231, 8)
    __type._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 231, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute projectionAlgorithm uses Python identifier projectionAlgorithm
    __projectionAlgorithm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'projectionAlgorithm'), 'projectionAlgorithm', '__httpeuclid_esa_orgschemabasfit_wcsAxis_projectionAlgorithm', _ImportedBinding_euclid_dm__impfits.wcsAxisProjectionAlgorithm)
    __projectionAlgorithm._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 232, 8)
    __projectionAlgorithm._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 232, 8)
    
    projectionAlgorithm = property(__projectionAlgorithm.value, __projectionAlgorithm.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __unit.name() : __unit,
        __type.name() : __type,
        __projectionAlgorithm.name() : __projectionAlgorithm
    })
Namespace.addCategoryObject('typeBinding', u'wcsAxis', wcsAxis)


# Complex type {http://euclid.esa.org/schema/bas/fit}tableHdu with content type ELEMENT_ONLY
class tableHdu (genericHdu):
    """Describes the structure of a binary table HDU."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'tableHdu')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 199, 4)
    _ElementMap = genericHdu._ElementMap.copy()
    _AttributeMap = genericHdu._AttributeMap.copy()
    # Base type is genericHdu
    
    # Element HeaderKeywordList ({http://euclid.esa.org/schema/bas/fit}HeaderKeywordList) inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    
    # Element {http://euclid.esa.org/schema/bas/fit}ColumnList uses Python identifier ColumnList
    __ColumnList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ColumnList'), 'ColumnList', '__httpeuclid_esa_orgschemabasfit_tableHdu_httpeuclid_esa_orgschemabasfitColumnList', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 207, 20), )

    
    ColumnList = property(__ColumnList.value, __ColumnList.set, None, None)

    
    # Attribute name inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    
    # Attribute multiplicity inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    _ElementMap.update({
        __ColumnList.name() : __ColumnList
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'tableHdu', tableHdu)


# Complex type {http://euclid.esa.org/schema/bas/fit}arrayHdu with content type ELEMENT_ONLY
class arrayHdu (genericHdu):
    """Describes the structure of an array (or image) HDU."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'arrayHdu')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 267, 4)
    _ElementMap = genericHdu._ElementMap.copy()
    _AttributeMap = genericHdu._AttributeMap.copy()
    # Base type is genericHdu
    
    # Element HeaderKeywordList ({http://euclid.esa.org/schema/bas/fit}HeaderKeywordList) inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    
    # Element {http://euclid.esa.org/schema/bas/fit}ArrayInfo uses Python identifier ArrayInfo
    __ArrayInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ArrayInfo'), 'ArrayInfo', '__httpeuclid_esa_orgschemabasfit_arrayHdu_httpeuclid_esa_orgschemabasfitArrayInfo', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 275, 20), )

    
    ArrayInfo = property(__ArrayInfo.value, __ArrayInfo.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}WCSList uses Python identifier WCSList
    __WCSList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'WCSList'), 'WCSList', '__httpeuclid_esa_orgschemabasfit_arrayHdu_httpeuclid_esa_orgschemabasfitWCSList', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 276, 20), )

    
    WCSList = property(__WCSList.value, __WCSList.set, None, None)

    
    # Attribute name inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    
    # Attribute multiplicity inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    _ElementMap.update({
        __ArrayInfo.name() : __ArrayInfo,
        __WCSList.name() : __WCSList
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'arrayHdu', arrayHdu)


FitsFormatList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitsFormatList'), fitsFormatList, documentation=u'This element should be the root of all the XML files in the Instances/fit directory.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 307, 4))
Namespace.addCategoryObject('elementBinding', FitsFormatList.name().localName(), FitsFormatList)



headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UndefinedKeyword'), headerUndefinedKeyword, scope=headerKeywordList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 138, 12)))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StringKeyword'), headerStringKeyword, scope=headerKeywordList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 139, 12)))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogicalKeyword'), headerLogicalKeyword, scope=headerKeywordList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 140, 12)))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IntegerKeyword'), headerIntegerKeyword, scope=headerKeywordList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 141, 12)))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DoubleKeyword'), headerDoubleKeyword, scope=headerKeywordList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 142, 12)))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComplexIntegerKeyword'), headerComplexIntegerKeyword, scope=headerKeywordList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 143, 12)))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComplexDoubleKeyword'), headerComplexDoubleKeyword, scope=headerKeywordList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 144, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 137, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UndefinedKeyword')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 138, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StringKeyword')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 139, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogicalKeyword')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 140, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IntegerKeyword')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 141, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DoubleKeyword')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 142, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComplexIntegerKeyword')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 143, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComplexDoubleKeyword')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 144, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
headerKeywordList._Automaton = _BuildAutomaton()




tableColumnList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Column'), binaryTableColumn, scope=tableColumnList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 195, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 195, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tableColumnList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Column')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 195, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tableColumnList._Automaton = _BuildAutomaton_()




wcsAxesList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Axis'), wcsAxis, scope=wcsAxesList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 241, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(wcsAxesList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Axis')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 241, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
wcsAxesList._Automaton = _BuildAutomaton_2()




wcsList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WCS'), wcsType, scope=wcsList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 263, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(wcsList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WCS')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 263, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
wcsList._Automaton = _BuildAutomaton_3()




fitsFormatList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitsFormat'), fitsFormat, scope=fitsFormatList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 302, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 302, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(fitsFormatList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FitsFormat')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 302, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
fitsFormatList._Automaton = _BuildAutomaton_4()




fitsFile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'DataContainer'), _ImportedBinding_euclid_dm__dss.dataContainer, scope=fitsFile, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 64, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fitsFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 64, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
fitsFile._Automaton = _BuildAutomaton_5()




wcsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AxesList'), wcsAxesList, scope=wcsType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 251, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(wcsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AxesList')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 251, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
wcsType._Automaton = _BuildAutomaton_6()




fitsFormat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GenericHDU'), genericHdu, scope=fitsFormat, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 288, 12)))

fitsFormat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TableHDU'), tableHdu, scope=fitsFormat, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 289, 12)))

fitsFormat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ArrayHDU'), arrayHdu, scope=fitsFormat, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 290, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fitsFormat._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GenericHDU')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 288, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fitsFormat._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TableHDU')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 289, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fitsFormat._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ArrayHDU')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 290, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
fitsFormat._Automaton = _BuildAutomaton_7()




genericHdu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList'), headerKeywordList, scope=genericHdu, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 173, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(genericHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
genericHdu._Automaton = _BuildAutomaton_8()




tableHdu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ColumnList'), tableColumnList, scope=tableHdu, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 207, 20)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tableHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tableHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ColumnList')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 207, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tableHdu._Automaton = _BuildAutomaton_9()




arrayHdu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ArrayInfo'), arrayInfo, scope=arrayHdu, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 275, 20)))

arrayHdu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WCSList'), wcsList, scope=arrayHdu, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 276, 20)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(arrayHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(arrayHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ArrayInfo')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 275, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(arrayHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WCSList')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/bas/fit/euc-test-fit.xsd', 276, 20))
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
arrayHdu._Automaton = _BuildAutomaton_10()

