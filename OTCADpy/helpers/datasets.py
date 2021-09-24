#Created by Stash Kempinski (stash.kempinski [at] secura.com)

#Classification of industries
industries = ['Pulp and Paper', 'Power and Utilities', 'Food & Beverage', 'Electronic Manufacturing', 'Transportation', 'Petroleum', 'Water/Waste Water', 'Chemical', 'Metals', 'Automotive', 'General Manufacturing', 'Pharmaceutical', 'Other', 'Unknown']

#Classification of attackers
attackTypes = ['Disgruntled Employee', 'Targeted Attack', 'Untargeted Attack', 'Unknown']

def getEmptyIndustryDict(defaultVar):
    industryDict = {}
    for industry in industries:
            industryDict[industry] = type(defaultVar)()

    return industryDict

def getEmptyAttackerDict(defaultVar):
    attackDict = {}
    for attacker in attackTypes:
            attackDict[attacker] = type(defaultVar)()

    return attackDict