from xml.dom import minidom
import os

#print(os.getcwd())
os.chdir('Practical14')

'''C:/Users/玄青石/Desktop/收藏/IBI_2024-25/IBI1_2024-25/

'''
import xml.dom.minidom
import xml.sax
import time

# DOM 
class DOMParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.result = {"molecular_function": {"term": None, "count": 0},
                       "biological_process": {"term": None, "count": 0},
                       "cellular_component": {"term": None, "count": 0}}

    def parse(self):
        dom_tree = xml.dom.minidom.parse(self.file_path)
        terms = dom_tree.getElementsByTagName("term")
        for term in terms:
            namespace = term.getElementsByTagName("namespace")[0].childNodes[0].data
            if namespace in ["molecular_function", "biological_process", "cellular_component"]:
                is_a_elements = term.getElementsByTagName("is_a")
                count = len(is_a_elements)
                if count > self.result[namespace]["count"]:
                    self.result[namespace]["term"] = term.getElementsByTagName("id")[0].childNodes[0].data#explor the tree
                    self.result[namespace]["count"] = count

# SAX
class SAXHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.result = {"molecular_function": {"term": None, "count": 0},
                       "biological_process": {"term": None, "count": 0},
                       "cellular_component": {"term": None, "count": 0}}
        self.current_tag = ""
        self.current_namespace = ""
        self.current_term = ""
        self.current_count = 0

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if self.current_tag == "term":
            self.current_namespace = ""
            self.current_term= ""
            self.current_count = 0
        if self.current_tag == "is_a":
            self.current_count += 1
            

    def endElement(self, tag):
        if tag == "term":
            ns = self.current_namespace.strip()
            term_id = self.current_term.strip()
            if ns in self.result and term_id:
                if self.current_count > self.result[ns]["count"]:
                    self.result[ns]["term"] = term_id
                    self.result[ns]["count"] = self.current_count
            # Reset current values for the next term
            self.current_namespace = ""
            self.current_term = ""
            self.current_count = 0
        self.current_tag = ""  # Reset current tag after processing
        

    def characters(self, content):
        if self.current_tag == "namespace":
            self.current_namespace += content
        elif self.current_tag == "id":
            self.current_term += content.strip()  # Clean up the term ID
        
        

def sax_parse(file_path):#returns the result of SAX parsing
    handler = SAXHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    return handler.result

if __name__ == "__main__":
    file_path = "go_obo.xml"

    # DOM
    start_time = time.time()
    dom_parser = DOMParser(file_path)
    dom_parser.parse()
    dom_result = dom_parser.result
    dom_time = (time.time() - start_time)
    print("The result of DOM:")
    for namespace, info in dom_result.items():
        print(f"{namespace}: {info['term']}  {info['count']}")

    # SAX
    start_time = time.time()
    sax_result = sax_parse(file_path)
    sax_time = (time.time() - start_time)
    print("\nThe result of SAX:")
    for namespace, info in sax_result.items():
        print(f"{namespace}: {info['term']}  {info['count']}")

    # compare time usage
    print("\ntime comparism:")
    print(f"The time of DOM:{dom_time} seconds")
    print(f"The time of SAX:{sax_time} seconds")
    if dom_time < sax_time:
        print("DOM is faster by {:.2f} seconds".format(sax_time - dom_time))
    else:
        print("SAX is faster by {:.2f} seconds".format(dom_time - sax_time))
    