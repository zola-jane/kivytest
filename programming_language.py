class ProgrammingLanguage:
    def __init__(self, program="", typing=True, reflection="", year=0):
        self.program = program
        self.type = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".\
        format(self.program, self.type, self.reflection, self.year)

    def is_dynamic(self):
        if self.type == "Dynamic":
            return True
