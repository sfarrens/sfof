# /home/sartor/pymodule/euclid/dm/Interfaces/pro/le3/cog_stub.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4687b8155e81fd81c5e2d90247d5d9c75d6ec333
# Generated 2014-07-24 16:26:39.933370 by PyXB version 1.2.3
# Namespace http://euclid.esa.org/schema/Interfaces/pro/le3/cog

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
import euclid.dm._cog as _ImportedBinding_euclid_dm__cog

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/Interfaces/pro/le3/cog', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-in.xsd', 9, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/Interfaces/pro/le3/cog}Catalog uses Python identifier Catalog
    __Catalog = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Catalog'), 'Catalog', '__httpeuclid_esa_orgschemaInterfacesprole3cog_CTD_ANON_httpeuclid_esa_orgschemaInterfacesprole3cogCatalog', False, pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-in.xsd', 11, 16), )

    
    Catalog = property(__Catalog.value, __Catalog.set, None, None)

    
    # Element {http://euclid.esa.org/schema/Interfaces/pro/le3/cog}Params uses Python identifier Params
    __Params = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Params'), 'Params', '__httpeuclid_esa_orgschemaInterfacesprole3cog_CTD_ANON_httpeuclid_esa_orgschemaInterfacesprole3cogParams', False, pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-in.xsd', 12, 16), )

    
    Params = property(__Params.value, __Params.set, None, None)

    _ElementMap.update({
        __Catalog.name() : __Catalog,
        __Params.name() : __Params
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-out.xsd', 9, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/Interfaces/pro/le3/cog}Clusters uses Python identifier Clusters
    __Clusters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Clusters'), 'Clusters', '__httpeuclid_esa_orgschemaInterfacesprole3cog_CTD_ANON__httpeuclid_esa_orgschemaInterfacesprole3cogClusters', False, pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-out.xsd', 11, 16), )

    
    Clusters = property(__Clusters.value, __Clusters.set, None, None)

    
    # Element {http://euclid.esa.org/schema/Interfaces/pro/le3/cog}Members uses Python identifier Members
    __Members = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Members'), 'Members', '__httpeuclid_esa_orgschemaInterfacesprole3cog_CTD_ANON__httpeuclid_esa_orgschemaInterfacesprole3cogMembers', False, pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-out.xsd', 12, 16), )

    
    Members = property(__Members.value, __Members.set, None, None)

    _ElementMap.update({
        __Clusters.name() : __Clusters,
        __Members.name() : __Members
    })
    _AttributeMap.update({
        
    })



GalClusterInput = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GalClusterInput'), CTD_ANON, location=pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-in.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', GalClusterInput.name().localName(), GalClusterInput)

GalClusterOutput = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GalClusterOutput'), CTD_ANON_, location=pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-out.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', GalClusterOutput.name().localName(), GalClusterOutput)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Catalog'), _ImportedBinding_euclid_dm__cog.fofClusterInputCatalog, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-in.xsd', 11, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Params'), _ImportedBinding_euclid_dm__cog.fofParams, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-in.xsd', 12, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Catalog')), pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-in.xsd', 11, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Params')), pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-in.xsd', 12, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Clusters'), _ImportedBinding_euclid_dm__cog.catalogClusterLe3FitFile, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-out.xsd', 11, 16)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Members'), _ImportedBinding_euclid_dm__cog.catalogCluster_membersLe3FitFile, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-out.xsd', 12, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Clusters')), pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-out.xsd', 11, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Members')), pyxb.utils.utility.Location('/home/sartor/workspace/EUCLID/svn_tot/schema/branches/challenge4/Interfaces/pro/le3/cog/euc-test-le3-cog-out.xsd', 12, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()

