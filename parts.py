import pickle

from spaces import Space

parts = []

class Part:
    def __init__(self, name, space=None):
        self.name = name
        if space:
            self.space = space
        else:
            f = open(self.get_filename(), "rb")
            temp_part =  pickle.load(f)
            self = temp_part

    def save(self):
        f = open(self.get_filename(), "wb")
        pickle.dump(self, f)

    def get_filename(self):
        return "parts/%s.prt" % self.name
