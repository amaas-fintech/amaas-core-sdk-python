Search.setIndex({docnames:["amaascore","amaascore.asset_managers","amaascore.assets","amaascore.books","amaascore.core","amaascore.corporate_actions","amaascore.market_data","amaascore.monitor","amaascore.parties","amaascore.tools","amaascore.transactions","index","modules"],envversion:51,filenames:["amaascore.rst","amaascore.asset_managers.rst","amaascore.assets.rst","amaascore.books.rst","amaascore.core.rst","amaascore.corporate_actions.rst","amaascore.market_data.rst","amaascore.monitor.rst","amaascore.parties.rst","amaascore.tools.rst","amaascore.transactions.rst","index.rst","modules.rst"],objects:{"":{amaascore:[0,0,0,"-"]},"amaascore.asset_managers":{"interface":[1,0,0,"-"],asset_manager:[1,0,0,"-"],enums:[1,0,0,"-"],utils:[1,0,0,"-"]},"amaascore.asset_managers.asset_manager":{AssetManager:[1,1,1,""]},"amaascore.asset_managers.interface":{AssetManagersInterface:[1,1,1,""]},"amaascore.asset_managers.interface.AssetManagersInterface":{"new":[1,2,1,""],deactivate:[1,2,1,""],retrieve:[1,2,1,""],search:[1,2,1,""]},"amaascore.asset_managers.utils":{json_to_asset_manager:[1,3,1,""]},"amaascore.assets":{"interface":[2,0,0,"-"],asset:[2,0,0,"-"],bond:[2,0,0,"-"],bond_future:[2,0,0,"-"],bond_future_option:[2,0,0,"-"],bond_option:[2,0,0,"-"],cfd:[2,0,0,"-"],currency:[2,0,0,"-"],derivative:[2,0,0,"-"],equity:[2,0,0,"-"],etf:[2,0,0,"-"],foreign_exchange:[2,0,0,"-"],fund:[2,0,0,"-"],future:[2,0,0,"-"],future_option:[2,0,0,"-"],fx_option:[2,0,0,"-"],index:[2,0,0,"-"],listed_cfd:[2,0,0,"-"],listed_derivative:[2,0,0,"-"],option_mixin:[2,0,0,"-"],real_asset:[2,0,0,"-"],real_estate:[2,0,0,"-"],utils:[2,0,0,"-"]},"amaascore.assets.asset":{Asset:[2,1,1,""]},"amaascore.assets.asset.Asset":{children:[2,4,1,""],issue_date:[2,5,1,""],maturity_date:[2,5,1,""],reference_types:[2,2,1,""]},"amaascore.assets.bond":{BondBase:[2,1,1,""],BondCorporate:[2,1,1,""],BondGovernment:[2,1,1,""],BondMortgage:[2,1,1,""]},"amaascore.assets.bond.BondBase":{coupon:[2,5,1,""],par:[2,5,1,""]},"amaascore.assets.bond_future":{BondFuture:[2,1,1,""]},"amaascore.assets.bond_future.BondFuture":{underlying_bond_coupon:[2,5,1,""]},"amaascore.assets.bond_future_option":{BondFutureOption:[2,1,1,""]},"amaascore.assets.bond_option":{BondOption:[2,1,1,""]},"amaascore.assets.cfd":{ContractForDifference:[2,1,1,""]},"amaascore.assets.currency":{Currency:[2,1,1,""]},"amaascore.assets.derivative":{Derivative:[2,1,1,""]},"amaascore.assets.equity":{Equity:[2,1,1,""]},"amaascore.assets.etf":{ExchangeTradedFund:[2,1,1,""]},"amaascore.assets.foreign_exchange":{ForeignExchange:[2,1,1,""],ForeignExchangeBase:[2,1,1,""],NonDeliverableForward:[2,1,1,""]},"amaascore.assets.foreign_exchange.ForeignExchangeBase":{base_currency:[2,2,1,""],counter_currency:[2,2,1,""]},"amaascore.assets.fund":{Fund:[2,1,1,""]},"amaascore.assets.fund.Fund":{creation_date:[2,5,1,""]},"amaascore.assets.future":{Future:[2,1,1,""]},"amaascore.assets.future_option":{FutureOption:[2,1,1,""]},"amaascore.assets.fx_option":{ForeignExchangeOption:[2,1,1,""]},"amaascore.assets.index":{Index:[2,1,1,""]},"amaascore.assets.interface":{AssetsInterface:[2,1,1,""]},"amaascore.assets.interface.AssetsInterface":{"new":[2,2,1,""],amend:[2,2,1,""],assets_by_asset_manager:[2,2,1,""],deactivate:[2,2,1,""],retrieve:[2,2,1,""],search:[2,2,1,""]},"amaascore.assets.listed_cfd":{ListedContractForDifference:[2,1,1,""]},"amaascore.assets.listed_derivative":{ListedDerivative:[2,1,1,""]},"amaascore.assets.option_mixin":{OptionMixin:[2,1,1,""]},"amaascore.assets.option_mixin.OptionMixin":{option_style:[2,5,1,""],option_type:[2,5,1,""],strike:[2,5,1,""]},"amaascore.assets.real_asset":{RealAsset:[2,1,1,""]},"amaascore.assets.real_estate":{RealEstate:[2,1,1,""]},"amaascore.assets.utils":{assets_to_csv:[2,3,1,""],assets_to_csv_stream:[2,3,1,""],csv_filename_to_assets:[2,3,1,""],csv_stream_to_assets:[2,3,1,""],json_to_asset:[2,3,1,""]},"amaascore.books":{"interface":[3,0,0,"-"],book:[3,0,0,"-"],enums:[3,0,0,"-"],portfolio:[3,0,0,"-"],utils:[3,0,0,"-"]},"amaascore.books.book":{Book:[3,1,1,""]},"amaascore.books.book.Book":{book_type:[3,5,1,""],non_interface_attributes:[3,4,1,""],positions_by_asset:[3,2,1,""]},"amaascore.books.interface":{BooksInterface:[3,1,1,""]},"amaascore.books.interface.BooksInterface":{"new":[3,2,1,""],amend:[3,2,1,""],books_by_asset_manager:[3,2,1,""],retire:[3,2,1,""],retrieve:[3,2,1,""],search:[3,2,1,""]},"amaascore.books.portfolio":{Portfolio:[3,1,1,""]},"amaascore.books.portfolio.Portfolio":{positions_by_asset:[3,2,1,""],positions_by_book:[3,2,1,""]},"amaascore.books.utils":{json_to_book:[3,3,1,""]},"amaascore.core":{"interface":[4,0,0,"-"],amaas_model:[4,0,0,"-"],reference:[4,0,0,"-"],tenor:[4,0,0,"-"]},"amaascore.core.amaas_model":{AMaaSModel:[4,1,1,""],json_handler:[4,3,1,""],to_json:[4,3,1,""],to_json_string:[4,3,1,""]},"amaascore.core.amaas_model.AMaaSModel":{amaas_model_attributes:[4,4,1,""],non_interface_attributes:[4,4,1,""],to_interface:[4,2,1,""],to_json:[4,2,1,""]},"amaascore.core.interface":{Interface:[4,1,1,""]},"amaascore.core.interface.Interface":{generate_config_filename:[4,4,1,""],read_token:[4,2,1,""]},"amaascore.core.reference":{Reference:[4,1,1,""]},"amaascore.core.tenor":{Tenor:[4,1,1,""]},"amaascore.core.tenor.Tenor":{check_tenor:[4,6,1,""],tenor_to_relativedelta:[4,6,1,""],to_relativedelta:[4,2,1,""],valid_tenors:[4,4,1,""]},"amaascore.corporate_actions":{"interface":[5,0,0,"-"],corporate_action:[5,0,0,"-"],dividend:[5,0,0,"-"],notification:[5,0,0,"-"],split:[5,0,0,"-"],utils:[5,0,0,"-"]},"amaascore.corporate_actions.corporate_action":{CorporateAction:[5,1,1,""]},"amaascore.corporate_actions.corporate_action.CorporateAction":{children:[5,4,1,""],declared_date:[5,5,1,""],record_date:[5,5,1,""],settlement_date:[5,5,1,""]},"amaascore.corporate_actions.dividend":{Dividend:[5,1,1,""]},"amaascore.corporate_actions.dividend.Dividend":{dividend_rate:[5,5,1,""]},"amaascore.corporate_actions.interface":{CorporateActionsInterface:[5,1,1,""]},"amaascore.corporate_actions.interface.CorporateActionsInterface":{"new":[5,2,1,""],amend:[5,2,1,""],cancel:[5,2,1,""],corporate_actions_by_asset_manager:[5,2,1,""],retrieve:[5,2,1,""],search:[5,2,1,""]},"amaascore.corporate_actions.notification":{Notification:[5,1,1,""]},"amaascore.corporate_actions.split":{Split:[5,1,1,""]},"amaascore.corporate_actions.split.Split":{ratio:[5,5,1,""]},"amaascore.corporate_actions.utils":{corporate_actions_to_csv:[5,3,1,""],corporate_actions_to_csv_stream:[5,3,1,""],csv_filename_to_corporate_actions:[5,3,1,""],csv_stream_to_corporate_actions:[5,3,1,""],json_to_corporate_action:[5,3,1,""]},"amaascore.exceptions":{AMaaSException:[0,7,1,""],TransactionNeedsSaving:[0,7,1,""]},"amaascore.market_data":{"interface":[6,0,0,"-"],eod_price:[6,0,0,"-"],fx_rate:[6,0,0,"-"],quote:[6,0,0,"-"],utils:[6,0,0,"-"]},"amaascore.market_data.eod_price":{EODPrice:[6,1,1,""]},"amaascore.market_data.eod_price.EODPrice":{business_date:[6,5,1,""],price:[6,5,1,""]},"amaascore.market_data.fx_rate":{FXRate:[6,1,1,""]},"amaascore.market_data.fx_rate.FXRate":{business_date:[6,5,1,""],rate:[6,5,1,""],rate_timestamp:[6,5,1,""]},"amaascore.market_data.interface":{MarketDataInterface:[6,1,1,""]},"amaascore.market_data.interface.MarketDataInterface":{persist_eod_prices:[6,2,1,""],persist_fx_rates:[6,2,1,""],retrieve_eod_prices:[6,2,1,""],retrieve_fx_rates:[6,2,1,""]},"amaascore.market_data.quote":{Quote:[6,1,1,""]},"amaascore.market_data.quote.Quote":{ask:[6,5,1,""],bid:[6,5,1,""],mid:[6,2,1,""],quote_datetime:[6,5,1,""]},"amaascore.market_data.utils":{json_to_eod_price:[6,3,1,""],json_to_fx_rate:[6,3,1,""]},"amaascore.monitor":{"interface":[7,0,0,"-"],item:[7,0,0,"-"],utils:[7,0,0,"-"]},"amaascore.monitor.interface":{MonitorInterface:[7,1,1,""]},"amaascore.monitor.interface.MonitorInterface":{close_item:[7,2,1,""],items_by_asset_manager:[7,2,1,""],new_item:[7,2,1,""],resubmit_item:[7,2,1,""],retrieve_item:[7,2,1,""],search_items:[7,2,1,""]},"amaascore.monitor.item":{Item:[7,1,1,""]},"amaascore.monitor.utils":{json_to_item:[7,3,1,""]},"amaascore.parties":{"interface":[8,0,0,"-"],broker:[8,0,0,"-"],children:[8,0,0,"-"],company:[8,0,0,"-"],enums:[8,0,0,"-"],exchange:[8,0,0,"-"],fund:[8,0,0,"-"],government_agency:[8,0,0,"-"],individual:[8,0,0,"-"],organisation:[8,0,0,"-"],party:[8,0,0,"-"],utils:[8,0,0,"-"]},"amaascore.parties.broker":{Broker:[8,1,1,""]},"amaascore.parties.children":{Address:[8,1,1,""],Email:[8,1,1,""]},"amaascore.parties.company":{Company:[8,1,1,""]},"amaascore.parties.exchange":{Exchange:[8,1,1,""]},"amaascore.parties.fund":{Fund:[8,1,1,""]},"amaascore.parties.government_agency":{GovernmentAgency:[8,1,1,""]},"amaascore.parties.individual":{Individual:[8,1,1,""]},"amaascore.parties.individual.Individual":{date_of_birth:[8,5,1,""],description:[8,5,1,""]},"amaascore.parties.interface":{PartiesInterface:[8,1,1,""]},"amaascore.parties.interface.PartiesInterface":{"new":[8,2,1,""],amend:[8,2,1,""],deactivate:[8,2,1,""],parties_by_asset_manager:[8,2,1,""],retrieve:[8,2,1,""],search:[8,2,1,""]},"amaascore.parties.organisation":{Organisation:[8,1,1,""]},"amaascore.parties.party":{Party:[8,1,1,""]},"amaascore.parties.party.Party":{addresses:[8,5,1,""],children:[8,4,1,""],emails:[8,5,1,""],party_status:[8,5,1,""],upsert_address:[8,2,1,""],upsert_email:[8,2,1,""]},"amaascore.parties.utils":{csv_filename_to_parties:[8,3,1,""],csv_stream_to_parties:[8,3,1,""],json_to_party:[8,3,1,""],parties_to_csv:[8,3,1,""],parties_to_csv_stream:[8,3,1,""]},"amaascore.tools":{generate_asset:[9,0,0,"-"],generate_asset_manager:[9,0,0,"-"],generate_book:[9,0,0,"-"],generate_corporate_action:[9,0,0,"-"],generate_market_data:[9,0,0,"-"],generate_monitor_item:[9,0,0,"-"],generate_party:[9,0,0,"-"],generate_transaction:[9,0,0,"-"]},"amaascore.tools.generate_asset":{generate_asset:[9,3,1,""],generate_bond:[9,3,1,""],generate_bond_option:[9,3,1,""],generate_common:[9,3,1,""],generate_foreignexchange:[9,3,1,""]},"amaascore.tools.generate_asset_manager":{generate_asset_manager:[9,3,1,""]},"amaascore.tools.generate_book":{generate_book:[9,3,1,""]},"amaascore.tools.generate_corporate_action":{generate_common:[9,3,1,""],generate_corporate_action:[9,3,1,""],generate_dividend:[9,3,1,""],generate_split:[9,3,1,""]},"amaascore.tools.generate_market_data":{generate_eod_price:[9,3,1,""],generate_fx_rate:[9,3,1,""],generate_quote:[9,3,1,""]},"amaascore.tools.generate_monitor_item":{generate_item:[9,3,1,""]},"amaascore.tools.generate_party":{generate_address:[9,3,1,""],generate_broker:[9,3,1,""],generate_common:[9,3,1,""],generate_email:[9,3,1,""],generate_individual:[9,3,1,""],generate_party:[9,3,1,""]},"amaascore.tools.generate_transaction":{generate_common:[9,3,1,""],generate_position:[9,3,1,""],generate_transaction:[9,3,1,""]},"amaascore.transactions":{"interface":[10,0,0,"-"],children:[10,0,0,"-"],enums:[10,0,0,"-"],position:[10,0,0,"-"],transaction:[10,0,0,"-"],utils:[10,0,0,"-"]},"amaascore.transactions.children":{Charge:[10,1,1,""],Code:[10,1,1,""],Comment:[10,1,1,""],Link:[10,1,1,""],Party:[10,1,1,""]},"amaascore.transactions.children.Charge":{charge_value:[10,5,1,""]},"amaascore.transactions.interface":{TransactionsInterface:[10,1,1,""]},"amaascore.transactions.interface.TransactionsInterface":{"new":[10,2,1,""],allocate_transaction:[10,2,1,""],amend:[10,2,1,""],cancel:[10,2,1,""],net_transactions:[10,2,1,""],position_search:[10,2,1,""],positions_by_asset_manager:[10,2,1,""],positions_by_asset_manager_book:[10,2,1,""],retrieve:[10,2,1,""],retrieve_netting_set:[10,2,1,""],retrieve_transaction_allocations:[10,2,1,""],search:[10,2,1,""],transactions_by_asset_manager:[10,2,1,""],upsert_transaction_asset:[10,2,1,""],upsert_transaction_book:[10,2,1,""]},"amaascore.transactions.position":{Position:[10,1,1,""]},"amaascore.transactions.position.Position":{quantity:[10,5,1,""]},"amaascore.transactions.transaction":{Transaction:[10,1,1,""]},"amaascore.transactions.transaction.Transaction":{add_link:[10,2,1,""],charge_types:[10,2,1,""],charges_net_effect:[10,2,1,""],children:[10,4,1,""],code_types:[10,2,1,""],execution_time:[10,5,1,""],gross_settlement:[10,5,1,""],net_settlement:[10,5,1,""],postings:[10,5,1,""],price:[10,5,1,""],quantity:[10,5,1,""],reference_types:[10,2,1,""],remove_link:[10,2,1,""],settlement_date:[10,5,1,""],transaction_action:[10,5,1,""],transaction_date:[10,5,1,""],transaction_status:[10,5,1,""],transaction_type:[10,5,1,""],upsert_code:[10,2,1,""],upsert_link_set:[10,2,1,""]},"amaascore.transactions.utils":{csv_filename_to_transactions:[10,3,1,""],csv_stream_to_transactions:[10,3,1,""],json_to_position:[10,3,1,""],json_to_transaction:[10,3,1,""],transactions_to_csv:[10,3,1,""],transactions_to_csv_stream:[10,3,1,""]},amaascore:{asset_managers:[1,0,0,"-"],assets:[2,0,0,"-"],books:[3,0,0,"-"],config:[0,0,0,"-"],core:[4,0,0,"-"],corporate_actions:[5,0,0,"-"],error_messages:[0,0,0,"-"],exceptions:[0,0,0,"-"],market_data:[6,0,0,"-"],monitor:[7,0,0,"-"],parties:[8,0,0,"-"],tools:[9,0,0,"-"],transactions:[10,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","function","Python function"],"4":["py","staticmethod","Python static method"],"5":["py","attribute","Python attribute"],"6":["py","classmethod","Python class method"],"7":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function","4":"py:staticmethod","5":"py:attribute","6":"py:classmethod","7":"py:exception"},terms:{"case":10,"class":[0,1,2,3,4,5,6,7,8,10],"default":2,"enum":[0,11,12],"function":[2,10],"new":[1,2,3,5,8,10],"return":[1,2,3,4,6,10],"static":[2,3,4,5,8,10],"true":[4,6,8,10],Not:6,The:[1,6,10],account_id:10,accounting_typ:10,activ:[1,2,3,4,6,8,9,10],add_link:10,address:8,address_primari:[8,9],address_typ:8,affect:10,all:[0,10],allocate_transact:10,allocation_dict:10,allocation_typ:10,also:1,altogeth:10,amaa:[0,4,10],amaas_model:[0,1,2,3,5,6,7,8,10,11,12],amaas_model_attribut:4,amaasexcept:0,amaasmodel:[1,2,3,4,5,6,7,8,10],amend:[2,3,5,8,10],ani:10,annot:4,anticip:4,anyth:[3,4],api:10,arg:[1,2,3,4,5,6,7,8,10],ask:[6,9],asset:[0,1,3,10,11,12],asset_book_id:[7,9,10],asset_id:[2,3,5,6,7,9,10],asset_issuer_id:2,asset_manag:[0,11,12],asset_manager_id:[1,2,3,5,6,7,8,9,10],asset_manager_statu:[1,9],asset_manager_typ:[1,9],asset_statu:2,assetmanag:1,assetmanagersinterfac:1,assets_by_asset_manag:2,assets_to_csv:2,assets_to_csv_stream:2,assetsinterfac:2,associ:10,attribut:[4,8,10],base:[0,1,2,3,4,5,6,7,8,10],base_curr:[2,3,8],bid:[6,9],bond:[0,11,12],bond_futur:[0,11,12],bond_future_opt:[0,11,12],bond_opt:[0,11,12],bondbas:2,bondcorpor:2,bondfutur:2,bondfutureopt:2,bondgovern:2,bondmortgag:2,bondopt:2,book:[0,10,11,12],book_id:[3,9,10],book_statu:3,book_typ:[3,9],books_by_asset_manag:3,booksinterfac:3,broker:[0,11,12],busi:6,business_d:[6,9],cach:10,call:10,can:10,cancel:[5,10],cast:10,certain:10,cfd:[0,11,12],chang:2,charg:10,charge_curr:9,charge_typ:10,charge_valu:10,charges_net_effect:10,cheapest_to_deliver_id:2,check_tenor:4,children:[0,2,5,11,12],circumst:10,citi:8,classmethod:4,client_id:[1,9,10],close_item:7,close_tim:3,code:10,code_typ:10,code_valu:10,collect:[8,10],combin:3,comment:10,comment_valu:10,compani:[0,11,12],config:[11,12],config_filenam:4,contain:10,content:[11,12],contractfordiffer:2,convert:4,core:[0,1,2,3,5,6,7,8,10,12],corporate_act:[0,11,12],corporate_action_id:[5,9],corporate_action_statu:5,corporate_actions_by_asset_manag:5,corporate_actions_to_csv:5,corporate_actions_to_csv_stream:5,corporateact:5,corporateactionsinterfac:5,could:6,counter:2,counter_curr:2,counterparty_book_id:[9,10],country_id:[2,8,9],coupon:2,creat:[1,10],creation_d:2,csv:[0,11,12],csv_filename_to_asset:2,csv_filename_to_corporate_act:5,csv_filename_to_parti:8,csv_filename_to_transact:10,csv_stream_to_asset:2,csv_stream_to_corporate_act:5,csv_stream_to_parti:8,csv_stream_to_transact:10,currenc:[0,10,11,12],current:[2,4,10],date:[2,6,9,10],date_of_birth:8,datetim:[1,2,3,9],deactiv:[1,2,8],decim:10,declared_d:5,default_book_close_tim:1,default_book_owner_id:1,default_timezon:1,deliver:2,depend:3,deriv:[0,3,6,11,12],descript:[2,3,5,8],dict:[8,10],dict_to_convert:4,dictionari:3,differ:2,dividend:[0,11,12],dividend_asset_id:5,dividend_r:5,doe:3,doesn:4,effect:10,elect:5,email:[8,9],email_primari:[8,9],email_typ:8,endpoint:4,energy_futur:[0,11,12],entri:10,eod:9,eod_pric:[0,11,12],eodpric:6,equiti:[0,11,12],equity_futur:[0,11,12],error_messag:[11,12],etf:[0,11,12],except:[11,12],exchang:[0,11,12],exchangetradedfund:2,execution_tim:10,exist:3,expiry_d:2,fals:[2,5,9],filenam:[2,5,8,10],foreign_exchang:[0,11,12],foreignexchang:2,foreignexchangebas:2,foreignexchangeopt:2,forward:2,from:[3,10],fund:[0,11,12],fungibl:[2,9],futur:[0,4,11,12],future_opt:[0,11,12],futureopt:2,fx_option:[0,11,12],fx_rate:[0,11,12],fxrate:6,generate_address:9,generate_asset:[0,11,12],generate_asset_manag:[0,11,12],generate_bond:9,generate_bond_opt:9,generate_book:[0,11,12],generate_brok:9,generate_common:9,generate_config_filenam:4,generate_corporate_act:[0,11,12],generate_dividend:9,generate_email:9,generate_eod_pric:9,generate_foreignexchang:9,generate_fx_r:9,generate_individu:9,generate_item:9,generate_market_data:[0,11,12],generate_monitor_item:[0,11,12],generate_parti:[0,11,12],generate_posit:9,generate_quot:9,generate_split:9,generate_transact:[0,11,12],given_nam:8,government_ag:[0,11,12],governmentag:8,gross_settl:10,helper:[2,10],here:10,howev:10,index:[0,11,12],index_futur:[0,11,12],individu:[0,11,12],inform:1,instanti:2,interest_rate_futur:[0,11,12],interfac:[0,11,12],issue_d:2,item:[0,10,11,12],item_class:[7,9],item_d:[7,9],item_id:[7,9],item_level:[7,9],item_sourc:[7,9],item_statu:7,item_typ:[7,9],items_by_asset_manag:7,itself:10,json:4,json_asset:2,json_asset_manag:1,json_book:3,json_corporate_act:5,json_eod_pric:6,json_fx_rat:6,json_handl:4,json_item:7,json_posit:10,json_to_asset:2,json_to_asset_manag:1,json_to_book:3,json_to_convert:8,json_to_corporate_act:5,json_to_eod_pric:6,json_to_fx_r:6,json_to_item:7,json_to_parti:8,json_to_posit:10,json_to_transact:10,json_transact:10,just:2,kei:3,kwarg:[1,2,3,4,5,6,7,8,10],line_on:8,line_two:8,link:[2,8,10],link_list:10,link_set:10,link_typ:10,linked_transaction_id:10,list:10,listed_cfd:[0,11,12],listed_deriv:[0,11,12],listedcontractfordiffer:2,listedderiv:2,logger:[1,2,3,5,6,7,8,10],manag:1,market_data:[0,11,12],marketdatainterfac:6,maturity_d:2,messag:[5,7,9],mid:6,might:2,minor_unit_plac:2,model:2,modul:[11,12],monitor:[0,11,12],monitorinterfac:7,more:3,multipl:10,need:[2,4,6],net:10,net_affect:10,net_affecting_charg:9,net_settl:10,net_transact:10,netting_typ:10,never:2,new_item:7,non:4,non_interface_attribut:[3,4],nondeliverableforward:2,none:[1,2,3,4,5,6,7,8,9,10],normal:10,note:10,notif:[0,11,12],object:[2,3,4,6,8,10],one:3,onli:[1,4,10],open:[5,7],option:2,option_mixin:[0,11,12],option_styl:[2,9],option_typ:[2,9],optionmixin:2,organis:[0,11,12],origin:1,other:[8,10],out:4,over:2,owner:10,owner_id:[3,9],packag:[11,12],page:11,pair:2,par:2,param:10,paramet:[1,6,10],parti:[0,10,11,12],parties_by_asset_manag:8,parties_to_csv:8,parties_to_csv_stream:8,partiesinterfac:8,party_id:[1,3,5,8,9,10],party_statu:[8,9],party_typ:10,pass:10,pay_frequ:2,persist_eod_pric:6,persist_fx_r:6,plan:3,pop:4,popul:10,portfolio:[0,11,12],posit:[0,3,11,12],position_d:10,position_search:10,positions_by_asset:3,positions_by_asset_manag:10,positions_by_asset_manager_book:10,positions_by_book:3,possibl:1,post:10,postal_cod:8,potenti:4,premium:2,price:[6,9,10],quantiti:[9,10],quot:[0,11,12],quote_datetim:6,rate:[6,9],rate_timestamp:[6,9],rate_typ:[6,9],ratio:5,read:1,read_token:4,real_asset:[0,11,12],real_est:[0,11,12],realasset:2,realest:2,realli:6,record_d:5,refer:[0,2,5,8,10,11,12],reference_typ:[2,10],reference_valu:[4,10],region:8,relationship:[0,11,12],remov:10,remove_link:10,requir:4,resubmit_item:7,result:10,retir:3,retriev:[1,2,3,5,8,10],retrieve_eod_pric:6,retrieve_fx_r:6,retrieve_item:7,retrieve_netting_set:10,retrieve_transaction_alloc:10,same:[2,10],scenario:10,search:[1,2,3,5,8,10,11],search_item:7,servic:[1,4],set:10,settlement_curr:[9,10],settlement_d:[5,10],should:[2,10],singl:[3,10],sort:3,sourc:[0,1,2,3,4,5,6,7,8,9,10],split:[0,11,12],spot:2,store:3,stream:[2,5,8,10],strike:[2,9],submodul:[11,12],subpackag:[11,12],surnam:8,synthet:[0,11,12],synthetic_from_book:[0,11,12],synthetic_multi_leg:[0,11,12],tenor:[0,11,12],tenor_to_relativedelta:4,test:10,than:3,thei:3,thi:[2,3,4,10],timedelta:[1,3],timezon:3,to_interfac:4,to_json:4,to_json_str:4,to_relativedelta:4,todo:[2,3,10],tool:[0,11,12],total:10,trade:[3,9,10],transact:[0,2,11,12],transaction_act:[9,10],transaction_asset_json:10,transaction_book_json:10,transaction_curr:[9,10],transaction_d:[9,10],transaction_date_end:10,transaction_date_start:10,transaction_id:[7,9,10],transaction_statu:[9,10],transaction_status:10,transaction_typ:[9,10],transactionneedssav:0,transactions_by_asset_manag:10,transactions_to_csv:10,transactions_to_csv_stream:10,transactionsinterfac:10,two:2,type:[8,10],underli:2,underlying_asset_id:2,underlying_bond_coupon:2,underlying_bond_tenor:2,update_existing_pric:6,update_existing_r:6,upsert_address:8,upsert_cod:10,upsert_email:8,upsert_link_set:10,upsert_transaction_asset:10,upsert_transaction_book:10,usd:3,use_auth:4,used:1,useful:[2,10],utc:[1,3],util:[0,11,12],valid_tenor:4,valu:4,venue_id:2,version:[4,8,10],via:10,what:[8,10],when:4,whether:3,which:[6,8,10],within:10,your:1,zero:10},titles:["amaascore package","amaascore.asset_managers package","amaascore.assets package","amaascore.books package","amaascore.core package","amaascore.corporate_actions package","amaascore.market_data package","amaascore.monitor package","amaascore.parties package","amaascore.tools package","amaascore.transactions package","Welcome to amaas-core-sdk-python&#8217;s documentation!","amaascore"],titleterms:{"enum":[1,3,8,10],amaa:11,amaas_model:4,amaascor:[0,1,2,3,4,5,6,7,8,9,10,11,12],asset:2,asset_manag:[1,8],bond:2,bond_futur:2,bond_future_opt:2,bond_opt:2,book:3,broker:8,cfd:2,children:[8,10],compani:8,config:0,content:[0,1,2,3,4,5,6,7,8,9,10],core:[4,11],corporate_act:5,csv:9,currenc:2,deriv:2,dividend:5,document:11,energy_futur:2,eod_pric:6,equiti:2,equity_futur:2,error_messag:0,etf:2,except:0,exchang:8,foreign_exchang:2,fund:[2,8],futur:2,future_opt:2,fx_option:2,fx_rate:6,generate_asset:9,generate_asset_manag:9,generate_book:9,generate_corporate_act:9,generate_market_data:9,generate_monitor_item:9,generate_parti:9,generate_transact:9,government_ag:8,index:2,index_futur:2,indic:11,individu:8,interest_rate_futur:2,interfac:[1,2,3,4,5,6,7,8,10],item:7,listed_cfd:2,listed_deriv:2,market_data:6,modul:[0,1,2,3,4,5,6,7,8,9,10],monitor:7,notif:5,option_mixin:2,organis:8,packag:[0,1,2,3,4,5,6,7,8,9,10],parti:8,portfolio:3,posit:10,python:11,quot:6,real_asset:2,real_est:2,refer:4,relationship:1,sdk:11,split:5,submodul:[0,1,2,3,4,5,6,7,8,9,10],subpackag:0,synthet:2,synthetic_from_book:2,synthetic_multi_leg:2,tabl:11,tenor:4,tool:9,transact:10,util:[1,2,3,5,6,7,8,10],welcom:11}})