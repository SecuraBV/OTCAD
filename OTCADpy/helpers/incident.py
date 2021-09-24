#Created by Stash Kempinski (stash.kempinski [at] secura.com)
import tkinter as tk
import uuid

class Incident(object):
    """ Incident class used in the statistics scripts.
    """
    def __init__(self, name, year, industry, sources=None, mitre=None, guid=None, attackType=None):
        self.guid = guid
        self.name = name
        self.year = int(year)
        self.industry = industry
        self.sources = sources
        self.attackType = attackType
        self.mitre = mitre

class IncidentUI(object):
    """ Incident class used in the UI.
        This class contains tkinter variables used to interact with the UI.
    """
    def __init__(self, name, year, industry, sources=None, guid=None, attackType=None):
        if guid == None:
            guid = uuid.uuid4()

        self.guid = tk.StringVar(value=guid)
        self.name = tk.StringVar(value=name)
        self.year = tk.IntVar(value=int(year))
        self.industry = industry
        self.sources = '\n'.join(sources)
        self.attackType = attackType

    def __str__(self):
            extra = f"({self.year.get()}) "
            return extra + self.name.get()

    def __repr__(self):
            return self.name.get()