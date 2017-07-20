from binaryninja import show_html_report, show_plain_text_report, show_markdown_report
from mako.template import Template
from mako import exceptions
import os, glob

name = os.path.dirname(os.path.realpath(__file__)).split('/')[-1]
template = Template(filename=(os.path.dirname(os.path.realpath(__file__)) + '/writeup.md'))

def render(bv):
    try:
        show_markdown_report("{} Writeup".format(name), template.render(bv=bv))
    except:
        show_plain_text_report("{}: Error in Rendering".format(name), exceptions.text_error_template().render())
