from binaryninja import show_html_report, show_plain_text_report
from mako.template import Template
from mako import exceptions
import os

name = os.path.dirname(os.path.realpath(__file__)).split('/')[-1]
template = Template(filename=(os.path.dirname(os.path.realpath(__file__)) + '/writeup.mhtml'))

def render(bv):
    try:
        show_html_report("{} Writeup".format(name), template.render(bv=bv))
    except:
        show_plain_text_report("{}: Error in Rendering".format(name), exceptions.text_error_template().render())
