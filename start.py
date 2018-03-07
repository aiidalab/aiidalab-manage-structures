import ipywidgets as ipw

def get_start_widget(appbase, jupbase):
    #http://fontawesome.io/icons/
    template = """
    <table>
    <td valign="top"><ul>
    <li><a href="{appbase}/upload_structure.ipynb" target="_blank">Upload structures</a>
    </ul></td>
    <td valign="top"><ul>
    <li><a href="{appbase}/import_from_cod.ipynb" target="_blank">Upload structures from CoD</a>
    </ul></td>
    </tr></table>
"""
    
    html = template.format(appbase=appbase, jupbase=jupbase)
    return ipw.HTML(html)
    
#EOF
