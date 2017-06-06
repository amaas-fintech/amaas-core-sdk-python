from amaascore.parties.children import Address, Email, Link, Reference, Comment

DIRECT = {'addresses': 'Address', 'emails': 'Email', 'references': 'Reference', 'comments': 'Comment'}

def party_formatted_string_to_links(links_input):
    """
    Example formatted string ::
    '{link_1:[{linked_party_id:12345},{linked_party_id:54321,active:true}],link_2:[{linked_party_id:12365}]}'
    string of "true" will be converted to True, "false" will be converted to False
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
            elif (field.split(':')[1] == 'false' or field.split(':')[1]=='False'):
                params_dict[field.split(':')[0]] = False
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
                elif (field.split(':')[1] == 'false' or field.split(':')[1]=='False'):
                    params_dict[field.split(':')[0]] = False
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

def generic_formatted_string(references_input, _key):
    """
    Example formatted string ::
    '{{reference_value:1,active:true},{reference_value:2}}'
    string of "true" will be converted to True
    """
    clazz = globals()[DIRECT[_key]]
    reference_dict = dict()
    while (references_input != '}' and references_input != '' and references_input is not None):
        params_dict = dict()
        temp = references_input.split('}', 1)[0]
        while (temp[0] in [',', '{']):
            temp = temp[1:]
        key = temp.split(':', 1)[0]
        temp = temp.split(':', 1)[1]
        while (temp[0] in [',', '{']):
            temp = temp[1:]
        temp_list = temp.split(',')
        for field in temp_list:
            while (field[0] in [',', '{']):
                field = field[1:]
            if (field.split(':')[1] == 'true' or field.split(':')[1]=='True'):
                params_dict[field.split(':')[0]] = True
            elif (field.split(':')[1] == 'false' or field.split(':')[1]=='False'):
                params_dict[field.split(':')[0]] = False
            else:
                params_dict[field.split(':')[0]] = field.split(':')[1]
        reference_dict[key] = clazz(**params_dict)
        if len(references_input.split('}', 1))==2:
            references_input = references_input.split('}', 1)[1]
        else:
            references_input = ''
    return reference_dict

def process_normal(_dict):
    """
    Example formatted string :: (order: addresses, comments, emails, links, references)
    '{address_1:{line_one:12345,city:Singapore,country_id:SGD,address_primary:123,line_two:6789,active:true}}',
    '{comment_1:{comment_value:1,active:true},comment_2:{comment_value:2,active:false}}',
    '{email_1:{email:1@1.com,email_primary:true,active:true},email_2:{email:2@2.com,email_primary:false}}',
    '{link_1:[{linked_party_id:12345},{linked_party_id:54321,active:true}],link_2:[{linked_party_id:12365}]}',
    '{reference_1:{reference_value:1,active:true},reference_2:{reference_value:2}}'
    string of "true" will be converted to True, "false" will be converted to False
    """
    new_dict = dict()
    for _key, _value in _dict.items():
        if _key in DIRECT.keys():
            if _value != '' and _value != '{}' and _value is not None:
                new_dict[_key] = generic_formatted_string(_value, _key)
        elif _key == 'links':
            if _value != '' and _value != '{}' and _value is not None:
                new_dict[_key] = party_formatted_string_to_links(_value)
        else:
            new_dict[_key] = _value
    return new_dict
