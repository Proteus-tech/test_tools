import simplejson
import os

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
    
from django.utils.xmlutils import SimplerXMLGenerator
from django.utils.encoding import smart_unicode
from django.conf import settings

    
class DictToXML(object):
    def __init__(self, data_dict, root_element='root', element='element'):
        self.data_dict = data_dict
        self.root_element = root_element
        self.element = element

    def _to_xml(self, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                xml.startElement(self.element, {})
                self._to_xml(xml, item)
                xml.endElement(self.element)
        elif isinstance(data, dict):
            for key, value in data.iteritems():
                xml.startElement(key, {})
                self._to_xml(xml, value)
                xml.endElement(key)
        else:
            xml.characters(smart_unicode(data))

    def render(self,):
        stream = StringIO.StringIO()
        xml = SimplerXMLGenerator(stream, "utf-8")
        xml.startDocument()
        xml.startElement(self.root_element, {})
        self._to_xml(xml, self.data_dict)
        xml.endElement(self.root_element)
        xml.endDocument()
        return stream.getvalue()

def get_data(*args, **kwargs):

    format = kwargs.get('format', '')
    data_dict = kwargs.get('data', '')
    if not data_dict:
        return data_dict

    if format == 'json':
        return simplejson.dumps(data_dict)
    if format == 'xml':
        if 'format' in kwargs.keys():
            kwargs.pop('format')
        if 'data' in kwargs.keys():
            kwargs.pop('data')
        return DictToXML(data_dict, *args, **kwargs).render()

    return data_dict

  