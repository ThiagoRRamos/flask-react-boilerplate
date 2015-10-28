from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
mongo_db = client.woohoo

class MongoAttribute(object):

    def __init__(self, key):
        self.key = key

    def __get__(self, instance, owner):
        return instance._data[self.key]

    def __set__(self, instance, value):
        instance._data[self.key] = value

class ClassProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()

class BaseObject(object):
    class Meta(object):
        db = 'woohoo'
        collection = 'default'

    def __init__(self, *args, **kwargs):
        self._data = {}
        for el in kwargs:
            self._data[el] = kwargs[el]

    @ClassProperty
    @classmethod
    def collection(cls):
        return client[cls.Meta.db][cls.Meta.collection]

    @classmethod
    def find_one(cls, *args, **kwargs):
        res = cls.collection.find_one(*args, **kwargs)
        if res:
            return cls(**res)

    @classmethod
    def find(cls, *args, **kwargs):
        for result in cls.collection.find(*args, **kwargs):
            yield cls(**result)

    id = MongoAttribute('_id')

    def save(self):
        if '_id' in self._data:
            return self.collection.update_one({'_id': self.id}, {'$set': self._data})
        self.id = self.collection.insert_one(self._data).inserted_id

    def __setitem__(self, key, item):
        self._data[key] = item

    def __getitem__(self, key):
        return self._data[key]