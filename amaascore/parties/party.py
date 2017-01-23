from amaascore.core.amaas_model import AMaaSModel


class Party(AMaaSModel):

    def __init__(self, asset_manager_id, party_id, party_class, references={}, *args, **kwargs):
        self.asset_manager_id = asset_manager_id
        self.party_id = party_id
        self.party_class = party_class
        self.party_type = self.__class__.__name__
        self.references = references
        super(Party, self).__init__(*args, **kwargs)
