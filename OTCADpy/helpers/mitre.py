# Created by Stash Kempinski (stash.kempinski [at] secura.com)

#Technique IDs with their human readable variant
techniques = {
'T0800': 'Activate Firmware Update Mode', 
'T0878': 'Alarm Suppression', 
'T0802': 'Automated Collection', 
'T0803': 'Block Command Message', 
'T0804': 'Block Reporting Message', 
'T0805': 'Block Serial COM', 
'T0806': 'Brute Force I/O', 
'T0875': 'Change Program State', 
'T0807': 'Command-Line Interface', 
'T0885': 'Commonly Used Port', 
'T0884': 'Connection Proxy', 
'T0808': 'Control Device Identification', 
'T0879': 'Damage to Property', 
'T0809': 'Data Destruction', 
'T0810': 'Data Historian Compromise',
'T0811': 'Data from Information Repositories', 
'T0812': 'Default Credentials', 
'T0813': 'Denial of Control', 
'T0814': 'Denial of Service', 
'T0815': 'Denial of View', 
'T0868': 'Detect Operating Mode', 
'T0870': 'Detect Program State', 
'T0816': 'Device Restart/Shutdown', 
'T0817': 'Drive-by Compromise', 
'T0818': 'Engineering Workstation Compromise', 
'T0871': 'Execution through API', 
'T0819': 'Exploit Public-Facing Application', 
'T0820': 'Exploitation for Evasion', 
'T0866': 'Exploitation of Remote Services', 
'T0822': 'External Remote Services', 
'T0823': 'Graphical User Interface', 
'T0874': 'Hooking', 
'T0877': 'I/O Image', 
'T0824': 'I/O Module Discovery', 
'T0872': 'Indicator Removal on Host', 
'T0883': 'Internet Accessible Device', 
'T0825': 'Location Identification', 
'T0826': 'Loss of Availability', 
'T0827': 'Loss of Control', 
'T0828': 'Loss of Productivity and Revenue', 
'T0880': 'Loss of Safety', 
'T0829': 'Loss of View', 
'T0830': 'Man in the Middle', 
'T0835': 'Manipulate I/O Image', 
'T0831': 'Manipulation of Control', 
'T0832': 'Manipulation of View',
'T0849': 'Masquerading', 
'T0838': 'Modify Alarm Settings', 
'T0833': 'Modify Control Logic', 
'T0836': 'Modify Parameter', 
'T0839': 'Module Firmware', 
'T0801': 'Monitor Process State', 
'T0840': 'Network Connection Enumeration', 
'T0841': 'Network Service Scanning', 
'T0842': 'Network Sniffing', 
'T0861': 'Point & Tag Identification', 
'T0843': 'Program Download', 
'T0844': 'Program Organization Units', 
'T0845': 'Program Upload', 
'T0873': 'Project File Infection', 
'T0867': 'Remote File Copy', 
'T0846': 'Remote System Discovery', 
'T0847': 'Replication Through Removable Media',
'T0848': 'Rogue Master Device', 
'T0850': 'Role Identification', 
'T0851': 'Rootkit', 
'T0852': 'Screen Capture', 
'T0853': 'Scripting', 
'T0854': 'Serial Connection Enumeration', 
'T0881': 'Service Stop', 
'T0865': 'Spearphishing Attachment', 
'T0856': 'Spoof Reporting Message', 
'T0869': 'Standard Application Layer Protocol', 
'T0862': 'Supply Chain Compromise', 
'T0857': 'System Firmware', 
'T0882': 'Theft of Operational Information', 
'T0855': 'Unauthorized Command Message', 
'T0863': 'User Execution', 
'T0858': 'Utilize/Change Operating Mode', 
'T0859': 'Valid Accounts', 
'T0860': 'Wireless Compromise'
}

#Dictionary with the human readable version of each tactic
tactics = { 
    "initial-access-ics": "Initial access",
    "execution-ics": "Execution",
    "persistence-ics": "Persistence",
    "evasion-ics": "Evasion",
    "discovery-ics": "Discovery",
    "lateral-movement-ics": "Lateral Movement",
    "collection-ics": "Collection",
    "command-and-control-ics": "Command and Control",
    "inhibit-response-function": "Inhibit Response Function",
    "impair-process-control": "Impair Process Control",
    "impact-ics": "Impact"
}

#All techniques per tactic
techniquesInTactic = {
'inhibit-response-function': ['T0800', 'T0878', 'T0803', 'T0804', 'T0805', 'T0809', 'T0814', 'T0816', 'T0835', 'T0838', 'T0833', 'T0843', 'T0851', 'T0857', 'T0858'], 
'collection-ics': ['T0802', 'T0811', 'T0868', 'T0870', 'T0877', 'T0825', 'T0801', 'T0861', 'T0845', 'T0850', 'T0852'], 
'impair-process-control': ['T0806', 'T0875', 'T0849', 'T0833', 'T0836', 'T0839', 'T0843', 'T0848', 'T0881', 'T0856', 'T0855'],
'execution-ics': ['T0875', 'T0807', 'T0871', 'T0823', 'T0830', 'T0844', 'T0873', 'T0853', 'T0863'], 
'command-and-control-ics': ['T0885', 'T0884', 'T0869'], 
'discovery-ics': ['T0808', 'T0824', 'T0840', 'T0841', 'T0842', 'T0846', 'T0854'], 
'impact-ics': ['T0879', 'T0813', 'T0815', 'T0826', 'T0827', 'T0828', 'T0880', 'T0829', 'T0831', 'T0832', 'T0882'], 
'initial-access-ics': ['T0810', 'T0817', 'T0818', 'T0819', 'T0822', 'T0883', 'T0847', 'T0865', 'T0862', 'T0860'], 
'lateral-movement-ics': ['T0812', 'T0866', 'T0822', 'T0844', 'T0867', 'T0859'], 
'evasion-ics': ['T0820', 'T0872', 'T0849', 'T0848', 'T0851', 'T0856', 'T0858'], 
'persistence-ics': ['T0874', 'T0839', 'T0843', 'T0873', 'T0857', 'T0859']
}

def getReadableTactics():
    ''' Get the "human readable" names of the tactics
    '''
    readableNames = []
    for tactic in tactics:
        readableNames.append(tactics[tactic])
    
    return readableNames

def getEmptyTacticDict(defaultVar):
    ''' Generate a dictionary for all tactics filled with a default var
    '''
    mitreDict = {}
    for tactic in tactics:
            mitreDict[tactic] = type(defaultVar)()

    return mitreDict

def getTechniqueDict(pTactic, defaultVar, readable=False):
    ''' Generate a dictionary of techniques for a tactic filled with a default var
        Optionally use the human readable variant of the techniques
    '''
    if pTactic not in techniquesInTactic:
        raise NameError(f"Tactic {pTactic} not found, are you using the id of the tactic? (e.g. \"lateral-movement-ics\" instead of \" Lateral Movement\"")

    techniqueDict = {}
    for technique in techniquesInTactic[pTactic]:
        if readable:
            techniqueDict[techniques[technique]] = type(defaultVar)()
        else:
            techniqueDict[technique] = type(defaultVar)()
    
    return techniqueDict