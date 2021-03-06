from uuid import uuid1
from app.extensions import db
from datetime import datetime


class Userorder(db.Model):
    __tablename__ = 'userorder'
    orderid = db.Column(db.String(64), primary_key=True, default=str(uuid1()))
    addressid = db.Column(db.String(64), nullable=False)
    userid = db.Column(db.String(64), nullable=False)
    sumtotal = db.Column(db.DECIMAL(12, 2), nullable=False)
    createtime = db.Column(db.DateTime, default=str(datetime.now()))

    def db2json(self):
        data = to_json(self)
        return data


class Sorder(db.Model):
    __tablename__ = 'sorder'
    sorderid = db.Column(db.String(64), primary_key=True, default=str(uuid1()))
    orderid = db.Column(db.String(64), nullable=False)
    addressid = db.Column(db.String(64), nullable=False)
    sellerid = db.Column(db.String(64), nullable=False)
    userid = db.Column(db.String(64), nullable=False)
    goodsname = db.Column(db.String(64), nullable=False)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(32), nullable=False)
    sumunit = db.Column(db.DECIMAL(12, 2), nullable=False)
    state = db.Column(db.String(4), default='1')
    createtime = db.Column(db.DateTime, default=str(datetime.now()))

    def db2json(self):
        data = to_json(self)
        return data


class Exorder(db.Model):
    __tablename__ = 'exorder'
    sorderid = db.Column(db.String(64), primary_key=True, default=str(uuid1()))
    orderid = db.Column(db.String(64), nullable=False)
    sellerid = db.Column(db.String(64), nullable=False)
    userid = db.Column(db.String(64), nullable=False)
    exdesc = db.Column(db.String(64))
    exrepl = db.Column(db.Text(128))
    createtime = db.Column(db.DateTime, default=str(datetime.now()))
    repltime = db.Column(db.DateTime, default=str(datetime.now()))

    def db2json(self):
        data = to_json(self)
        return data


class Hisorder(db.Model):
    __tablename__ = 'hisorder'
    orderid = db.Column(db.String(64), primary_key=True, default=str(uuid1()))
    addressid = db.Column(db.String(64), nullable=False)
    userid = db.Column(db.String(64), nullable=False)
    sumtotal = db.Column(db.DECIMAL(12, 2), nullable=False)
    createtime = db.Column(db.DateTime, default=str(datetime.now()))

    def db2json(self):
        data = to_json(self)
        return data


class Hissorder(db.Model):
    __tablename__ = 'hissorder'
    sorderid = db.Column(db.String(64), primary_key=True, default=str(uuid1()))
    orderid = db.Column(db.String(64), nullable=False)
    addressid = db.Column(db.String(64), nullable=False)
    sellerid = db.Column(db.String(64), nullable=False)
    userid = db.Column(db.String(64), nullable=False)
    goodsname = db.Column(db.String(64), nullable=False)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(32), nullable=False)
    sumunit = db.Column(db.DECIMAL(12, 2), nullable=False)
    state = db.Column(db.String(4), default='1')
    createtime = db.Column(db.DateTime, default=str(datetime.now()))

    def db2json(self):
        data = to_json(self)
        return data


class Address(db.Model):
    __tablename__ = 'useraddress'
    addressid = db.Column(db.String(64), primary_key=True, default=str(uuid1()))
    userid = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    mobile = db.Column(db.String(32), nullable=False)
    address = db.Column(db.String(128))
    isfirst = db.Column(db.String(2), default='0')
    createtime = db.Column(db.DateTime, default=str(datetime.now()))

    def db2json(self):
        data = to_json(self)
        return data


def to_json(self):
    data = self.__dict__
    if "_sa_instance_state" in data:
        del data["_sa_instance_state"]
    if 'price' in data:
        data['price'] = float(data['price'])
    if 'sumunit' in data:
        data['sumunit'] = float(data['sumunit'])
    return data
