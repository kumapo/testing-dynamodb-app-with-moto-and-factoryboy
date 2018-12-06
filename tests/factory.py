import factory
import factory.fuzzy
import datetime
import uuid
import dataclasses

class ChatFactory(factory.Factory):
    class Meta:
        model = dataclasses.make_dataclass('Chat', ['id', 'message_id', 'message', 'message_date', 'username'])

    id = factory.Faker('uuid4')
    message_id = factory.Faker('uuid4')
    message = factory.Faker('sentence', locale='ja_JP')
    message_date = factory.LazyFunction(datetime.datetime.utcnow().isoformat)
    username = factory.Faker('user_name')

    @classmethod
    def dict_factory(cls, create=False, extra=None):
        # https://github.com/FactoryBoy/factory_boy/blob/master/factory/base.py#L443
        declarations = cls._meta.pre_declarations.as_dict()
        declarations.update(extra or {})
        return factory.make_factory(dict, **declarations)