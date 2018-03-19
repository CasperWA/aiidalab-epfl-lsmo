import ipywidgets as ipw

def get_start_widget(appbase, jupbase):
    #http://fontawesome.io/icons/
    template = """
    <table>
    <tr>
        <th style="text-align:center">Calculations</th>
        <th style="width:70px" rowspan=2></th>
        <th style="text-align:center">Results analysis</th>        
        <th style="width:70px" rowspan=2></th>
        <th style="text-align:center">Import</th>        
    <tr>
    <td valign="top"><ul>
    <li><a href="{appbase}/calculations/isotherm.ipynb" target="_blank">Isotherm</a>
    </ul></td>
    
    <td valign="top"><ul>
    <li><a href="{appbase}/results/analysis.ipynb" target="_blank">Preprocess</a>
    <li><a href="{appbase}/results/show.ipynb" target="_blank">Show</a>
    <li><a href="{appbase}/results/show_interactive.ipynb" target="_blank">Show (interactive)</a>
    </ul></td>
    
     <td valign="top"><ul>
    <li><a href="{appbase}/import/import.ipynb" target="_blank">Import database</a>
    </ul></td>
    </tr></table>
"""
    
    html = template.format(appbase=appbase, jupbase=jupbase)
    return ipw.HTML(html)
    
#EOF