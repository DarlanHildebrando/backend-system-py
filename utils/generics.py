class Generics:
     @staticmethod
     def get_generic(model, parameters=None, single=None):
        if parameters is None:
            parameters = {}

        if single:
            return model.objects.get(**parameters)
        return model.objects.filter(**parameters)