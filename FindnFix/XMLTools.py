# import xml.etree.ElementTree as ET
# from xml.dom import minidom as MD
from lxml import etree


def file_to_tree(xmlFile):
    parser = etree.XMLParser(remove_blank_text=True, ns_clean=True, remove_comments=True)
    return etree.parse(xmlFile, parser)


def strip_comments(tree):
    comments = tree.xpath('//comment()')

    for c in comments:
        p = c.getparent()
        if p is not None:
            p.remove(c)

    return tree


def pprint(tree):
    etree.tostring(tree, pretty_print=True)






# def strip_ns_prefix(tree):
#     #iterate through only element nodes (skip comment node, text node, etc) :
#     for element in tree.xpath('descendant-or-self::*'):
#         #if element has prefix...
#         if element.prefix:
#             #replace element name with it's local name
#             element.tag = etree.QName(element).localname
#     return tree

def printXmlNoComment(xmlFile):
    tree = etree.parse(xmlFile)

    comments = tree.xpath('//comment()')

    for c in comments:
        p = c.getparent()
        if p is not None:
            p.remove(c)

    print etree.tostring(tree)


def findElements(xmlFile, element):
    tree = etree.parse(xmlFile)
    parser = etree.XMLParser(ns_clean=True)
    print('parser:::', len(parser.error_log))
    #print(etree.tostring(tree))
    new_tree = tree #strip_ns_prefix(tree)
    return(new_tree.xpath('{0}'.format(element))) #, namespaces='http://java.sun.com/xml/ns/javaee'))

def findElementsHack(xmlFile, element):
    tree = etree.parse(xmlFile)
    parser = etree.XMLParser(ns_clean=True)
    print('parser:::', len(parser.error_log))
    #print(etree.tostring(tree))
    new_tree = tree #strip_ns_prefix(tree)
    return(new_tree.xpath('{0}'.format(element), namespaces={"d" : 'http://java.sun.com/xml/ns/javaee'}))


def findAttributes(xmlFile, element, attribute):
    results = []
    for el in findElements(xmlFile, element):
        att = el.xpath('./@{0}'.format(attribute))
        results.append((att, el))
    return(results)


def findSubElements(xmlFile, element, sub):
    elements = findElementsHack(xmlFile, element)
    print('ele:::', elements)
    results = []
    for el in elements:
        subel = el.xpath('{}'.format(sub))
        results.append((subel, el))
    return(results)




def etToString(elemTree):
    return(etree.tostring(elemTree))
#     rough_string = ET.tostring(elemTree, 'utf-8')
#     reparsed = MD.parseString(rough_string)
#     return (reparsed.toprettyxml(indent="    ", newl=''))
#
#
# def findAttribute(element, attribute):
#
#
#
#     return attributeValue
