from decimal import Decimal


class OptionMixin(object):

    @property
    def put_call(self):
        if hasattr(self, '_put_call'):
            return self._put_call

    @put_call.setter
    def put_call(self, put_call):
        if put_call:
            if put_call in ['Put', 'Call']:
                self._put_call = put_call
            else:
                raise ValueError("Invalid value for put_call: %s" % put_call)

    @property
    def option_type(self):
        if hasattr(self, '_option_type'):
            return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        if option_type:
            if option_type in ['American', 'Bermudan', 'European']:
                self._option_type= option_type
            else:
                raise ValueError("Invalid value for option_type: %s" % option_type)

    @property
    def strike(self):
        if hasattr(self, '_strike'):
            return self._strike

    @strike.setter
    def strike(self, strike):
        """ Force strike to be a Decimal. """
        if strike:
            self._strike = Decimal(strike)