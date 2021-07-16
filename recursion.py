import json

def html_dict_search(html_dict, selector):
    f=open(html_dict,"r")
    html_dict=json.loads(f.read())
    for i in html_dict[selector]:
        print(i)
    f.close()
    """
    Implement `id` and `class` selectors
    """
    pass
html_dict="D:\Aasma\FreeCodeChamp\python_drills\html_dict.json"
selector="Employees"
html_dict_search(html_dict, selector)
