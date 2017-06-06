from amaascore.core.amaas_model import AMaaSModel

class Reference(AMaaSModel):
    
    def __init__(self, reference_value, active=True, *args, **kwargs):
        self.reference_value = reference_value
        self.active = active
        super(Reference, self).__init__(*args, **kwargs)

def action_formatted_string_to_references(references_input):
    """
    Example formatted string ::
    '{{reference_value:1,active:true},{reference_value:2}}'
    string of "true" will be converted to True
    """
    reference_dict = dict()
    while (references_input != '}' and references_input != ''):
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
            if (field.split(':')[1] == 'true' or field.split(':')[1]=='True'):
                params_dict[field.split(':')[0]] = True
            else:
                params_dict[field.split(':')[0]] = field.split(':')[1]
        reference_dict[key] = Reference(params_dict)
        if len(references_input.split('}', 1))==2:
            references_input = references_input.split('}', 1)[1]
        else:
            references_input = ''
    return reference_dict

def process_normal(_dict):
    new_dict = dict()
    for key, value in _dict.items():
        if key == 'references':
            if value != '' and value != '{}' and value is not None:
                new_dict[key] = action_formatted_string_to_references(value)
        else:
            new_dict[key] = value
    return new_dict