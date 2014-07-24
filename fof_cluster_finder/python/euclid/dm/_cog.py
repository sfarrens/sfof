# /home/sartor/pymodule/euclid/dm/_cog.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a17fe44f5818a6dad4c3af2f6274ac08c385d7a5
# Generated 2014-07-23 16:11:22.132887 by PyXB version 1.2.3
# Namespace http://euclid.esa.org/schema/pro/le3/cog [xmlns:cog]

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
import euclid.dm._fit as _ImportedBinding_euclid_dm__fit

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/le3/cog', create_if_missing=True)
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


# Complex type {http://euclid.esa.org/schema/pro/le3/cog}fofClusterInputCatalog with content type ELEMENT_ONLY
class fofClusterInputCatalog (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://euclid.esa.org/schema/pro/le3/cog}fofClusterInputCatalog with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fofClusterInputCatalog')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 44, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PhotZcatalog uses Python identifier PhotZcatalog
    __PhotZcatalog = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PhotZcatalog'), 'PhotZcatalog', '__httpeuclid_esa_orgschemaprole3cog_fofClusterInputCatalog_PhotZcatalog', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 46, 12), )

    
    PhotZcatalog = property(__PhotZcatalog.value, __PhotZcatalog.set, None, None)

    
    # Element SpecZcatalog uses Python identifier SpecZcatalog
    __SpecZcatalog = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SpecZcatalog'), 'SpecZcatalog', '__httpeuclid_esa_orgschemaprole3cog_fofClusterInputCatalog_SpecZcatalog', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 47, 12), )

    
    SpecZcatalog = property(__SpecZcatalog.value, __SpecZcatalog.set, None, None)

    _ElementMap.update({
        __PhotZcatalog.name() : __PhotZcatalog,
        __SpecZcatalog.name() : __SpecZcatalog
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'fofClusterInputCatalog', fofClusterInputCatalog)


# Complex type {http://euclid.esa.org/schema/pro/le3/cog}fofParams with content type ELEMENT_ONLY
class fofParams (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://euclid.esa.org/schema/pro/le3/cog}fofParams with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fofParams')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 51, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element link_mode uses Python identifier link_mode
    __link_mode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'link_mode'), 'link_mode', '__httpeuclid_esa_orgschemaprole3cog_fofParams_link_mode', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 53, 12), )

    
    link_mode = property(__link_mode.value, __link_mode.set, None, None)

    
    # Element print_bin_data uses Python identifier print_bin_data
    __print_bin_data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'print_bin_data'), 'print_bin_data', '__httpeuclid_esa_orgschemaprole3cog_fofParams_print_bin_data', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 54, 12), )

    
    print_bin_data = property(__print_bin_data.value, __print_bin_data.set, None, None)

    
    # Element link_r uses Python identifier link_r
    __link_r = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'link_r'), 'link_r', '__httpeuclid_esa_orgschemaprole3cog_fofParams_link_r', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 55, 12), )

    
    link_r = property(__link_r.value, __link_r.set, None, None)

    
    # Element link_z uses Python identifier link_z
    __link_z = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'link_z'), 'link_z', '__httpeuclid_esa_orgschemaprole3cog_fofParams_link_z', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 56, 12), )

    
    link_z = property(__link_z.value, __link_z.set, None, None)

    
    # Element kdtree_depth uses Python identifier kdtree_depth
    __kdtree_depth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'kdtree_depth'), 'kdtree_depth', '__httpeuclid_esa_orgschemaprole3cog_fofParams_kdtree_depth', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 57, 12), )

    
    kdtree_depth = property(__kdtree_depth.value, __kdtree_depth.set, None, None)

    
    # Element min_n_gal uses Python identifier min_n_gal
    __min_n_gal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'min_n_gal'), 'min_n_gal', '__httpeuclid_esa_orgschemaprole3cog_fofParams_min_n_gal', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 58, 12), )

    
    min_n_gal = property(__min_n_gal.value, __min_n_gal.set, None, None)

    
    # Element z_min uses Python identifier z_min
    __z_min = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'z_min'), 'z_min', '__httpeuclid_esa_orgschemaprole3cog_fofParams_z_min', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 59, 12), )

    
    z_min = property(__z_min.value, __z_min.set, None, None)

    
    # Element z_max uses Python identifier z_max
    __z_max = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'z_max'), 'z_max', '__httpeuclid_esa_orgschemaprole3cog_fofParams_z_max', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 60, 12), )

    
    z_max = property(__z_max.value, __z_max.set, None, None)

    
    # Element z_bin_size uses Python identifier z_bin_size
    __z_bin_size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'z_bin_size'), 'z_bin_size', '__httpeuclid_esa_orgschemaprole3cog_fofParams_z_bin_size', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 61, 12), )

    
    z_bin_size = property(__z_bin_size.value, __z_bin_size.set, None, None)

    
    # Element z_ref uses Python identifier z_ref
    __z_ref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'z_ref'), 'z_ref', '__httpeuclid_esa_orgschemaprole3cog_fofParams_z_ref', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 62, 12), )

    
    z_ref = property(__z_ref.value, __z_ref.set, None, None)

    
    # Element c uses Python identifier c
    __c = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'c'), 'c', '__httpeuclid_esa_orgschemaprole3cog_fofParams_c', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 63, 12), )

    
    c = property(__c.value, __c.set, None, None)

    
    # Element H0 uses Python identifier H0
    __H0 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'H0'), 'H0', '__httpeuclid_esa_orgschemaprole3cog_fofParams_H0', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 64, 12), )

    
    H0 = property(__H0.value, __H0.set, None, None)

    
    # Element omega_m uses Python identifier omega_m
    __omega_m = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'omega_m'), 'omega_m', '__httpeuclid_esa_orgschemaprole3cog_fofParams_omega_m', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 65, 12), )

    
    omega_m = property(__omega_m.value, __omega_m.set, None, None)

    
    # Element omega_l uses Python identifier omega_l
    __omega_l = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'omega_l'), 'omega_l', '__httpeuclid_esa_orgschemaprole3cog_fofParams_omega_l', False, pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 66, 12), )

    
    omega_l = property(__omega_l.value, __omega_l.set, None, None)

    _ElementMap.update({
        __link_mode.name() : __link_mode,
        __print_bin_data.name() : __print_bin_data,
        __link_r.name() : __link_r,
        __link_z.name() : __link_z,
        __kdtree_depth.name() : __kdtree_depth,
        __min_n_gal.name() : __min_n_gal,
        __z_min.name() : __z_min,
        __z_max.name() : __z_max,
        __z_bin_size.name() : __z_bin_size,
        __z_ref.name() : __z_ref,
        __c.name() : __c,
        __H0.name() : __H0,
        __omega_m.name() : __omega_m,
        __omega_l.name() : __omega_l
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'fofParams', fofParams)


# Complex type {http://euclid.esa.org/schema/pro/le3/cog}catalogGalaxyPhotoZLe3FitFile with content type ELEMENT_ONLY
class catalogGalaxyPhotoZLe3FitFile (_ImportedBinding_euclid_dm__fit.fitsFile):
    """Complex type {http://euclid.esa.org/schema/pro/le3/cog}catalogGalaxyPhotoZLe3FitFile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogGalaxyPhotoZLe3FitFile')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 17, 4)
    _ElementMap = _ImportedBinding_euclid_dm__fit.fitsFile._ElementMap.copy()
    _AttributeMap = _ImportedBinding_euclid_dm__fit.fitsFile._AttributeMap.copy()
    # Base type is _ImportedBinding_euclid_dm__fit.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', _ImportedBinding_euclid_dm__fit.fitsFormatIdentifier, fixed=True, unicode_default=u'le3.catalog.galaxy.photoz', required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 23, 16)
    __format._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 23, 16)
    
    format = property(__format.value, __format.set, None, None)

    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', _ImportedBinding_euclid_dm__fit.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 25, 16)
    __version._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 25, 16)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', u'catalogGalaxyPhotoZLe3FitFile', catalogGalaxyPhotoZLe3FitFile)


# Complex type {http://euclid.esa.org/schema/pro/le3/cog}catalogGalaxySpecZLe3FitFile with content type ELEMENT_ONLY
class catalogGalaxySpecZLe3FitFile (_ImportedBinding_euclid_dm__fit.fitsFile):
    """Complex type {http://euclid.esa.org/schema/pro/le3/cog}catalogGalaxySpecZLe3FitFile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogGalaxySpecZLe3FitFile')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 31, 4)
    _ElementMap = _ImportedBinding_euclid_dm__fit.fitsFile._ElementMap.copy()
    _AttributeMap = _ImportedBinding_euclid_dm__fit.fitsFile._AttributeMap.copy()
    # Base type is _ImportedBinding_euclid_dm__fit.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', _ImportedBinding_euclid_dm__fit.fitsFormatIdentifier, fixed=True, unicode_default=u'le3.catalog.galaxy.specz', required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 37, 16)
    __format._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 37, 16)
    
    format = property(__format.value, __format.set, None, None)

    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', _ImportedBinding_euclid_dm__fit.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 39, 16)
    __version._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 39, 16)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', u'catalogGalaxySpecZLe3FitFile', catalogGalaxySpecZLe3FitFile)


# Complex type {http://euclid.esa.org/schema/pro/le3/cog}catalogClusterLe3FitFile with content type ELEMENT_ONLY
class catalogClusterLe3FitFile (_ImportedBinding_euclid_dm__fit.fitsFile):
    """Complex type {http://euclid.esa.org/schema/pro/le3/cog}catalogClusterLe3FitFile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogClusterLe3FitFile')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 70, 4)
    _ElementMap = _ImportedBinding_euclid_dm__fit.fitsFile._ElementMap.copy()
    _AttributeMap = _ImportedBinding_euclid_dm__fit.fitsFile._AttributeMap.copy()
    # Base type is _ImportedBinding_euclid_dm__fit.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', _ImportedBinding_euclid_dm__fit.fitsFormatIdentifier, fixed=True, unicode_default=u'le3.catalog.cluster', required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 76, 16)
    __format._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 76, 16)
    
    format = property(__format.value, __format.set, None, None)

    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', _ImportedBinding_euclid_dm__fit.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 78, 16)
    __version._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 78, 16)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', u'catalogClusterLe3FitFile', catalogClusterLe3FitFile)


# Complex type {http://euclid.esa.org/schema/pro/le3/cog}catalogCluster_membersLe3FitFile with content type ELEMENT_ONLY
class catalogCluster_membersLe3FitFile (_ImportedBinding_euclid_dm__fit.fitsFile):
    """Complex type {http://euclid.esa.org/schema/pro/le3/cog}catalogCluster_membersLe3FitFile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogCluster_membersLe3FitFile')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 84, 4)
    _ElementMap = _ImportedBinding_euclid_dm__fit.fitsFile._ElementMap.copy()
    _AttributeMap = _ImportedBinding_euclid_dm__fit.fitsFile._AttributeMap.copy()
    # Base type is _ImportedBinding_euclid_dm__fit.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', _ImportedBinding_euclid_dm__fit.fitsFormatIdentifier, fixed=True, unicode_default=u'le3.catalog.cluster_members', required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 90, 16)
    __format._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 90, 16)
    
    format = property(__format.value, __format.set, None, None)

    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', _ImportedBinding_euclid_dm__fit.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 92, 16)
    __version._UseLocation = pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 92, 16)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', u'catalogCluster_membersLe3FitFile', catalogCluster_membersLe3FitFile)




fofClusterInputCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PhotZcatalog'), catalogGalaxyPhotoZLe3FitFile, scope=fofClusterInputCatalog, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 46, 12)))

fofClusterInputCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SpecZcatalog'), catalogGalaxySpecZLe3FitFile, scope=fofClusterInputCatalog, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 47, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fofClusterInputCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'PhotZcatalog')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 46, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fofClusterInputCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'SpecZcatalog')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 47, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
fofClusterInputCatalog._Automaton = _BuildAutomaton()




fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'link_mode'), pyxb.binding.datatypes.string, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 53, 12), fixed=True, unicode_default=u'dynamic'))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'print_bin_data'), pyxb.binding.datatypes.string, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 54, 12), fixed=True, unicode_default=u'no'))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'link_r'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 55, 12)))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'link_z'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 56, 12)))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'kdtree_depth'), pyxb.binding.datatypes.integer, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 57, 12)))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'min_n_gal'), pyxb.binding.datatypes.int, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 58, 12)))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'z_min'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 59, 12)))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'z_max'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 60, 12)))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'z_bin_size'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 61, 12)))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'z_ref'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 62, 12)))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'c'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 63, 12), fixed=True, unicode_default=u'2.997e5'))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'H0'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 64, 12), fixed=True, unicode_default=u'100.0'))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'omega_m'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 65, 12), fixed=True, unicode_default=u'0.3'))

fofParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'omega_l'), pyxb.binding.datatypes.double, scope=fofParams, location=pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 66, 12), fixed=True, unicode_default=u'0.7'))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'link_mode')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 53, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'print_bin_data')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 54, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'link_r')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 55, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'link_z')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 56, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'kdtree_depth')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 57, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'min_n_gal')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 58, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'z_min')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 59, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'z_max')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 60, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'z_bin_size')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 61, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'z_ref')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 62, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'c')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 63, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'H0')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 64, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'omega_m')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 65, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fofParams._UseForTag(pyxb.namespace.ExpandedName(None, u'omega_l')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 66, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
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
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
fofParams._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(catalogGalaxyPhotoZLe3FitFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 21, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
catalogGalaxyPhotoZLe3FitFile._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(catalogGalaxySpecZLe3FitFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 35, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
catalogGalaxySpecZLe3FitFile._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(catalogClusterLe3FitFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 74, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
catalogClusterLe3FitFile._Automaton = _BuildAutomaton_4()




def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(catalogCluster_membersLe3FitFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), pyxb.utils.utility.Location(u'/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Dictionary/pro/le3/cog/euc-test-le3-cog.xsd', 88, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
catalogCluster_membersLe3FitFile._Automaton = _BuildAutomaton_5()

