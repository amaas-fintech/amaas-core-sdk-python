from amaascore.parties.party import Party


class Individual(Party):

    def __init__(self, asset_manager_id, party_id, references={}, *args, **kwargs):
        self.asset_manager_id = asset_manager_id
        self.party_id = party_id
        self.party_class = 'Individual'
        self.references = references
        super(Organisation, self).__init__(asset_manager_id=asset_manager_id, party_id=party_id, references=references,
                                           *args, **kwargs)
