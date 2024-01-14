from .code_generator import Generator


def generate_first_name():
    g = Generator()
    return 'CleverUser-' + str(g.generate_code())

def generate_username():
    g = Generator()
    return 'clvr_' + str(g.generate_code())