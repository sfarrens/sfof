# /home/sartor/pymodule/euclid/dm/_dss.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:44ff076caf94dd1666a330718f99f59b80790879
# Generated 2014-07-24 16:26:39.931924 by PyXB version 1.2.3
# Namespace http://euclid.esa.org/schema/sys/dss [xmlns:dss]

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
import euclid.dm._sys as _ImportedBinding_euclid_dm__sys

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys/dss', create_if_missing=True)
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


# Atomic simple type: {http://euclid.esa.org/schema/sys/dss}protocol
class protocol (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocol')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 21, 4)
    _Documentation = None
protocol._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=protocol, enum_prefix=None)
protocol.http = protocol._CF_enumeration.addEnumeration(unicode_value=u'http', tag=u'http')
protocol.https = protocol._CF_enumeration.addEnumeration(unicode_value=u'https', tag=u'https')
protocol.ftp = protocol._CF_enumeration.addEnumeration(unicode_value=u'ftp', tag=u'ftp')
protocol.sftp = protocol._CF_enumeration.addEnumeration(unicode_value=u'sftp', tag=u'sftp')
protocol.file = protocol._CF_enumeration.addEnumeration(unicode_value=u'file', tag=u'file')
protocol.gridftp = protocol._CF_enumeration.addEnumeration(unicode_value=u'gridftp', tag=u'gridftp')
protocol.srm = protocol._CF_enumeration.addEnumeration(unicode_value=u'srm', tag=u'srm')
protocol._InitializeFacetMap(protocol._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'protocol', protocol)

# Atomic simple type: {http://euclid.esa.org/schema/sys/dss}checksumAlgorithm
class checksumAlgorithm (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'checksumAlgorithm')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 35, 4)
    _Documentation = None
checksumAlgorithm._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=checksumAlgorithm, enum_prefix=None)
checksumAlgorithm.MD5 = checksumAlgorithm._CF_enumeration.addEnumeration(unicode_value=u'MD5', tag=u'MD5')
checksumAlgorithm.Adler32 = checksumAlgorithm._CF_enumeration.addEnumeration(unicode_value=u'Adler32', tag=u'Adler32')
checksumAlgorithm._InitializeFacetMap(checksumAlgorithm._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'checksumAlgorithm', checksumAlgorithm)

# Atomic simple type: {http://euclid.esa.org/schema/sys/dss}dataContainerFileStatus
class dataContainerFileStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The status of the file on the permanent storage node."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataContainerFileStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 49, 4)
    _Documentation = u'The status of the file on the permanent storage node.'
dataContainerFileStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dataContainerFileStatus, enum_prefix=None)
dataContainerFileStatus.PROPOSED = dataContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'PROPOSED', tag=u'PROPOSED')
dataContainerFileStatus.PROCESSING = dataContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'PROCESSING', tag=u'PROCESSING')
dataContainerFileStatus.COMMITED = dataContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'COMMITED', tag=u'COMMITED')
dataContainerFileStatus.VALIDATED = dataContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'VALIDATED', tag=u'VALIDATED')
dataContainerFileStatus.ARCHIVED = dataContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'ARCHIVED', tag=u'ARCHIVED')
dataContainerFileStatus.DELETED = dataContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'DELETED', tag=u'DELETED')
dataContainerFileStatus._InitializeFacetMap(dataContainerFileStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dataContainerFileStatus', dataContainerFileStatus)

# Atomic simple type: {http://euclid.esa.org/schema/sys/dss}fileContainerFileStatus
class fileContainerFileStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The status of the file on the permanent storage node."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fileContainerFileStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 99, 5)
    _Documentation = u'The status of the file on the permanent storage node.'
fileContainerFileStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fileContainerFileStatus, enum_prefix=None)
fileContainerFileStatus.ONLINE = fileContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'ONLINE', tag=u'ONLINE')
fileContainerFileStatus.OFFLINE = fileContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'OFFLINE', tag=u'OFFLINE')
fileContainerFileStatus.DELETED = fileContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'DELETED', tag=u'DELETED')
fileContainerFileStatus.emptyString = fileContainerFileStatus._CF_enumeration.addEnumeration(unicode_value=u'', tag='emptyString')
fileContainerFileStatus._InitializeFacetMap(fileContainerFileStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'fileContainerFileStatus', fileContainerFileStatus)

# Atomic simple type: {http://euclid.esa.org/schema/sys/dss}dataDistributionCommandType
class dataDistributionCommandType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataDistributionCommandType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 187, 4)
    _Documentation = None
dataDistributionCommandType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dataDistributionCommandType, enum_prefix=None)
dataDistributionCommandType.SUBMIT = dataDistributionCommandType._CF_enumeration.addEnumeration(unicode_value=u'SUBMIT', tag=u'SUBMIT')
dataDistributionCommandType.RETRIEVE = dataDistributionCommandType._CF_enumeration.addEnumeration(unicode_value=u'RETRIEVE', tag=u'RETRIEVE')
dataDistributionCommandType.COPY = dataDistributionCommandType._CF_enumeration.addEnumeration(unicode_value=u'COPY', tag=u'COPY')
dataDistributionCommandType.CHECK = dataDistributionCommandType._CF_enumeration.addEnumeration(unicode_value=u'CHECK', tag=u'CHECK')
dataDistributionCommandType.DELETE = dataDistributionCommandType._CF_enumeration.addEnumeration(unicode_value=u'DELETE', tag=u'DELETE')
dataDistributionCommandType._InitializeFacetMap(dataDistributionCommandType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dataDistributionCommandType', dataDistributionCommandType)

# Atomic simple type: {http://euclid.esa.org/schema/sys/dss}dataDistributionCommandStatus
class dataDistributionCommandStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataDistributionCommandStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 197, 4)
    _Documentation = None
dataDistributionCommandStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dataDistributionCommandStatus, enum_prefix=None)
dataDistributionCommandStatus.NEW = dataDistributionCommandStatus._CF_enumeration.addEnumeration(unicode_value=u'NEW', tag=u'NEW')
dataDistributionCommandStatus.APPROVED = dataDistributionCommandStatus._CF_enumeration.addEnumeration(unicode_value=u'APPROVED', tag=u'APPROVED')
dataDistributionCommandStatus.SCHEDULED = dataDistributionCommandStatus._CF_enumeration.addEnumeration(unicode_value=u'SCHEDULED', tag=u'SCHEDULED')
dataDistributionCommandStatus.PENDING = dataDistributionCommandStatus._CF_enumeration.addEnumeration(unicode_value=u'PENDING', tag=u'PENDING')
dataDistributionCommandStatus.EXECUTING = dataDistributionCommandStatus._CF_enumeration.addEnumeration(unicode_value=u'EXECUTING', tag=u'EXECUTING')
dataDistributionCommandStatus.DELETED = dataDistributionCommandStatus._CF_enumeration.addEnumeration(unicode_value=u'DELETED', tag=u'DELETED')
dataDistributionCommandStatus.ERROR = dataDistributionCommandStatus._CF_enumeration.addEnumeration(unicode_value=u'ERROR', tag=u'ERROR')
dataDistributionCommandStatus.COMPLETED = dataDistributionCommandStatus._CF_enumeration.addEnumeration(unicode_value=u'COMPLETED', tag=u'COMPLETED')
dataDistributionCommandStatus._InitializeFacetMap(dataDistributionCommandStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dataDistributionCommandStatus', dataDistributionCommandStatus)

# Complex type {http://euclid.esa.org/schema/sys/dss}checksumType with content type ELEMENT_ONLY
class checksumType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://euclid.esa.org/schema/sys/dss}checksumType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'checksumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 42, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/dss}Algorithm uses Python identifier Algorithm
    __Algorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Algorithm'), 'Algorithm', '__httpeuclid_esa_orgschemasysdss_checksumType_httpeuclid_esa_orgschemasysdssAlgorithm', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 44, 12), )

    
    Algorithm = property(__Algorithm.value, __Algorithm.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemasysdss_checksumType_httpeuclid_esa_orgschemasysdssValue', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 45, 12), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Algorithm.name() : __Algorithm,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'checksumType', checksumType)


# Complex type {http://euclid.esa.org/schema/sys/dss}dataContainerStorage with content type ELEMENT_ONLY
class dataContainerStorage (pyxb.binding.basis.complexTypeDefinition):
    """
                Data entity which is identified by a unique name possibly available as identical copies at different locations. 
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataContainerStorage')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 82, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/dss}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysdss_dataContainerStorage_httpeuclid_esa_orgschemasysdssId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 89, 12), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}Filename uses Python identifier Filename
    __Filename = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Filename'), 'Filename', '__httpeuclid_esa_orgschemasysdss_dataContainerStorage_httpeuclid_esa_orgschemasysdssFilename', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 90, 12), )

    
    Filename = property(__Filename.value, __Filename.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpeuclid_esa_orgschemasysdss_dataContainerStorage_httpeuclid_esa_orgschemasysdssDescription', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 91, 12), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpeuclid_esa_orgschemasysdss_dataContainerStorage_httpeuclid_esa_orgschemasysdssType', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 92, 12), )

    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), 'CreationDate', '__httpeuclid_esa_orgschemasysdss_dataContainerStorage_httpeuclid_esa_orgschemasysdssCreationDate', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 93, 12), )

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}CheckSum uses Python identifier CheckSum
    __CheckSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CheckSum'), 'CheckSum', '__httpeuclid_esa_orgschemasysdss_dataContainerStorage_httpeuclid_esa_orgschemasysdssCheckSum', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 94, 12), )

    
    CheckSum = property(__CheckSum.value, __CheckSum.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Location'), 'Location', '__httpeuclid_esa_orgschemasysdss_dataContainerStorage_httpeuclid_esa_orgschemasysdssLocation', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 95, 12), )

    
    Location = property(__Location.value, __Location.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Filename.name() : __Filename,
        __Description.name() : __Description,
        __Type.name() : __Type,
        __CreationDate.name() : __CreationDate,
        __CheckSum.name() : __CheckSum,
        __Location.name() : __Location
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'dataContainerStorage', dataContainerStorage)


# Complex type {http://euclid.esa.org/schema/sys/dss}fileContainer with content type ELEMENT_ONLY
class fileContainer (pyxb.binding.basis.complexTypeDefinition):
    """
                Specification of storage node and directory where the file is stored. 
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fileContainer')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 111, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/dss}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysdss_fileContainer_httpeuclid_esa_orgschemasysdssId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 118, 12), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}Path uses Python identifier Path
    __Path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Path'), 'Path', '__httpeuclid_esa_orgschemasysdss_fileContainer_httpeuclid_esa_orgschemasysdssPath', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 119, 12), )

    
    Path = property(__Path.value, __Path.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__httpeuclid_esa_orgschemasysdss_fileContainer_httpeuclid_esa_orgschemasysdssURL', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 120, 12), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}StorageNode uses Python identifier StorageNode
    __StorageNode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StorageNode'), 'StorageNode', '__httpeuclid_esa_orgschemasysdss_fileContainer_httpeuclid_esa_orgschemasysdssStorageNode', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 121, 12), )

    
    StorageNode = property(__StorageNode.value, __StorageNode.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}FileStatus uses Python identifier FileStatus
    __FileStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileStatus'), 'FileStatus', '__httpeuclid_esa_orgschemasysdss_fileContainer_httpeuclid_esa_orgschemasysdssFileStatus', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 122, 12), )

    
    FileStatus = property(__FileStatus.value, __FileStatus.set, None, None)

    
    # Attribute storagetype uses Python identifier storagetype
    __storagetype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'storagetype'), 'storagetype', '__httpeuclid_esa_orgschemasysdss_fileContainer_storagetype', pyxb.binding.datatypes.string)
    __storagetype._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 124, 9)
    __storagetype._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 124, 9)
    
    storagetype = property(__storagetype.value, __storagetype.set, None, u'\n                    Type of the storage - online, near-on-line\n                ')

    _ElementMap.update({
        __Id.name() : __Id,
        __Path.name() : __Path,
        __URL.name() : __URL,
        __StorageNode.name() : __StorageNode,
        __FileStatus.name() : __FileStatus
    })
    _AttributeMap.update({
        __storagetype.name() : __storagetype
    })
Namespace.addCategoryObject('typeBinding', u'fileContainer', fileContainer)


# Complex type {http://euclid.esa.org/schema/sys/dss}storageNode with content type ELEMENT_ONLY
class storageNode (pyxb.binding.basis.complexTypeDefinition):
    """Details for accessing a storage node"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'storageNode')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 133, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/dss}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysdss_storageNode_httpeuclid_esa_orgschemasysdssId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 138, 12), )

    
    Id = property(__Id.value, __Id.set, None, u'Should be of the form: sdc_protocol_domain_port_basePath')

    
    # Element {http://euclid.esa.org/schema/sys/dss}Protocol uses Python identifier Protocol
    __Protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Protocol'), 'Protocol', '__httpeuclid_esa_orgschemasysdss_storageNode_httpeuclid_esa_orgschemasysdssProtocol', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 143, 12), )

    
    Protocol = property(__Protocol.value, __Protocol.set, None, u'Protocol used to retrieve the file from this storage node.')

    
    # Element {http://euclid.esa.org/schema/sys/dss}Domain uses Python identifier Domain
    __Domain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Domain'), 'Domain', '__httpeuclid_esa_orgschemasysdss_storageNode_httpeuclid_esa_orgschemasysdssDomain', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 148, 12), )

    
    Domain = property(__Domain.value, __Domain.set, None, u'Name of the domain for this storage node.')

    
    # Element {http://euclid.esa.org/schema/sys/dss}Port uses Python identifier Port
    __Port = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Port'), 'Port', '__httpeuclid_esa_orgschemasysdss_storageNode_httpeuclid_esa_orgschemasysdssPort', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 153, 12), )

    
    Port = property(__Port.value, __Port.set, None, u'Port number this storage node can be accessed.')

    
    # Element {http://euclid.esa.org/schema/sys/dss}BasePath uses Python identifier BasePath
    __BasePath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'BasePath'), 'BasePath', '__httpeuclid_esa_orgschemasysdss_storageNode_httpeuclid_esa_orgschemasysdssBasePath', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 158, 12), )

    
    BasePath = property(__BasePath.value, __BasePath.set, None, u'Root path for the where to refer file locations to.')

    
    # Element {http://euclid.esa.org/schema/sys/dss}Sdc uses Python identifier Sdc
    __Sdc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Sdc'), 'Sdc', '__httpeuclid_esa_orgschemasysdss_storageNode_httpeuclid_esa_orgschemasysdssSdc', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 163, 12), )

    
    Sdc = property(__Sdc.value, __Sdc.set, None, u'Name of the SDC this storage node is associated with.')

    _ElementMap.update({
        __Id.name() : __Id,
        __Protocol.name() : __Protocol,
        __Domain.name() : __Domain,
        __Port.name() : __Port,
        __BasePath.name() : __BasePath,
        __Sdc.name() : __Sdc
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'storageNode', storageNode)


# Complex type {http://euclid.esa.org/schema/sys/dss}fileDescriptor with content type ELEMENT_ONLY
class fileDescriptor (pyxb.binding.basis.complexTypeDefinition):
    """
                Descriptor of a file used to store transient data such as data managed by the IAL
                until moved to the workspace as input for the pipeline processing tasks.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fileDescriptor')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 172, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/dss}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysdss_fileDescriptor_httpeuclid_esa_orgschemasysdssId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 180, 12), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}Filename uses Python identifier Filename
    __Filename = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Filename'), 'Filename', '__httpeuclid_esa_orgschemasysdss_fileDescriptor_httpeuclid_esa_orgschemasysdssFilename', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 181, 12), )

    
    Filename = property(__Filename.value, __Filename.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}Path uses Python identifier Path
    __Path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Path'), 'Path', '__httpeuclid_esa_orgschemasysdss_fileDescriptor_httpeuclid_esa_orgschemasysdssPath', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 182, 12), )

    
    Path = property(__Path.value, __Path.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}StorageId uses Python identifier StorageId
    __StorageId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StorageId'), 'StorageId', '__httpeuclid_esa_orgschemasysdss_fileDescriptor_httpeuclid_esa_orgschemasysdssStorageId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 183, 12), )

    
    StorageId = property(__StorageId.value, __StorageId.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Filename.name() : __Filename,
        __Path.name() : __Path,
        __StorageId.name() : __StorageId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'fileDescriptor', fileDescriptor)


# Complex type {http://euclid.esa.org/schema/sys/dss}dataDistributionDefinitionElement with content type ELEMENT_ONLY
class dataDistributionDefinitionElement (pyxb.binding.basis.complexTypeDefinition):
    """
                dataDistributionDefinitionElement is a single file operation in DDO
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataDistributionDefinitionElement')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 211, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOElementId uses Python identifier DDOElementId
    __DDOElementId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOElementId'), 'DDOElementId', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinitionElement_httpeuclid_esa_orgschemasysdssDDOElementId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 218, 12), )

    
    DDOElementId = property(__DDOElementId.value, __DDOElementId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOElementStatus uses Python identifier DDOElementStatus
    __DDOElementStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOElementStatus'), 'DDOElementStatus', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinitionElement_httpeuclid_esa_orgschemasysdssDDOElementStatus', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 219, 12), )

    
    DDOElementStatus = property(__DDOElementStatus.value, __DDOElementStatus.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOElementCommand uses Python identifier DDOElementCommand
    __DDOElementCommand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOElementCommand'), 'DDOElementCommand', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinitionElement_httpeuclid_esa_orgschemasysdssDDOElementCommand', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 220, 12), )

    
    DDOElementCommand = property(__DDOElementCommand.value, __DDOElementCommand.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOElementFilename uses Python identifier DDOElementFilename
    __DDOElementFilename = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOElementFilename'), 'DDOElementFilename', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinitionElement_httpeuclid_esa_orgschemasysdssDDOElementFilename', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 221, 12), )

    
    DDOElementFilename = property(__DDOElementFilename.value, __DDOElementFilename.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOElementFrom uses Python identifier DDOElementFrom
    __DDOElementFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOElementFrom'), 'DDOElementFrom', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinitionElement_httpeuclid_esa_orgschemasysdssDDOElementFrom', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 222, 12), )

    
    DDOElementFrom = property(__DDOElementFrom.value, __DDOElementFrom.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOElementTo uses Python identifier DDOElementTo
    __DDOElementTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOElementTo'), 'DDOElementTo', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinitionElement_httpeuclid_esa_orgschemasysdssDDOElementTo', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 223, 12), )

    
    DDOElementTo = property(__DDOElementTo.value, __DDOElementTo.set, None, None)

    _ElementMap.update({
        __DDOElementId.name() : __DDOElementId,
        __DDOElementStatus.name() : __DDOElementStatus,
        __DDOElementCommand.name() : __DDOElementCommand,
        __DDOElementFilename.name() : __DDOElementFilename,
        __DDOElementFrom.name() : __DDOElementFrom,
        __DDOElementTo.name() : __DDOElementTo
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'dataDistributionDefinitionElement', dataDistributionDefinitionElement)


# Complex type {http://euclid.esa.org/schema/sys/dss}dataDistributionDefinition with content type ELEMENT_ONLY
class dataDistributionDefinition (pyxb.binding.basis.complexTypeDefinition):
    """
                dataDistributionDefinition contains pattern for all commands to DSS, including:
                          - submit file 
                          - retrieve file
                          - copy 
                          - delete 
                          - check 
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataDistributionDefinition')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 228, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOId uses Python identifier DDOId
    __DDOId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOId'), 'DDOId', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinition_httpeuclid_esa_orgschemasysdssDDOId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 240, 12), )

    
    DDOId = property(__DDOId.value, __DDOId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOOrigin uses Python identifier DDOOrigin
    __DDOOrigin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOOrigin'), 'DDOOrigin', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinition_httpeuclid_esa_orgschemasysdssDDOOrigin', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 241, 12), )

    
    DDOOrigin = property(__DDOOrigin.value, __DDOOrigin.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOPPOId uses Python identifier DDOPPOId
    __DDOPPOId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOPPOId'), 'DDOPPOId', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinition_httpeuclid_esa_orgschemasysdssDDOPPOId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 242, 12), )

    
    DDOPPOId = property(__DDOPPOId.value, __DDOPPOId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOStatus uses Python identifier DDOStatus
    __DDOStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOStatus'), 'DDOStatus', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinition_httpeuclid_esa_orgschemasysdssDDOStatus', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 243, 12), )

    
    DDOStatus = property(__DDOStatus.value, __DDOStatus.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/dss}DDOElements uses Python identifier DDOElements
    __DDOElements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DDOElements'), 'DDOElements', '__httpeuclid_esa_orgschemasysdss_dataDistributionDefinition_httpeuclid_esa_orgschemasysdssDDOElements', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 244, 12), )

    
    DDOElements = property(__DDOElements.value, __DDOElements.set, None, None)

    _ElementMap.update({
        __DDOId.name() : __DDOId,
        __DDOOrigin.name() : __DDOOrigin,
        __DDOPPOId.name() : __DDOPPOId,
        __DDOStatus.name() : __DDOStatus,
        __DDOElements.name() : __DDOElements
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'dataDistributionDefinition', dataDistributionDefinition)


# Complex type {http://euclid.esa.org/schema/sys/dss}dataContainer with content type ELEMENT_ONLY
class dataContainer (pyxb.binding.basis.complexTypeDefinition):
    """
                Data entity which is identified by a unique name possibly available as identical copies at different locations. 
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataContainer')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 64, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/dss}FileName uses Python identifier FileName
    __FileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileName'), 'FileName', '__httpeuclid_esa_orgschemasysdss_dataContainer_httpeuclid_esa_orgschemasysdssFileName', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 71, 12), )

    
    FileName = property(__FileName.value, __FileName.set, None, None)

    
    # Attribute filestatus uses Python identifier filestatus
    __filestatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'filestatus'), 'filestatus', '__httpeuclid_esa_orgschemasysdss_dataContainer_filestatus', dataContainerFileStatus, required=True)
    __filestatus._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 73, 8)
    __filestatus._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 73, 8)
    
    filestatus = property(__filestatus.value, __filestatus.set, None, u'\n                    The status of the file - committed, validated, archived, deleted \n                ')

    _ElementMap.update({
        __FileName.name() : __FileName
    })
    _AttributeMap.update({
        __filestatus.name() : __filestatus
    })
Namespace.addCategoryObject('typeBinding', u'dataContainer', dataContainer)




checksumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Algorithm'), checksumAlgorithm, scope=checksumType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 44, 12)))

checksumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.string, scope=checksumType, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 45, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(checksumType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Algorithm')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 44, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(checksumType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 45, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
checksumType._Automaton = _BuildAutomaton()




dataContainerStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=dataContainerStorage, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 89, 12)))

dataContainerStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filename'), _ImportedBinding_euclid_dm__sys.dataFileName, scope=dataContainerStorage, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 90, 12)))

dataContainerStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=dataContainerStorage, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 91, 12)))

dataContainerStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), pyxb.binding.datatypes.string, scope=dataContainerStorage, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 92, 12)))

dataContainerStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), _ImportedBinding_euclid_dm__sys.systemDateTime, scope=dataContainerStorage, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 93, 12)))

dataContainerStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CheckSum'), checksumType, scope=dataContainerStorage, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 94, 12)))

dataContainerStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Location'), fileContainer, scope=dataContainerStorage, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 95, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 95, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataContainerStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 89, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataContainerStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filename')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 90, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataContainerStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 91, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataContainerStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 92, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataContainerStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 93, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(dataContainerStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CheckSum')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 94, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dataContainerStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Location')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 95, 12))
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
dataContainerStorage._Automaton = _BuildAutomaton_()




fileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=fileContainer, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 118, 12)))

fileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Path'), pyxb.binding.datatypes.string, scope=fileContainer, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 119, 12)))

fileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.string, scope=fileContainer, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 120, 12)))

fileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StorageNode'), storageNode, scope=fileContainer, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 121, 12)))

fileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileStatus'), fileContainerFileStatus, scope=fileContainer, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 122, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 120, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 122, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 118, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Path')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 119, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 120, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StorageNode')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 121, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(fileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileStatus')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 122, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
fileContainer._Automaton = _BuildAutomaton_2()




storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=storageNode, documentation=u'Should be of the form: sdc_protocol_domain_port_basePath', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 138, 12)))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Protocol'), protocol, scope=storageNode, documentation=u'Protocol used to retrieve the file from this storage node.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 143, 12)))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Domain'), pyxb.binding.datatypes.string, scope=storageNode, documentation=u'Name of the domain for this storage node.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 148, 12)))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Port'), pyxb.binding.datatypes.int, scope=storageNode, documentation=u'Port number this storage node can be accessed.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 153, 12)))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BasePath'), pyxb.binding.datatypes.string, scope=storageNode, documentation=u'Root path for the where to refer file locations to.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 158, 12)))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sdc'), _ImportedBinding_euclid_dm__sys.infraName, scope=storageNode, documentation=u'Name of the SDC this storage node is associated with.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 163, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 138, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Protocol')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 143, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Domain')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 148, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Port')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 153, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BasePath')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 158, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sdc')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 163, 12))
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
storageNode._Automaton = _BuildAutomaton_3()




fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=fileDescriptor, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 180, 12)))

fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filename'), pyxb.binding.datatypes.string, scope=fileDescriptor, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 181, 12)))

fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Path'), pyxb.binding.datatypes.string, scope=fileDescriptor, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 182, 12)))

fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StorageId'), pyxb.binding.datatypes.string, scope=fileDescriptor, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 183, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 180, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filename')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 181, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Path')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 182, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StorageId')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 183, 12))
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
fileDescriptor._Automaton = _BuildAutomaton_4()




dataDistributionDefinitionElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOElementId'), pyxb.binding.datatypes.string, scope=dataDistributionDefinitionElement, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 218, 12)))

dataDistributionDefinitionElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOElementStatus'), dataDistributionCommandStatus, scope=dataDistributionDefinitionElement, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 219, 12)))

dataDistributionDefinitionElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOElementCommand'), dataDistributionCommandType, scope=dataDistributionDefinitionElement, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 220, 12)))

dataDistributionDefinitionElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOElementFilename'), _ImportedBinding_euclid_dm__sys.dataFileName, scope=dataDistributionDefinitionElement, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 221, 12)))

dataDistributionDefinitionElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOElementFrom'), fileContainer, scope=dataDistributionDefinitionElement, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 222, 12)))

dataDistributionDefinitionElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOElementTo'), fileContainer, scope=dataDistributionDefinitionElement, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 223, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 222, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 223, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinitionElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOElementId')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 218, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinitionElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOElementStatus')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 219, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinitionElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOElementCommand')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 220, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinitionElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOElementFilename')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 221, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinitionElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOElementFrom')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 222, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinitionElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOElementTo')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 223, 12))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
dataDistributionDefinitionElement._Automaton = _BuildAutomaton_5()




dataDistributionDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOId'), pyxb.binding.datatypes.string, scope=dataDistributionDefinition, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 240, 12)))

dataDistributionDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOOrigin'), _ImportedBinding_euclid_dm__sys.infraName, scope=dataDistributionDefinition, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 241, 12)))

dataDistributionDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOPPOId'), pyxb.binding.datatypes.string, scope=dataDistributionDefinition, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 242, 12)))

dataDistributionDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOStatus'), dataDistributionCommandStatus, scope=dataDistributionDefinition, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 243, 12)))

dataDistributionDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DDOElements'), dataDistributionDefinitionElement, scope=dataDistributionDefinition, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 244, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOId')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 240, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOOrigin')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 241, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOPPOId')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 242, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOStatus')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 243, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(dataDistributionDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DDOElements')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 244, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
dataDistributionDefinition._Automaton = _BuildAutomaton_6()




dataContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileName'), _ImportedBinding_euclid_dm__sys.dataFileName, scope=dataContainer, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 71, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(dataContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileName')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/dss/euc-test-dss.xsd', 71, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
dataContainer._Automaton = _BuildAutomaton_7()

