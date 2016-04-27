from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    make_list(python)
    make_list(ruby)
    make_list(vb)

    program_dictionary = {1: make_list(python), 2: make_list(ruby), 3: make_list(vb)}
    is_dynamic(program_dictionary)


def make_list(object_name):
    new_list = str(object_name).split(", ")
    return new_list


def is_dynamic(dictionary):
    print("The dynamically typed languages are:")
    for key in dictionary:
        program_list = dictionary[key]
        if "Dynamic Typing" in program_list:
            print(program_list[0])


main()
