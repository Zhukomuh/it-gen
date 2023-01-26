class PhaseSwitcherDescriptor:
    def __init__(self, value, phase: bool = True):
        self.value = value
        self.phase = phase

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if self.phase is True:
            self.value = value
            return self.value
        else:
            raise AttributeError("Field is read only")

    def __delete__(self, instance):
        if self.phase is True:
            del self.value
        else:
            raise AttributeError("Field is read only")


class Sample:
    sample_field = PhaseSwitcherDescriptor(34, False)

    def __str__(self):
        return f'Field: {self.sample_field}'
