from decimal import Decimal


class OptionMixin(object):
    """
    A mixin to add the relevant option attributes to assets.

    This class should not be instantiated on its own - it is a mixin for other assets.

    NED - I've seen mixins get out of control.  If we think this is happening, revisit the decision for this class.
    """

    def __init__(self, *args, **kwargs):
        self.put_call = kwargs.get('put_call')
        self.strike = kwargs.get('strike')
        super(OptionMixin, self).__init__()

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
    def strike(self):
        if hasattr(self, '_strike'):
            return self._strike

    @strike.setter
    def strike(self, strike):
        """ Force strike to be a Decimal. """
        if strike:
            self._strike = Decimal(strike)
