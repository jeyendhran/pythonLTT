from xml.sax.handler import ContentHandler
from xml.sax import make_parser

class MyPlaneParser(ContentHandler):

    def startElement(self, name, attrs):
        if name == 'ad':
            self.id = attrs.get('id')
                

    def endElement(self, name):
        if name == 'ad':
            print("ID is",self.id)


plane = MyPlaneParser()
saxparser = make_parser()
saxparser.setContentHandler(plane)
xmlfile = open("sample_xml.xml",'r')
saxparser.parse(xmlfile)
xmlfile.close()