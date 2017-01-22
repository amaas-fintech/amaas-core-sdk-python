import uuid

from amaascore.core.amaas_model import AMaaSModel


class Book(AMaaSModel):
    """
    TODO - does this derive from anything?  Sort of depends on whether or not we are planning on storing it.
    """

    def __init__(self, asset_manager_id, book_id=None, positions=None):
        self.asset_manager_id = asset_manager_id
        self.book_id = book_id or uuid.uuid4().hex
        self.positions = positions

    def positions_by_asset(self):
        """
        A dictionary of Position objects keyed by asset_id.  If an asset position exists in more than one book, they
         are combined into a single position.
        :return:
        """
        return {position.asset_id: position for position in self.positions}
