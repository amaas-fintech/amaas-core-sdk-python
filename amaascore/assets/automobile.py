from datetime import date
from dateutil.parser import parse

from amaascore.assets.real_asset import RealAsset
from amaascore.assets.enums import *

class Automobile(RealAsset):

    @staticmethod
    def mandatory_attributes():
        return set()

    @staticmethod
    def additional_attributes():
        return set()

    def __init__(self, asset_manager_id, asset_id, client_id, asset_issuer_id=None,
                 country_id=None, display_name='', description='',
                 venue_id=None, issue_date=None, maturity_date=date.max, comments=None,
                 links=None, references=None, additional=None, currency=None,
                 asset_status='Active', manufacture_year=None,
                 value_date=None, value=None, account_id=None,
                 vehicle_id=None, make=None, model=None, color=None,
                 style=None, genre=None, rarity=None,
                 condition=None, imported=None, imported_country_id=None,
                 engine_id=None, chassis_id=None, steering=None, gearbox=None, gears=None,
                 drive=None, engine_cap=None, power=None, weight=None,
                 speed=None, fuel_type=None, petrol_grade=None, *args, **kwargs):
        super(Automobile, self).__init__(asset_manager_id=asset_manager_id,
                                         asset_id=asset_id, client_id=client_id,
                                         asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                         display_name=display_name,
                                         description=description, country_id=country_id,
                                         venue_id=venue_id, issue_date=issue_date,
                                         currency=currency, maturity_date=maturity_date,
                                         comments=comments, links=links, references=references,
                                         additional=additional,
                                         *args, **kwargs)
        self.manufacure_year = manufacture_year
        self.value_date = value_date
        self.value = value
        self.account_id = account_id
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.color = color
        self.style = style
        self.genre = genre
        self.rarity = rarity
        self.condition = condition
        self.imported = imported
        self.imported_country_id = imported_country_id
        self.engine_id = engine_id
        self.chassis_id = chassis_id
        self.steering = steering
        self.gearbox = gearbox
        self.gears = gears
        self.drive = drive
        self.engine_cap = engine_cap
        self.power = power
        self.weight = weight
        self.speed = speed
        self.fuel_type = fuel_type
        self.petrol_grade = petrol_grade

    @property
    def manufacture_year(self):
        return self._manufacture_year

    @manufacture_year.setter
    def manufacture_year(self, manufacture_year):
        if isinstance(manufacture_year, str):
            manufacture_year = int(manufacture_year)
        self._manufacture_year = manufacture_year

    @property
    def value_date(self):
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        if isinstance(value_date, str):
            value_date = parse(value_date).date()
        self._value_date = value_date

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        self._vehicle_id = vehicle_id

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        if not make:
            self._make = None
        elif make in CAR_MAKE_RECORD:
            self._make = make
        else:
            raise ValueError("Invalid input for car make: %s" % make)
    
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        """too many car models, accept any inputs for now"""
        self._model = model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not color:
            self._color = None
        elif color in CAR_COLOR_RECORD:
            self._color = color
        else:
            raise ValueError("Invalid input for car color: %s" % color)

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style):
        if not style:
            self._style = None
        elif style in set(CAR_STYLE.keys()):
            self._style = style
        elif style in set(CAR_STYLE.values()):
            self._style = list(CAR_STYLE.keys())[list(CAR_STYLE.values()).index(style)]
        else:
            raise ValueError("Invalid input for car style: %s" % style)

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if not genre:
            self._genre = None
        elif genre in set(CAR_GENRE.keys()):
            self._genre = genre
        elif genre in set(CAR_GENRE.values()):
            self._genre = list(CAR_GENRE.keys())[list(CAR_GENRE.values()).index(genre)]
        else:
            raise ValueError("Invalid input for car genre: %s" % genre)

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, rarity):
        if not rarity:
            self._rarity = None
        elif rarity in CAR_RARITY:
            self._rarity = rarity
        else:
            raise ValueError("Invalid input for car rarity: %s" % rarity)

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, condition):
        if not condition:
            self._condition = None
        elif condition in set(CAR_CONDITION.keys()):
            self._condition = condition
        elif condition in set(CAR_CONDITION.values()):
            self._condition = list(CAR_CONDITION.keys())[list(CAR_CONDITION.values()).index(condition)]
        else:
            raise ValueError("Invalid input for car condition: %s" % condition)

    @property
    def imported(self):
        return self._imported

    @imported.setter
    def imported(self, imported):
        if not imported:
            self._imported = None
        else:
            if imported not in [True, False]:
                raise ValueError("imported should be True or False: %s" % imported)
            self._imported = imported

    @property
    def imported_country_id(self):
        return self._imported_country_id

    @imported_country_id.setter
    def imported_country_id(self, imported_country_id):
        self._imported_country_id = imported_country_id

    @property
    def engine_id(self):
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        self._engine_id = engine_id

    @property
    def chassis_id(self):
        return self._chassis_id

    @chassis_id.setter
    def chassis_id(self, chassis_id):
        self._chassis_id = chassis_id

    @property
    def steering(self):
        return self._steering

    @steering.setter
    def steering(self, steering):
        if not steering:
            self._steering = None
        else:
            if steering not in ['LHD', 'RHD']:
                raise ValueError("Invalid steering LHD/RHD: %s" % steering)
            self._steering = steering

    @property
    def gearbox(self):
        return self._gearbox

    @gearbox.setter
    def gearbox(self, gearbox):
        if not gearbox:
            self._gearbox = None
        else:
            if gearbox not in ['A', 'M']:
                raise ValueError("Invalid gearbox A/M: %s" % gearbox)
            self._gearbox = gearbox

    @property
    def gears(self):
        return self._gears

    @gears.setter
    def gears(self, gears):
        self._gears = gears

    @property
    def drive(self):
        return self._drive

    @drive.setter
    def drive(self, drive):
        if not drive:
            self._drive = None
        else:
            if drive not in ['RWD', 'FWD', 'AWD']:
                raise ValueError("Invalid drive RWD/FWD/AWD: %s" % drive)
            self._drive = drive

    @property
    def engine_cap(self):
        return self._engine_cap

    @engine_cap.setter
    def engine_cap(self, engine_cap):
        self._engine_cap = engine_cap

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        self._power = power

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        if not fuel_type:
            self._fuel_type = None
        else:
            if fuel_type not in ['Petrol', 'Diesel']:
                raise ValueError("Invalid fuel_type Petrol/Diesel: %s" % fuel_type)
            self._fuel_type = fuel_type

    @property
    def petrol_grade(self):
        return self._petrol_grade

    @petrol_grade.setter
    def petrol_grade(self, petrol_grade):
        if not petrol_grade:
            self._petrol_grade = None
        else:
            if isinstance(petrol_grade, str):
                petrol_grade = int(float(petrol_grade))
            if petrol_grade in set(CAR_PETROL_GRADE.keys()):
                self._petrol_grade = CAR_PETROL_GRADE[petrol_grade]
            else:
                raise ValueError("Invalid data type for petrol_grade (87~94): %s" % petrol_grade)
