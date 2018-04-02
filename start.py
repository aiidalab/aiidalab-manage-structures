import ipywidgets as ipw

def get_start_widget(appbase, jupbase):
    #http://fontawesome.io/icons/
    template = """
    <table>
    <tr>
        <th style="text-align:center"></th>
        <th style="width:70px" rowspan=2></th>
        <th style="text-align:center"></th>
        <th style="width:70px" rowspan=2></th>
        <th style="text-align:center"></th>
    <tr>
    <td valign="top"><ul>
    <li><a href="{appbase}/examples.ipynb" target="_blank">Look at the examples</a>
    </ul></td>
    <td valign="top"><ul>
    <li><a href="{appbase}/import_from_cod.ipynb" target="_blank">Upload from the CoD</a>
    </ul></td>
    <td valign="top"><ul>
    <li><a href="{appbase}/upload_structure.ipynb" target="_blank">Upload from computer</a>
    </ul></td>
    </tr></table>
"""
    
    html = template.format(appbase=appbase, jupbase=jupbase)
    return ipw.HTML(html)
    
#EOF
