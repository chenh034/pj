class Model:
    test = ''

    def to_dict(self):
        return {col.name: getattr(self, col.name, None) for col in self.__table__.columns}

