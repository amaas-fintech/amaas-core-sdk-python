#This file contains the essential function and methods to parse the csv file
#Some of the functions are helper functions
#Some of the processing function is for csv upload and download functions
#Information are contained in lists and dictionaries
#Check function usages by docstrings
#generic uploader depends heavily on amaasclass, must included in csv header and rows
#boolean strings will be converted to True or False
"""
example csv header and row values: (take note of children fields header format)
amaasclass,asset_id,links.link1.0.linked_asset_id,links.link1.0.active
Equity,12345,54321,true
"""
import csv

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaasutils.logging_utils import DEFAULT_LOGGING

from amaascore.assets.interface import AssetsInterface
from amaascore.parties.interface import PartiesInterface
from amaascore.books.interface import BooksInterface
from amaascore.corporate_actions.interface import CorporateActionsInterface
from amaascore.market_data.interface import MarketDataInterface
from amaascore.transactions.interface import TransactionsInterface
from amaascore.asset_managers.interface import AssetManagersInterface

from amaascore import parties
from amaascore import assets
from amaascore import transactions

from amaascore.assets.children import Link, Reference
from amaascore.parties.children import Address, Email, Link, Reference, Comment
from amaascore.transactions.children import Charge, Code, Comment, Link, Party, Reference


ASSET = ['Asset', 'Automobile', 'BondFutureOption', 'BondFuture', 'BondOption', 'Bond', 'ContractForDifference', 'Currency', 'CustomAsset', 
         'Derivative', 'EnergyFuture', 'EquityFuture', 'Equity', 'ExchangeTradedFund', 'ForeignExchange', 'Fund', 'FutureOption', 'Future'
         'ForeignExchangeOption', 'IndexFuture', 'Index', 'InterestRateFuture', 'ListedContractForDifference', 'ListedDerivative'
         'OptionMixin', 'RealAsset', 'RealEstate', 'Sukuk', 'SyntheticFromBook', 'SyntheticMultiLeg', 'Synthetic', 'Warrant', 'Wine']

PARTY = ['Broker', 'Company', 'Exchange', 'Fund', 'GovernmentAgency', 'Individual', 'Organisation', 'Party', 'SubFund']

BOOK = ['Book']

CORPORATE_ACTION = ['CorporateAction', 'Dividend', 'Notification', 'Split']

MARKET_DATA = ['EODPrice', 'FXRate', 'Quote']

TRANSACTION = ['Transaction']

ASSET_MANAGER = ['AssetManager', 'Relationship']

CHILDREN_CLASS = {'asset': {'links': assets.children.Link, 'references': assets.children.Reference},
                  'party': {'addresses': parties.children.Address, 'emails': parties.children.Email,
                             'links': parties.children.Link, 'references': parties.children.Reference,
                             'comments': parties.children.Comment},
                  'transaction': {'charges': transactions.children.Charge, 'codes': transactions.children.Code,
                                   'comments': transactions.children.Comment, 'links': transactions.children.Link,
                                   'references': transactions.children.Reference, 'parties': transactions.children.Party},
                  'asset_manager': {},
                  'book': {},
                  'corporate_action': {'references': assets.children.Reference}}

CHILDREN_SIGNAL = {'references', 'addresses', 'emails', 'comments', 'charges', 'codes', 'parties'}

def direct_to_class(amaasclass):
    """direct from amaasclass (first params given in the row) to the dictionary of the children class"""
    if amaasclass in ASSET:
        return CHILDREN_CLASS['asset']
    elif amaasclass in PARTY:
        return CHILDREN_CLASS['party']
    elif amaasclass in TRANSACTION:
        return CHILDREN_CLASS['transaction']
    elif amaasclass in BOOK:
        return CHILDREN_CLASS['book']
    elif amaasclass in CORPORATE_ACTION:
        return CHILDREN_CLASS['corporate_action']
    elif amaasclass in MARKET_DATA:
        return None #None for now
    else:
        return CHILDREN_CLASS['asset_manager']

def interface_direct_class(data_class):
    """help to direct to the correct interface interacting with DB by class name only"""
    if data_class in ASSET:
        interface = AssetsInterface()
    elif data_class in PARTY:
        interface = PartiesInterface()
    elif data_class in BOOK:
        interface = BooksInterface()
    elif data_class in CORPORATE_ACTION:
        interface = CorporateActionsInterface()
    elif data_class in MARKET_DATA:
        interface = MarketDataInterface()
    elif data_class in TRANSACTION:
        interface = TransactionsInterface()
    else:
        interface = AssetManagersInterface()
    return interface

def interface_direct_csvpath(csvpath):
    """help to direct to the correct interface interacting with DB by csvfile path"""
    with open(csvpath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_class = row.pop('amaasclass', '')
            return interface_direct_class(data_class)

def formatted_string_to_links(links_input, clazz):
    """
    Example formatted string ::
    '{link_1:[{linked_asset_id:12345},{linked_asset_id:54321,active:true}],link_2:[{linked_asset_id:12365}]}'
    string of "true" will be converted to True string of "false" will be converted to False (Python Boolean)
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
            params_dict[field.split(':')[0]] = process_value(field.split(':')[1])
        link_list.append(clazz(**params_dict))
        params_dict = dict()
        while(value!= '' and value[0:2] == ',{'):
            temp = value.split('}', 1)[0]
            value = value.split('}', 1)[1]
            while (temp[0] in [',', '{']):
                temp = temp[1:]
            temp_list = temp.split(',')
            for field in temp_list:
                params_dict[field.split(':')[0]] = process_value(field.split(':')[1])
            link_list.append(clazz(**params_dict))
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

def formatted_string_to_others(typi_input, clazz):
    """
    Example formatted string that is passed in from above::
    '{address_1:{line_one:12345,city:Singapore,country_id:SGD,address_primary:123,line_two:6789,active:true}}',
    '{comment_1:{comment_value:1,active:true},comment_2:{comment_value:2,active:false}}',
    '{email_1:{email:1@1.com,email_primary:true,active:true},email_2:{email:2@2.com,email_primary:false}}',
    '{reference_1:{reference_value:1,active:true},reference_2:{reference_value:2}}'
    '{charge_1:{charge_value:10,currency:SGD,active:true},charge_2:{charge_value:1,currency:SGD}}'
    '{code_1:{code_value:1,active:true},code_2:{code_value:2}}'
    '{comment_1:{comment_value:1,active:true},comment_2:{comment_value:2}}'
    '{party_1:{party_id:1,active:true},party_2:{party_id:2,active:false}}'
    string of "true" will be converted to True, string of "false" will be converted to False (Python Boolean)
    """
    typi_dict = dict()
    while (typi_input != '}' and typi_input != ''):
        params_dict = dict()
        temp = typi_input.split('}', 1)[0]
        while (temp[0] in [',', '{']):
            temp = temp[1:]
        key = temp.split(':', 1)[0]
        temp = temp.split(':', 1)[1]
        while (temp[0] in [',', '{']):
            temp = temp[1:]
        temp_list = temp.split(',')
        for field in temp_list:
            params_dict[field.split(':')[0]] = process_value(field.split(':')[1])
        typi_dict[key] = clazz(**params_dict)
        if len(typi_input.split('}', 1))==2:
            typi_input = typi_input.split('}', 1)[1]
        else:
            typi_input = ''
    return typi_dict

def process_header(header_str):
    """helper method"""
    if not children_signal(header_str):
        return header_str
    naive_split = header_str.split('.')
    return naive_split
    if naive_split[0] == 'links':
        res_list = [naive_split[0]]
        res_list.append(naive_split[1].split('[')[0])
        res_list.append(int(naive_split[1].split('[')[1][0:-1]))
        res_list.append(naive_split[2])
        return res_list
    else:
        return naive_split

def process_value(value_str):
    """
    process the value to check exotic value inputs
    true or false should be converted to python boolean values
    empty strings should be converted to None because it is undefined
    """
    #check for boolean
    if value_str == 'true' or value_str == 'True':
        return True
    elif value_str == 'false' or value_str == 'False':
        return False
    #check for None (undefined types)
    elif value_str == '':
        return None
    else:
        return value_str

def children_signal(header_str):
    """Check whether the string is signalling the field is a children feild"""
    if '.' in header_str:
        return True
    return False

def group_raw_to_formatted_string_dict(raw_dict):
    """this method can convert the children fields value by grouping them and convert to formatted string internally decided"""
    cooked_dict = dict()
    last_header_first = last_header_second = last_header_third = last_header_fourth = None
    for header, value in raw_dict.items():
        header = process_header(header)
        if isinstance(header, list):
            if len(header) == 4:
                if not cooked_dict.get('links', None):
                    cooked_dict['links']='{'
                cooking_value = cooked_dict['links']
                if header[1] in cooking_value:
                    cooking_str = cooking_value.split(header[1])[1].split(']', 1)[0]
                    if header[2] == last_header_third:
                        cooked_str = header[1]+cooking_str[0:-1]+','+header[3]+':'+value+'}]'
                    else:
                        addon_str = ',{'+header[3]+':'+value+'}'
                        cooked_str = header[1]+cooking_str+addon_str+']'
                    cooked_dict['links'] = cooking_value.split(header[1])[0]+cooked_str+cooking_value.split(header[1])[1].split(']', 1)[1]
                else:
                    addon_str = header[1]+':'+'[{'+header[3]+':'+value+'}]'
                    if cooking_value == '{':
                        cooked_dict['links'] = cooking_value+addon_str+'}'
                    else:
                        cooked_dict['links'] = cooking_value[0:-1]+addon_str+'}'
                last_header_first = header[0]
                last_header_second = header[1]
                last_header_third = header[2]
                last_header_fourth = header[3]
            else:
                if not cooked_dict.get(header[0], None):
                    cooked_dict[header[0]] = '{'
                cooking_value = cooked_dict[header[0]]
                if header[1] in cooking_value:
                    cooking_str = cooking_value.split(header[1])[1].split('}', 1)[0]
                    cooked_str = header[1]+cooking_str+','+header[2]+':'+value+'}'
                    cooked_dict[header[0]] = cooking_value.split(header[1])[0]+cooked_str+cooking_value.split(header[1])[1].split('}', 1)[1]
                else:
                    addon_str = header[1]+':{'+header[2]+':'+value+'}'
                    if len(addon_str) != 0:
                        addon_str = ','+addon_str
                    if cooking_value == '{':
                        cooked_dict[header[0]] = cooking_value+addon_str+'}'
                    else:
                        cooked_dict[header[0]] = cooking_value[0:-1]+addon_str+'}'
                last_header_first = header[0]
                last_header_second = header[1]
                last_header_third = header[2]
                last_header_fourth = None
        else:
            cooked_dict[header] = value
    return cooked_dict

def process_normal(_dict):
    """
    this method process the _dict to correct dict to be called by class constructor
    this method will be imported and called by main csv uploader function to help process the csv input stream
    """
    cooked_dict = group_raw_to_formatted_string_dict(_dict)
    data_class = cooked_dict.pop('amaasclass', '')
    children_class_dict = direct_to_class(data_class)
    tasty_dict = dict()
    for cooked_key, cooked_value in cooked_dict.items():
        if cooked_key in CHILDREN_SIGNAL:
            processed_dict = {cooked_key: formatted_string_to_others(cooked_value, children_class_dict[cooked_key])}
        elif cooked_key == 'links':
            processed_dict = {cooked_key: formatted_string_to_links(cooked_value, children_class_dict[cooked_key])}
        else:
            processed_dict = {cooked_key: process_value(cooked_value)}
        tasty_dict.update(processed_dict)
    return tasty_dict
