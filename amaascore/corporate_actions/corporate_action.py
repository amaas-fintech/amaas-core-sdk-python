import datetime
from dateutil.parser import parse
import uuid

from amaascore.core.amaas_model import AMaaSModel
from amaascore.core.reference import Reference


class CorporateAction(AMaaSModel):

    @staticmethod
    def children():
        return {'references': Reference}

    def __init__(self, asset_manager_id, corporate_action_id, record_date, corporate_action_status='Open',
                 asset_id=None, party_id=None, declared_date=None, settlement_date=None, elective=False, message=None,
                 description='', references=None, *args, **kwargs):
        self.asset_manager_id = asset_manager_id
        self.corporate_action_id = corporate_action_id or uuid.uuid4().hex
        self.corporate_action_type = self.__class__.__name__
        self.corporate_action_status = corporate_action_status
        self.record_date = record_date
        self.declared_date = declared_date or datetime.date.today()
        self.settlement_date = settlement_date or self.record_date
        self.asset_id = asset_id
        self.party_id = party_id
        self.elective = elective
        self.message = message
        self.description = description
        self.references = references or {}
        self.references['AMaaS'] = Reference(reference_value=self.corporate_action_id)  # Upserts the AMaaS Reference

        super(CorporateAction, self).__init__(*args, **kwargs)

    @property
    def record_date(self):
        if hasattr(self, '_record_date'):
            return self._record_date

    @record_date.setter
    def record_date(self, value):
        """
        The date on which the corporate action takes effect
        :param value:
        :return:
        """
        if value:
            self._record_date = parse(value).date() if isinstance(value, (str, unicode)) else value

    @property
    def declared_date(self):
        if hasattr(self, '_record_date'):
            return self._record_date

    @declared_date.setter
    def declared_date(self, value):
        """
        The date on which the corporate action was declared
        :param value:
        :return:
        """
        if value:
            self._declared_date = parse(value).date() if isinstance(value, (str, unicode)) else value

    @property
    def settlement_date(self):
        if hasattr(self, '_settlement_date'):
            return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, value):
        """
        The date on which the corporate action is settled
        :param value:
        :return:
        """
        if value:
            self._settlement_date = parse(value).date() if isinstance(value, (str, unicode)) else value