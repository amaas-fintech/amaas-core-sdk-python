from amaascore.assets.children import Link, Reference

def asset_formatted_string_to_links(links_input):
    """
    Example formatted string ::
    '{link_1:[{linked_asset_id:12345},{linked_asset_id:54321,active:true}],link_2:[{linked_asset_id:12365}]}'
    string of "true" will be converted to True
    """
    links_dict = dict()
    key = ''
    if links_input!= '' and (links_input).split('{', 1)[1] != '':
        links_input = links_input.split('{', 1)[1]
        key=links_input.split(':',1)[0]
        links_input = links_input.split(':',1)[1]
    link_list = []
    value = links_input.split(']',1)[0][1:]
    if (len(links_input.split('}',1)) != 1):
        links_input = links_input.split(']',1)[1]
    while(key!=''):
        params_dict = dict()
        temp = value.split('}', 1)[0]
        value = value.split('}', 1)[1]
        while (temp[0] in [',', '{']):
            temp = temp[1:]
        temp_list = temp.split(',')
        for field in temp_list:
            if (field.split(':')[1] == 'true' or field.split(':')[1]=='True'):
                params_dict[field.split(':')[0]] = True
            else:
                params_dict[field.split(':')[0]] = field.split(':')[1]
        link_list.append(Link(params_dict))
        params_dict = dict()
        while(value!= '' and value[0:2] == ',{'):
            temp = value.split('}', 1)[0]
            value = value.split('}', 1)[1]
            while (temp[0] in [',', '{']):
                temp = temp[1:]
            temp_list = temp.split(',')
            for field in temp_list:
                if (field.split(':')[1] == 'true' or field.split(':')[1]=='True'):
                    params_dict[field.split(':')[0]] = True
                else:
                    params_dict[field.split(':')[0]] = field.split(':')[1]
            link_list.append(Link(params_dict))
            params_dict = dict()
        links_dict[key] = link_list
        if (links_input[0] == ','):
            links_input = links_input[1:]
        else:
            break
        link_list = []
        key = links_input.split(':', 1)[0]
        value = links_input.split(':', 1)[1].split(']', 1)[0][1:]
        links_input = links_input.split(':', 1)[1].split(']', 1)[1]        
    return links_dict

def asset_formatted_string_to_references(references_input):
    """
    Example formatted string ::
    '{{reference_value:1,active:true},{reference_value:2}}'
    string of "true" will be converted to True
    """
    reference_list = []
    while (references_input != '}' and references_input != ''):
        params_dict = dict()
        temp = references_input.split('}', 1)[0]
        while (temp[0] in [',', '{']):
            temp = temp[1:]
        if len(references_input.split('}', 1))==2:
            references_input = references_input.split('}', 1)[1]
        else:
            references_input = ''
        temp_list = temp.split(',')
        for field in temp_list:
            if (field.split(':')[1] == 'true' or field.split(':')[1]=='True'):
                params_dict[field.split(':')[0]] = True
            else:
                params_dict[field.split(':')[0]] = field.split(':')[1]
        reference_list.append(Reference(params_dict))
    return reference_list