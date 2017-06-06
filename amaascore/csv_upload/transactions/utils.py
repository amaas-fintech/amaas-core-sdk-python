from amaascore.transactions.children import Charge, Code, Comment, Link, Party, Reference

DIRECT = {'charges': 'Charge', 'codes': 'Code', 'comments': 'Comment', 'Parties': 'Party', 'references': 'Reference'}

def transaction_formatted_string_to_links(links_input):
    """
    Example formatted string ::
    '{link_1:[{linked_transaction_id:12345},{linked_transaction_id:54321,active:true}],link_2:[{linked_transaction_id:12365}]}'
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
        try:
            params_dict = dict()
            temp = references_input.split('}', 1)[0]
            while (temp[0] in [',', '{']):
                temp = temp[1:]
            key = temp.split(':', 1)[0]
            temp = temp.split(':', 1)[1]
            print(temp)
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
        except IndexError:
            break
    return reference_dict

def process_normal(_dict):
    """
    Example formatted string :: (order: charges, codes, comments, links, parties, references)
    '{charge_1:{charge_value:10,currency:SGD,active:true},charge_2:{charge_value:1,currency:SGD}}'
    '{code_1:{code_value:1,active:true},code_2:{code_value:2}}'
    '{comment_1:{comment_value:1,active:true},comment_2:{comment_value:2}}'
    '{link_1:[{linked_transaction_id:12345},{linked_transaction_id:54321,active:true}],link_2:[{linked_transaction_id:12365}]}'
    '{party_1:{party_id:1,active:true},party_2:{party_id:2,active:false}}'
    '{{reference_value:1,active:true},{reference_value:2}}'
    string of "true"/"True" will be converted to True, "false"/"True" will be converted to False
    """
    new_dict = dict()
    for _key, _value in _dict.items():
        if _key in DIRECT.keys():
            if _value != '' and _value != '{}' and _value is not None:
                new_dict[_key] = generic_formatted_string(_value, _key)
        elif _key == 'links':
            if _value != '' and _value != '{}' and _value is not None:
                new_dict[_key] = transaction_formatted_string_to_links(_value)
        else:
            new_dict[_key] = _value
    return new_dict
