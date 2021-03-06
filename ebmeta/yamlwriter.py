import re
from string import Template
import yaml

#yaml_simple = re.compile("^[A-Za-z0-9\.]+$")
yaml_simple = re.compile("^[0-9\.]+$")
yaml_newline = re.compile("^", re.MULTILINE)
def yaml_value(txt, multiline=False):
    if txt == None: return u'~'
    print "-- " + repr(txt)
    if len(txt) == 0: return u'~'
    if type(txt) is list:
        return u'[' +   u', '.join(yaml_value(x) for x in txt)   + u']'
    if yaml_simple.match(txt): return txt
    if multiline:
        return u"|\n" + yaml_newline.sub(u"  ", txt)
    else:
        # print "::: " + txt
        # a = txt.decode("utf-8", 'replace')
        # a = a.replace(u'"', u'\\x22')
        return u'"' + txt + u'"'

def opf_to_yaml(opf, template_str):
    # templ = template.get_file_content('metadata.yaml')
    d = dict()
    for key in opf.keys():
        d[key.replace(u' ', u'_')] = yaml_value(opf[key], key == 'description')
    return Template(template_str).substitute(d)
