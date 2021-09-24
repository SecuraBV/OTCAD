# OTCADpy
## UI
The UI uses the tkinter package to provide a simple and quick interface to cyberattacks.json, the top dropdown enables the user to easily go through all cyber attacks, change their information, or add new ones. ui.py takes as only argument the cyberattacks.json. 
**You can save changed data using the CTRL+S shortcut.**

## Statistics
OTCADpy enables users to easily filter cyber attacks from OTCAD in arbitrary ways and extract statistical data from them. The getStatistics.py script creates an overview of the different attacker classifications, industry domains, and the occurences per ATT&CK for ICS technique. This overview can be generated as one total overview, or a per year overview which get parsed into their respective excel workbooks. The empty versions of these workbooks can be found in the "excel frames" folder.

### Per Year
By default, the per year statistics get generated on a cummulative basis, meaning that the statistics present in a year are from the start up until and including that year. This choice was made as it creates better readable graphs, but can be changed to liking (see the "Filter cyber attacks" section).

### Total
The total overview shows the total amount that each technique was used and the percentage it occurred in all cyber attacks. The added "Unknown" and "Not applicable" options can be found at the bottom of each tactic.

### getStatistics.py

Four arguments:
| Argument | Comment                                                  |
| -----    | -----                                                    |
| First    | path to the cyberattacks json file                       |
| Second   | path to the cyberattacks folder                          |
| Third    | do you want to generate **total** or **year** statistics |
| Fourth   |  Name of the resulting Excel workbook                    |

#### Filter cyber attacks
Using the FilterIncidents(PerYear) functions (line 12 & 24) of getStatistics.py it is possible to quickly filter incidents to liking (for example, if you only want statistics from targeted attacks). Multiple filters exist already, which can be from line 33 onwards, and can be chained (see the example in the FilterIncidents function).

## Contributions
Contributions are always welcome!