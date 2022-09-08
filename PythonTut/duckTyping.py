class pyCharm(object):
    """docstring for pyCharm"""

    def __init__(self):
        pass

    def execute(self):
        print("Compiling")
        print("Running")


class myEditor(object):
    """docstring for myEditor"""

    def __init__(self):
        pass

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop(object):
    """docstring for Laptop"""

    def __init__(self):
        pass

    def code(self, ide):
        ide.execute()


ide = pyCharm()
ide2 = myEditor()

lap1 = Laptop()
lap1.code(ide2)