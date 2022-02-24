import uuid
import json
import helpers.mitre as mitre
import sys
from os import path, remove
import time
import pickle
import helpers.datasets as ds
from helpers.incident import Incident


###########################
### functions & classes ###
###########################

#Create mitre dict for guid
def FillMitre(attackFolder: str, guid: str):
    ''' Parse the ATT&CK for ICS matrix json file to find out which techniques & tactics are used (or not) for an incident
    '''
    mitreDict = mitre.getEmptyTacticDict([])

    #If guid is found, parse
    if path.exists(f"{attackFolder}/{guid}.json"):
        jsonMitreFile = open(f"{attackFolder}/{guid}.json", "r")
        jsonMitre = json.loads(jsonMitreFile.read())
        jsonMitreFile.close()

        foundTactics = [] #Tactics that DO NOT need an "unknown"
        
        #Loop over techniques in technique array
        for technique in jsonMitre['techniques']:
            tactic = technique['tactic']
            foundTactics.append(tactic)

            techniqueId = 'Not applicable'
            if technique['color'] == "":
                techniqueId = technique['techniqueID']

            mitreDict[tactic].append(techniqueId)
        
        #Add unknown to missing tactics
        for tactic in mitre.tactics:
            if tactic not in foundTactics:
                mitreDict[tactic].append("Unknown")
    else:
        print(f"WARNING: unable to find json for guid [{guid}], this incident is excluded")
        return False


    #Sanity check
    for tactic in mitreDict:
        if ("Unknown" in mitreDict[tactic] or 'Not applicable' in mitreDict[tactic]) and len(mitreDict[tactic]) > 1:
            raise ValueError(f"The matrix for [{guid}] is filled in wrong: Unknown, Not applicable, and any techniques are mutually exclusive for a tactic. Please check if you have both a color and a technique selected somewhere for this GUID.")

    return mitreDict

def parseIncidents(jsonFile: str, attackFolder: str):
    ''' Parse all incidents
    '''
    #Open & parse file
    risidataFile = open(jsonFile, "r")
    incidents = json.loads(risidataFile.read(), object_hook=lambda d: Incident(**d))
    risidataFile.close()

    #Parse ATT&CK matrix
    incidentsToRemove = []
    for incident in incidents:
        incident.mitre = FillMitre(attackFolder, incident.guid)

        if not incident.mitre:
            incidentsToRemove.append(incident)

    incidents = [i for i in incidents if i not in incidentsToRemove]
    #Save raw incidents
    with open("cache.blob", "wb") as f:
        pickle.dump(time.ctime(path.getmtime(jsonFile)), f)
        pickle.dump(time.ctime(path.getmtime(attackFolder)), f)
        pickle.dump(incidents, f)
    
    return incidents








