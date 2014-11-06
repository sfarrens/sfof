# /home/sartor/pymodule/euclid/dm/_sys.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ef11d8db76a7f46c6c12cc44757c7de95f0af727
# Generated 2014-07-24 16:26:39.931732 by PyXB version 1.2.3
# Namespace http://euclid.esa.org/schema/sys [xmlns:sys]

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
import euclid.dm._bas as _ImportedBinding_euclid_dm__bas

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys', create_if_missing=True)
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


# Atomic simple type: {http://euclid.esa.org/schema/sys}systemDateTime
class systemDateTime (pyxb.binding.datatypes.dateTime):

    """
                An UTC date-time value with a precision of one millisecond
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'systemDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 19, 1)
    _Documentation = u'\n                An UTC date-time value with a precision of one millisecond\n            '
systemDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
systemDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\dZ')
systemDateTime._InitializeFacetMap(systemDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'systemDateTime', systemDateTime)

# Atomic simple type: {http://euclid.esa.org/schema/sys}configFileName
class configFileName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'configFileName')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 29, 1)
    _Documentation = None
configFileName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
configFileName._CF_pattern = pyxb.binding.facets.CF_pattern()
configFileName._CF_pattern.addPattern(pattern=u'EUC-[GSOV|IOTE|OPER|4SVT?|TD??|TEST].[A-Za-z0-9]{3,4}')
configFileName._InitializeFacetMap(configFileName._CF_maxLength,
   configFileName._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'configFileName', configFileName)

# Atomic simple type: {http://euclid.esa.org/schema/sys}infraName
class infraName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of SDC/infrastructures components used in EUCLID SGS.	"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'infraName')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 35, 1)
    _Documentation = u'List of SDC/infrastructures components used in EUCLID SGS.\t'
infraName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=infraName, enum_prefix=None)
infraName.EAS = infraName._CF_enumeration.addEnumeration(unicode_value=u'EAS', tag=u'EAS')
infraName.SDC_FR = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-FR', tag=u'SDC_FR')
infraName.SDC_IT = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-IT', tag=u'SDC_IT')
infraName.SDC_UK = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-UK', tag=u'SDC_UK')
infraName.SDC_NL = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-NL', tag=u'SDC_NL')
infraName.SDC_ES = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-ES', tag=u'SDC_ES')
infraName.SDC_FI = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-FI', tag=u'SDC_FI')
infraName.SDC_CH = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-CH', tag=u'SDC_CH')
infraName.SOC = infraName._CF_enumeration.addEnumeration(unicode_value=u'SOC', tag=u'SOC')
infraName.MOC = infraName._CF_enumeration.addEnumeration(unicode_value=u'MOC', tag=u'MOC')
infraName.CLOUDServices = infraName._CF_enumeration.addEnumeration(unicode_value=u'CLOUDServices', tag=u'CLOUDServices')
infraName.LOCAL = infraName._CF_enumeration.addEnumeration(unicode_value=u'LOCAL', tag=u'LOCAL')
infraName._InitializeFacetMap(infraName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'infraName', infraName)

# Atomic simple type: {http://euclid.esa.org/schema/sys}scientificGroupName
class scientificGroupName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of scientific groups used in EUCLID SGSreferring to OUs andSWG	"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'scientificGroupName')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 54, 1)
    _Documentation = u'List of scientific groups used in EUCLID SGSreferring to OUs andSWG\t'
scientificGroupName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=scientificGroupName, enum_prefix=None)
scientificGroupName.VIS = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'VIS', tag=u'VIS')
scientificGroupName.NIR = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'NIR', tag=u'NIR')
scientificGroupName.SIR = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SIR', tag=u'SIR')
scientificGroupName.SPE = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SPE', tag=u'SPE')
scientificGroupName.SIMWL = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SIMWL', tag=u'SIMWL')
scientificGroupName.SIM = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SIM', tag=u'SIM')
scientificGroupName.PHZ = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'PHZ', tag=u'PHZ')
scientificGroupName.LE3 = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'LE3', tag=u'LE3')
scientificGroupName.EXTDES = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'EXTDES', tag=u'EXTDES')
scientificGroupName.EXTPAN = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'EXTPAN', tag=u'EXTPAN')
scientificGroupName.EXTLSST = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'EXTLSST', tag=u'EXTLSST')
scientificGroupName.EXTKIDS = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'EXTKIDS', tag=u'EXTKIDS')
scientificGroupName.SHE = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SHE', tag=u'SHE')
scientificGroupName.MER = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'MER', tag=u'MER')
scientificGroupName._InitializeFacetMap(scientificGroupName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'scientificGroupName', scientificGroupName)

# Atomic simple type: {http://euclid.esa.org/schema/sys}version
class version (pyxb.binding.datatypes.string):

    """Generic use for a release of data,software, model,...No specific constraint between 3 and 6 characters from 0.1to 2.2.3 for example."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'version')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 75, 1)
    _Documentation = u'Generic use for a release of data,software, model,...No specific constraint between 3 and 6 characters from 0.1to 2.2.3 for example.'
version._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
version._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(6L))
version._InitializeFacetMap(version._CF_minLength,
   version._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'version', version)

# Atomic simple type: {http://euclid.esa.org/schema/sys}dataFileName
class dataFileName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataFileName')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 151, 1)
    _Documentation = None
dataFileName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
dataFileName._CF_pattern = pyxb.binding.facets.CF_pattern()
dataFileName._CF_pattern.addPattern(pattern=u'EUC-[GSOV|IOTE|OPER|4SVT?|TD??|TEST]{4}-[A-Za-z0-9]{1,10}-[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}(:*)[0-9]{2}(:*)[0-9]{2}(\\.[0-9]{1,6})?Z?\\.[A-Za-z0-9]{3,4}')
dataFileName._InitializeFacetMap(dataFileName._CF_maxLength,
   dataFileName._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'dataFileName', dataFileName)

# Complex type {http://euclid.esa.org/schema/sys}accessRights with content type ELEMENT_ONLY
class accessRights (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://euclid.esa.org/schema/sys}accessRights with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accessRights')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 84, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element EuclidConsortiumRead uses Python identifier EuclidConsortiumRead
    __EuclidConsortiumRead = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'EuclidConsortiumRead'), 'EuclidConsortiumRead', '__httpeuclid_esa_orgschemasys_accessRights_EuclidConsortiumRead', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 86, 3), )

    
    EuclidConsortiumRead = property(__EuclidConsortiumRead.value, __EuclidConsortiumRead.set, None, u'True if the interface is readable from Euclid consortia ')

    
    # Element EuclidConsortiumWrite uses Python identifier EuclidConsortiumWrite
    __EuclidConsortiumWrite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'EuclidConsortiumWrite'), 'EuclidConsortiumWrite', '__httpeuclid_esa_orgschemasys_accessRights_EuclidConsortiumWrite', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 91, 3), )

    
    EuclidConsortiumWrite = property(__EuclidConsortiumWrite.value, __EuclidConsortiumWrite.set, None, u'True if the interface is the writable from Euclid consortia')

    
    # Element ScientificGroupRead uses Python identifier ScientificGroupRead
    __ScientificGroupRead = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ScientificGroupRead'), 'ScientificGroupRead', '__httpeuclid_esa_orgschemasys_accessRights_ScientificGroupRead', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 96, 3), )

    
    ScientificGroupRead = property(__ScientificGroupRead.value, __ScientificGroupRead.set, None, u'True if the interface is readable from scientific group')

    
    # Element ScientificGroupWrite uses Python identifier ScientificGroupWrite
    __ScientificGroupWrite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ScientificGroupWrite'), 'ScientificGroupWrite', '__httpeuclid_esa_orgschemasys_accessRights_ScientificGroupWrite', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 101, 3), )

    
    ScientificGroupWrite = property(__ScientificGroupWrite.value, __ScientificGroupWrite.set, None, u'True if the interface is the writable from scientific group')

    _ElementMap.update({
        __EuclidConsortiumRead.name() : __EuclidConsortiumRead,
        __EuclidConsortiumWrite.name() : __EuclidConsortiumWrite,
        __ScientificGroupRead.name() : __ScientificGroupRead,
        __ScientificGroupWrite.name() : __ScientificGroupWrite
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'accessRights', accessRights)


# Complex type {http://euclid.esa.org/schema/sys}genericHeader with content type ELEMENT_ONLY
class genericHeader (pyxb.binding.basis.complexTypeDefinition):
    """Generic header for all data products"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'genericHeader')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 108, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ProductName uses Python identifier ProductName
    __ProductName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ProductName'), 'ProductName', '__httpeuclid_esa_orgschemasys_genericHeader_ProductName', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 114, 3), )

    
    ProductName = property(__ProductName.value, __ProductName.set, None, u'Product Name, the interface embeds one and only one Product. This information is derived from the task schema input/output name. ')

    
    # Element ProductId uses Python identifier ProductId
    __ProductId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ProductId'), 'ProductId', '__httpeuclid_esa_orgschemasys_genericHeader_ProductId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 119, 3), )

    
    ProductId = property(__ProductId.value, __ProductId.set, None, u'This Id is the unique reference of the object defined in thi interface, this Id is processed by IAL to ensure the uniqueness.')

    
    # Element ProductType uses Python identifier ProductType
    __ProductType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ProductType'), 'ProductType', '__httpeuclid_esa_orgschemasys_genericHeader_ProductType', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 124, 3), )

    
    ProductType = property(__ProductType.value, __ProductType.set, None, u'Identifies the type of product. The list of product types is defined within the Data Model.')

    
    # Element SoftwareName uses Python identifier SoftwareName
    __SoftwareName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SoftwareName'), 'SoftwareName', '__httpeuclid_esa_orgschemasys_genericHeader_SoftwareName', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 129, 3), )

    
    SoftwareName = property(__SoftwareName.value, __SoftwareName.set, None, u'This SoftwareName is extracted from the task definition : /tsk/component tsk/executable')

    
    # Element SoftwareRelease uses Python identifier SoftwareRelease
    __SoftwareRelease = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SoftwareRelease'), 'SoftwareRelease', '__httpeuclid_esa_orgschemasys_genericHeader_SoftwareRelease', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 134, 3), )

    
    SoftwareRelease = property(__SoftwareRelease.value, __SoftwareRelease.set, None, u'This SoftwareRelease is extracted from the task definition : /tsk/component tsk/version')

    
    # Element ScientificCustodian uses Python identifier ScientificCustodian
    __ScientificCustodian = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ScientificCustodian'), 'ScientificCustodian', '__httpeuclid_esa_orgschemasys_genericHeader_ScientificCustodian', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 139, 3), )

    
    ScientificCustodian = property(__ScientificCustodian.value, __ScientificCustodian.set, None, u'Scientific Group responsible of the quality of  the data referring to the OU or SWG or else. The custodian of this group and coordinates complete ')

    
    # Element AccessRights uses Python identifier AccessRights
    __AccessRights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AccessRights'), 'AccessRights', '__httpeuclid_esa_orgschemasys_genericHeader_AccessRights', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 144, 3), )

    
    AccessRights = property(__AccessRights.value, __AccessRights.set, None, u'Interface access rights.')

    _ElementMap.update({
        __ProductName.name() : __ProductName,
        __ProductId.name() : __ProductId,
        __ProductType.name() : __ProductType,
        __SoftwareName.name() : __SoftwareName,
        __SoftwareRelease.name() : __SoftwareRelease,
        __ScientificCustodian.name() : __ScientificCustodian,
        __AccessRights.name() : __AccessRights
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'genericHeader', genericHeader)




accessRights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'EuclidConsortiumRead'), pyxb.binding.datatypes.boolean, scope=accessRights, documentation=u'True if the interface is readable from Euclid consortia ', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 86, 3)))

accessRights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'EuclidConsortiumWrite'), pyxb.binding.datatypes.boolean, scope=accessRights, documentation=u'True if the interface is the writable from Euclid consortia', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 91, 3)))

accessRights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ScientificGroupRead'), pyxb.binding.datatypes.boolean, scope=accessRights, documentation=u'True if the interface is readable from scientific group', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 96, 3)))

accessRights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ScientificGroupWrite'), pyxb.binding.datatypes.boolean, scope=accessRights, documentation=u'True if the interface is the writable from scientific group', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 101, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(accessRights._UseForTag(pyxb.namespace.ExpandedName(None, u'EuclidConsortiumRead')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(accessRights._UseForTag(pyxb.namespace.ExpandedName(None, u'EuclidConsortiumWrite')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 91, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(accessRights._UseForTag(pyxb.namespace.ExpandedName(None, u'ScientificGroupRead')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 96, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(accessRights._UseForTag(pyxb.namespace.ExpandedName(None, u'ScientificGroupWrite')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 101, 3))
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
accessRights._Automaton = _BuildAutomaton()




genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ProductName'), _ImportedBinding_euclid_dm__bas.objectName, scope=genericHeader, documentation=u'Product Name, the interface embeds one and only one Product. This information is derived from the task schema input/output name. ', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 114, 3)))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ProductId'), _ImportedBinding_euclid_dm__bas.objectId, scope=genericHeader, documentation=u'This Id is the unique reference of the object defined in thi interface, this Id is processed by IAL to ensure the uniqueness.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 119, 3)))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ProductType'), pyxb.binding.datatypes.QName, scope=genericHeader, documentation=u'Identifies the type of product. The list of product types is defined within the Data Model.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 124, 3)))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SoftwareName'), pyxb.binding.datatypes.string, scope=genericHeader, documentation=u'This SoftwareName is extracted from the task definition : /tsk/component tsk/executable', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 129, 3)))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SoftwareRelease'), version, scope=genericHeader, documentation=u'This SoftwareRelease is extracted from the task definition : /tsk/component tsk/version', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 134, 3)))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ScientificCustodian'), scientificGroupName, scope=genericHeader, documentation=u'Scientific Group responsible of the quality of  the data referring to the OU or SWG or else. The custodian of this group and coordinates complete ', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 139, 3)))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AccessRights'), accessRights, scope=genericHeader, documentation=u'Interface access rights.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 144, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(genericHeader._UseForTag(pyxb.namespace.ExpandedName(None, u'ProductName')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 114, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(genericHeader._UseForTag(pyxb.namespace.ExpandedName(None, u'ProductId')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 119, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(genericHeader._UseForTag(pyxb.namespace.ExpandedName(None, u'ProductType')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 124, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(genericHeader._UseForTag(pyxb.namespace.ExpandedName(None, u'SoftwareName')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 129, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(genericHeader._UseForTag(pyxb.namespace.ExpandedName(None, u'SoftwareRelease')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 134, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(genericHeader._UseForTag(pyxb.namespace.ExpandedName(None, u'ScientificCustodian')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 139, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(genericHeader._UseForTag(pyxb.namespace.ExpandedName(None, u'AccessRights')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/euc-test-sys.xsd', 144, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
genericHeader._Automaton = _BuildAutomaton_()

