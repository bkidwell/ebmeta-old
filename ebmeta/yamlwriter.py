import re
from string import Template
import yaml

#yaml_simple = re.compile("^[A-Za-z0-9\.]+$")
yaml_simple = re.compile("^[0-9\.]+$")
yaml_newline = re.compile("^", re.MULTILINE)
def yaml_value(txt, multiline=False):
    if txt == None: return '~'
    if len(txt) == 0: return '~'
    if type(txt) is list:
        return '[' +   ', '.join(yaml_value(x) for x in txt)   + ']'
    if yaml_simple.match(txt): return txt
    if multiline:
        return ">\n" + yaml_newline.sub("  ", txt)
    else:
        return '"' + txt.replace('"', '\\x22') + '"'

def opf_to_yaml(opf, template_str):
    # templ = template.get_file_content('metadata.yaml')
    d = dict()
    for key in opf.keys():
        d[key.replace(' ', '_')] = yaml_value(opf[key], key == 'description')
    return Template(template_str).substitute(d)
