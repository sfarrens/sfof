# /home/sartor/pymodule/euclid/dm/_sgs.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:77d3da8c9c0b8eec64b9957d9ec227ca99caec32
# Generated 2014-07-24 16:26:39.933073 by PyXB version 1.2.3
# Namespace http://euclid.esa.org/schema/sys/sgs [xmlns:sgs]

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
import euclid.dm._dss as _ImportedBinding_euclid_dm__dss

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys/sgs', create_if_missing=True)
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


# Atomic simple type: {http://euclid.esa.org/schema/sys/sgs}emailAddress
class emailAddress (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'emailAddress')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 10, 1)
    _Documentation = None
emailAddress._CF_pattern = pyxb.binding.facets.CF_pattern()
emailAddress._CF_pattern.addPattern(pattern=u'[^@]+@[^\\.]+\\..+')
emailAddress._InitializeFacetMap(emailAddress._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'emailAddress', emailAddress)

# Complex type {http://euclid.esa.org/schema/sys/sgs}ivoaUCDParam with content type ELEMENT_ONLY
class ivoaUCDParam (pyxb.binding.basis.complexTypeDefinition):
    """This complex type agregates the two ivoa parameters : name and ucd. The definition of the UCD is on ivoa site : http://www.ivoa.net/Documents/REC/UCD/UCDlist-20070402.html#_Toc163276342."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ivoaUCDParam')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 15, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemasyssgs_ivoaUCDParam_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 21, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element UCD uses Python identifier UCD
    __UCD = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'UCD'), 'UCD', '__httpeuclid_esa_orgschemasyssgs_ivoaUCDParam_UCD', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 22, 3), )

    
    UCD = property(__UCD.value, __UCD.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __UCD.name() : __UCD
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ivoaUCDParam', ivoaUCDParam)


# Complex type {http://euclid.esa.org/schema/sys/sgs}curation with content type ELEMENT_ONLY
class curation (pyxb.binding.basis.complexTypeDefinition):
    """This type defines the different characterisitics of the curator of the corresponding set of data."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'curation')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Publisher uses Python identifier Publisher
    __Publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Publisher'), 'Publisher', '__httpeuclid_esa_orgschemasyssgs_curation_Publisher', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 31, 3), )

    
    Publisher = property(__Publisher.value, __Publisher.set, None, None)

    
    # Element PublisherID uses Python identifier PublisherID
    __PublisherID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PublisherID'), 'PublisherID', '__httpeuclid_esa_orgschemasyssgs_curation_PublisherID', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 32, 3), )

    
    PublisherID = property(__PublisherID.value, __PublisherID.set, None, None)

    
    # Element Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Reference'), 'Reference', '__httpeuclid_esa_orgschemasyssgs_curation_Reference', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 33, 3), )

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    
    # Element Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Version'), 'Version', '__httpeuclid_esa_orgschemasyssgs_curation_Version', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 34, 3), )

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Contact'), 'Contact', '__httpeuclid_esa_orgschemasyssgs_curation_Contact', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 35, 3), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element Rights uses Python identifier Rights
    __Rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Rights'), 'Rights', '__httpeuclid_esa_orgschemasyssgs_curation_Rights', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 36, 3), )

    
    Rights = property(__Rights.value, __Rights.set, None, None)

    
    # Element Date uses Python identifier Date
    __Date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Date'), 'Date', '__httpeuclid_esa_orgschemasyssgs_curation_Date', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 37, 3), )

    
    Date = property(__Date.value, __Date.set, None, None)

    
    # Element PublisherDID uses Python identifier PublisherDID
    __PublisherDID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PublisherDID'), 'PublisherDID', '__httpeuclid_esa_orgschemasyssgs_curation_PublisherDID', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 38, 3), )

    
    PublisherDID = property(__PublisherDID.value, __PublisherDID.set, None, None)

    _ElementMap.update({
        __Publisher.name() : __Publisher,
        __PublisherID.name() : __PublisherID,
        __Reference.name() : __Reference,
        __Version.name() : __Version,
        __Contact.name() : __Contact,
        __Rights.name() : __Rights,
        __Date.name() : __Date,
        __PublisherDID.name() : __PublisherDID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'curation', curation)


# Complex type {http://euclid.esa.org/schema/sys/sgs}contact with content type ELEMENT_ONLY
class contact (pyxb.binding.basis.complexTypeDefinition):
    """This type defines the coordinates of the organism/people in charge of the curation of the corresponding data."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'contact')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 41, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemasyssgs_contact_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 47, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Email uses Python identifier Email
    __Email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Email'), 'Email', '__httpeuclid_esa_orgschemasyssgs_contact_Email', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 48, 3), )

    
    Email = property(__Email.value, __Email.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Email.name() : __Email
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'contact', contact)


# Complex type {http://euclid.esa.org/schema/sys/sgs}product with content type ELEMENT_ONLY
class product (pyxb.binding.basis.complexTypeDefinition):
    """Descriptor for product."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'product')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 53, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemasyssgs_product_Name', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 58, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Description'), 'Description', '__httpeuclid_esa_orgschemasyssgs_product_Description', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 59, 3), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__httpeuclid_esa_orgschemasyssgs_product_Type', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 60, 3), )

    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Element ProductionDate uses Python identifier ProductionDate
    __ProductionDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ProductionDate'), 'ProductionDate', '__httpeuclid_esa_orgschemasyssgs_product_ProductionDate', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 61, 3), )

    
    ProductionDate = property(__ProductionDate.value, __ProductionDate.set, None, None)

    
    # Element Producer uses Python identifier Producer
    __Producer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Producer'), 'Producer', '__httpeuclid_esa_orgschemasyssgs_product_Producer', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 62, 3), )

    
    Producer = property(__Producer.value, __Producer.set, None, u'Creator of the data.')

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Source'), 'Source', '__httpeuclid_esa_orgschemasyssgs_product_Source', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 68, 4), )

    
    Source = property(__Source.value, __Source.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Description.name() : __Description,
        __Type.name() : __Type,
        __ProductionDate.name() : __ProductionDate,
        __Producer.name() : __Producer,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'product', product)


# Complex type {http://euclid.esa.org/schema/sys/sgs}fileDescriptor with content type ELEMENT_ONLY
class fileDescriptor (pyxb.binding.basis.complexTypeDefinition):
    """
				Descriptor of a file used to store transient data such as data managed by the IAL
				until moved to the workspace as input for the pipeline processing tasks.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fileDescriptor')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 73, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpeuclid_esa_orgschemasyssgs_fileDescriptor_Id', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 81, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element Filename uses Python identifier Filename
    __Filename = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Filename'), 'Filename', '__httpeuclid_esa_orgschemasyssgs_fileDescriptor_Filename', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 82, 3), )

    
    Filename = property(__Filename.value, __Filename.set, None, None)

    
    # Element Path uses Python identifier Path
    __Path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Path'), 'Path', '__httpeuclid_esa_orgschemasyssgs_fileDescriptor_Path', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 83, 3), )

    
    Path = property(__Path.value, __Path.set, None, None)

    
    # Element StorageId uses Python identifier StorageId
    __StorageId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'StorageId'), 'StorageId', '__httpeuclid_esa_orgschemasyssgs_fileDescriptor_StorageId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 84, 3), )

    
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


# Complex type {http://euclid.esa.org/schema/sys/sgs}taskProduct with content type ELEMENT_ONLY
class taskProduct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://euclid.esa.org/schema/sys/sgs}taskProduct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'taskProduct')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 89, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpeuclid_esa_orgschemasyssgs_taskProduct_Id', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 91, 12), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element PortName uses Python identifier PortName
    __PortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PortName'), 'PortName', '__httpeuclid_esa_orgschemasyssgs_taskProduct_PortName', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 92, 12), )

    
    PortName = property(__PortName.value, __PortName.set, None, None)

    
    # Element ProductType uses Python identifier ProductType
    __ProductType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ProductType'), 'ProductType', '__httpeuclid_esa_orgschemasyssgs_taskProduct_ProductType', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 93, 12), )

    
    ProductType = property(__ProductType.value, __ProductType.set, None, None)

    
    # Element ProductId uses Python identifier ProductId
    __ProductId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ProductId'), 'ProductId', '__httpeuclid_esa_orgschemasyssgs_taskProduct_ProductId', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 94, 12), )

    
    ProductId = property(__ProductId.value, __ProductId.set, None, None)

    
    # Element LocalFile uses Python identifier LocalFile
    __LocalFile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'LocalFile'), 'LocalFile', '__httpeuclid_esa_orgschemasyssgs_taskProduct_LocalFile', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 95, 12), )

    
    LocalFile = property(__LocalFile.value, __LocalFile.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __PortName.name() : __PortName,
        __ProductType.name() : __ProductType,
        __ProductId.name() : __ProductId,
        __LocalFile.name() : __LocalFile
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'taskProduct', taskProduct)


# Complex type {http://euclid.esa.org/schema/sys/sgs}dataFileNameList with content type ELEMENT_ONLY
class dataFileNameList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://euclid.esa.org/schema/sys/sgs}dataFileNameList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataFileNameList')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 100, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpeuclid_esa_orgschemasyssgs_dataFileNameList_Id', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 102, 12), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element FileName uses Python identifier FileName
    __FileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'FileName'), 'FileName', '__httpeuclid_esa_orgschemasyssgs_dataFileNameList_FileName', True, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 103, 12), )

    
    FileName = property(__FileName.value, __FileName.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __FileName.name() : __FileName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'dataFileNameList', dataFileNameList)




ivoaUCDParam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=ivoaUCDParam, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 21, 3)))

ivoaUCDParam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'UCD'), pyxb.binding.datatypes.string, scope=ivoaUCDParam, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 22, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ivoaUCDParam._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 21, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ivoaUCDParam._UseForTag(pyxb.namespace.ExpandedName(None, u'UCD')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 22, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ivoaUCDParam._Automaton = _BuildAutomaton()




curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Publisher'), ivoaUCDParam, scope=curation, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 31, 3)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PublisherID'), ivoaUCDParam, scope=curation, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 32, 3)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Reference'), ivoaUCDParam, scope=curation, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 33, 3)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Version'), ivoaUCDParam, scope=curation, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 34, 3)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Contact'), contact, scope=curation, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 35, 3)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Rights'), ivoaUCDParam, scope=curation, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 36, 3)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Date'), pyxb.binding.datatypes.dateTime, scope=curation, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 37, 3)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PublisherDID'), ivoaUCDParam, scope=curation, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 38, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 31, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 32, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 33, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 34, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 35, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 36, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 37, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 38, 3))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, u'Publisher')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 31, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, u'PublisherID')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 32, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, u'Reference')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 33, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, u'Version')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 34, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, u'Contact')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 35, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, u'Rights')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 36, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, u'Date')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 37, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, u'PublisherDID')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 38, 3))
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
curation._Automaton = _BuildAutomaton_()




contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=contact, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 47, 3)))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Email'), emailAddress, scope=contact, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 48, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 47, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 48, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(contact._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 47, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(contact._UseForTag(pyxb.namespace.ExpandedName(None, u'Email')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 48, 3))
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
contact._Automaton = _BuildAutomaton_2()




product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=product, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 58, 3)))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Description'), pyxb.binding.datatypes.string, scope=product, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 59, 3)))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Type'), pyxb.binding.datatypes.string, scope=product, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 60, 3)))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ProductionDate'), _ImportedBinding_euclid_dm__sys.systemDateTime, scope=product, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 61, 3)))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Producer'), _ImportedBinding_euclid_dm__sys.infraName, scope=product, documentation=u'Creator of the data.', location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 62, 3)))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Source'), _ImportedBinding_euclid_dm__dss.dataContainer, scope=product, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 68, 4)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(product._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 58, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(product._UseForTag(pyxb.namespace.ExpandedName(None, u'Description')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 59, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(product._UseForTag(pyxb.namespace.ExpandedName(None, u'Type')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 60, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(product._UseForTag(pyxb.namespace.ExpandedName(None, u'ProductionDate')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 61, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(product._UseForTag(pyxb.namespace.ExpandedName(None, u'Producer')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 62, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(product._UseForTag(pyxb.namespace.ExpandedName(None, u'Source')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 68, 4))
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
product._Automaton = _BuildAutomaton_3()




fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Id'), pyxb.binding.datatypes.string, scope=fileDescriptor, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 81, 3)))

fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Filename'), pyxb.binding.datatypes.string, scope=fileDescriptor, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 82, 3)))

fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Path'), pyxb.binding.datatypes.string, scope=fileDescriptor, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 83, 3)))

fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'StorageId'), pyxb.binding.datatypes.string, scope=fileDescriptor, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 84, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(None, u'Id')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 81, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(None, u'Filename')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 82, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(None, u'Path')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 83, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(None, u'StorageId')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 84, 3))
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




taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Id'), pyxb.binding.datatypes.string, scope=taskProduct, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 91, 12)))

taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PortName'), pyxb.binding.datatypes.string, scope=taskProduct, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 92, 12)))

taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ProductType'), pyxb.binding.datatypes.string, scope=taskProduct, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 93, 12)))

taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ProductId'), pyxb.binding.datatypes.string, scope=taskProduct, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 94, 12)))

taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LocalFile'), fileDescriptor, scope=taskProduct, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 95, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 93, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 94, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 95, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(taskProduct._UseForTag(pyxb.namespace.ExpandedName(None, u'Id')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 91, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(taskProduct._UseForTag(pyxb.namespace.ExpandedName(None, u'PortName')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 92, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(taskProduct._UseForTag(pyxb.namespace.ExpandedName(None, u'ProductType')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 93, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(taskProduct._UseForTag(pyxb.namespace.ExpandedName(None, u'ProductId')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 94, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(taskProduct._UseForTag(pyxb.namespace.ExpandedName(None, u'LocalFile')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 95, 12))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
taskProduct._Automaton = _BuildAutomaton_5()




dataFileNameList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Id'), pyxb.binding.datatypes.string, scope=dataFileNameList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 102, 12)))

dataFileNameList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'FileName'), _ImportedBinding_euclid_dm__sys.dataFileName, scope=dataFileNameList, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 103, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 103, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(dataFileNameList._UseForTag(pyxb.namespace.ExpandedName(None, u'Id')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 102, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dataFileNameList._UseForTag(pyxb.namespace.ExpandedName(None, u'FileName')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/sys/sgs/euc-test-sgs.xsd', 103, 12))
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
dataFileNameList._Automaton = _BuildAutomaton_6()

