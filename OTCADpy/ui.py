#Created by Stash Kempinski (stash.kempinski [at] secura.com)
import sys
import tkinter as tk
import json
import uuid
from os import path
from datetime import datetime
import pickle
from helpers.tktextwithvar import TextWithVar
from helpers.datasets import industries, attackTypes
from helpers.incident import IncidentUI as Incident

def SaveSources():
    ''' Save information present in source textbox.
    '''
    global selectedIncident
    selectedIncident.sources = sourcesTkVar.get()


def LoadIncident(incident: Incident):
    ''' Load an incident in the UI.
    '''
    global selectedIncident
    selectedIncident = incident
    sourcesTkVar.set(incident.sources)
    industryDropDown.set(incident.industry)
    attackTypeDropDown.set(incident.attackType)
    nameText['textvariable'] = incident.name
    yearText['textvariable'] = incident.year
    guidText['textvariable'] = incident.guid


def onOptionClick(event):
    ''' Click event for dropdown.
    '''
    SaveSources()
    UpdateMenu()
    LoadIncident(event)


def UpdateMenu():
    ''' Update dropdown menu.
    '''
    global opt
    global dropDownVar
    global cyberAttackData
    cyberAttackData.sort(key=lambda incident: incident.year.get())
    opt['menu'].delete(0, "end")
    for incident in cyberAttackData:
        opt['menu'].add_command(label=incident, command=tk._setit(dropDownVar, incident, onOptionClick))


def OnIndustryClick(event):
    ''' Updates the industry attribute of an incident.
    '''
    global selectedIncident
    selectedIncident.industry = event


def OnAttackTypeClick(event):
    ''' Attacker type change event.
    '''
    global selectedIncident
    selectedIncident.attackType = event

    button = tk.Button(dropWindow, text="Save", command = SaveJson)
    button.grid(row=0,column=1, sticky="ne")


def newIncident():
    ''' Creates a new incident.
    '''
    global cyberAttackData
    global opt
    global dropDownVar

    #Create new incident & add it to list
    newIncident = Incident("","",0,"","","")
    cyberAttackData.append(newIncident)

    UpdateMenu()

    #Set new data in window
    SaveSources()
    LoadIncident(newIncident)
    dropDownVar.set(newIncident)

def DumpIncident(incident: Incident):
    ''' Dump incident class to json parsable object.
    '''
    dumped = {}
    dumped['name'] = incident.name.get()
    dumped['year'] = incident.year.get()
    dumped['industry'] = incident.industry
    dumped['sources'] = incident.sources.split("\n")
    dumped['guid'] = incident.guid.get()
    dumped['attackType'] = incident.attackType

    return dumped

def SaveJson(event=None):
    ''' Save incidents to json.
    '''
    global cyberAttackData
    global dataFile

    SaveSources()
    UpdateMenu()

    jsonDumped = json.dumps(cyberAttackData, indent=4, default=DumpIncident)
    f = open(dataFile, "w")
    f.write(jsonDumped)
    f.close()

    print("Succesfully saved the cyber attacks.")

if __name__ == "__main__":
    #Create TK window
    window = tk.Tk()

    #Check if json file location is provided
    if len(sys.argv) < 2:
        print("Please provide the cyber attacks json file as argument.")
        print(f"For example: python3 ui.py \"..\\cyberattacks.json\"")
        quit()

    dataFile = sys.argv[1]

    if not path.isfile(dataFile):
        print("The provided json could not be found, please confirm that you entered the file path correctly.")
        quit()

    # Load Data
    cyberAttackDataFile = open(dataFile, "r")
    cyberAttackData = json.loads(cyberAttackDataFile.read(), object_hook=lambda d: Incident(**d))
    cyberAttackDataFile.close()
    cyberAttackData.sort(key=lambda incident: incident.year.get())
    selectedIncident = cyberAttackData[0]

    #### Create UI
    window.geometry('900x350')
    window.rowconfigure(1, minsize=800, weight=0)
    window.columnconfigure(0, minsize=800, weight=0)
    dropWindow = tk.Frame(window)
    editWindow = tk.Frame(window)
    dropWindow.grid(row=0, column=0, sticky="ns")
    editWindow.grid(row=1, column=0, sticky="nsew")
    rowNum = 0
    # Guid
    guidLabel = tk.Label(editWindow, text="GUID:")
    guidLabel.grid(row=rowNum,column=0, sticky="e")
    guidText = tk.Entry(editWindow, state="readonly", textvariable=selectedIncident.guid)
    guidText.grid(row=rowNum, column=1, sticky="nsew")
    rowNum = rowNum + 1
    # Name
    nameLabel = tk.Label(editWindow, text="Name:")
    nameLabel.grid(row=rowNum,column=0, sticky="e")
    nameText = tk.Entry(editWindow, textvariable=selectedIncident.name)
    nameText.grid(row=rowNum, column=1, sticky="nsew")
    rowNum = rowNum + 1
    # Year
    yearLabel = tk.Label(editWindow, text="Year:")
    yearLabel.grid(row=rowNum,column=0, sticky="e")
    yearText = tk.Entry(editWindow, textvariable=selectedIncident.year)
    yearText.grid(row=rowNum, column=1, sticky="nsew")
    rowNum = rowNum + 1
    # Industry
    industryLabel = tk.Label(editWindow, text="Industry:")
    industryLabel.grid(row=rowNum,column=0, sticky="e")
    industryDropDown = tk.Variable(window)
    industryDropDown.set(selectedIncident.industry)
    optIndustry = tk.OptionMenu(editWindow, industryDropDown, *industries, command=OnIndustryClick)
    optIndustry.grid(row=rowNum, column=1, sticky="nsew")
    rowNum = rowNum + 1
    # Sources
    sourcesTkVar = tk.StringVar(value=selectedIncident.sources)
    sourcesLabel = tk.Label(editWindow, text="Sources:")
    sourcesLabel.grid(row=rowNum,column=0, sticky="e")
    sourcesText = TextWithVar(editWindow, width=100, height=10, textvariable=sourcesTkVar)
    sourcesText.grid(row=rowNum, column=1, sticky="nsew")
    rowNum = rowNum + 1
    # Attacker type
    attackTypeLabel = tk.Label(editWindow, text="Attacker type:")
    attackTypeLabel.grid(row=rowNum,column=0, sticky="e")
    attackTypeDropDown = tk.Variable(window)
    attackTypeDropDown.set(selectedIncident.attackType)
    optIndustry = tk.OptionMenu(editWindow, attackTypeDropDown, *attackTypes, command=OnAttackTypeClick)
    optIndustry.grid(row=rowNum, column=1, sticky="nsew")
    rowNum = rowNum + 1
    # Dropdown
    dropDownVar = tk.Variable(window)
    dropDownVar.set(cyberAttackData[0])
    opt = tk.OptionMenu(dropWindow, dropDownVar, *cyberAttackData, command=onOptionClick)
    opt.config(width=90, font=('Helvetica', 12))
    opt.grid(row=0, column=0, sticky="nw")
    #"new" button
    button = tk.Button(dropWindow, text="New", command = newIncident)
    button.grid(row=0,column=2, sticky="ne")

    #Save shortcut
    window.bind("<Control-s>", SaveJson)

    #### MAIN LOOP
    window.mainloop()
