from amaascore.assets.future import Future


class BondFuture(Future):

    def __init__(self, asset_manager_id, asset_id, cheapest_to_deliver_id=None, asset_issuer_id=None,
                 asset_status='Active', issue_date=None, description='', country_id=None, venue_id=None, references={},
                 *args, **kwargs):
        """

        :param asset_manager_id:
        :param asset_id:
        :param cheapest_to_deliver_id: Populated from the server, cannot be calculated in the SDK.
        :param asset_issuer_id:
        :param asset_status:
        :param issue_date:
        :param description:
        :param country_id:
        :param venue_id:
        :param references:
        :param args:
        :param kwargs:
        """
        self.cheapest_to_deliver_id = cheapest_to_deliver_id
        super(BondFuture, self).__init__(asset_manager_id=asset_manager_id, asset_id=asset_id,
                                         asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                         description=description, country_id=country_id, venue_id=venue_id,
                                         references=references, issue_date=issue_date,
                                         *args, **kwargs)
