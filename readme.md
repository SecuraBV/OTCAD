# Operational Technology Cyber Attack Database (OTCAD)
OTCAD is a database of cyber attacks on OT/ICS mapped to MITRE's [ATT&CK® for ICS](https://collaborate.mitre.org/attackics/index.php/Main_Page) (v8). The database is easily extendable and adjustable through the use of both new and existing tools. Its main goal is to quickly get statistical, historical, and categorized data that can also be publicly confirmed. Using OTCAD should be effortless through the usage of ATT&CK for ICS' widely used terminology and existing tools.

The whitepaper that presents and discusses OTCAD in depth will be released very soon. This whitepaper also contains the methodology and information sources used to build the initial release of OTCAD.


## The database
#### Cyberattacks.json
This json file contains the database with all cyber attacks currently present in OTCAD. Each cyber attack contains the following attributes:
| Attribute     | Comment                                                                                       |
| ---------     | -------                                                                                       |
| guid          | Unique identifier for the cyber attack, used to link a cyber attack with its mapping data     |
| name          | Name of the cyber attack                                                                      |
| year          | Year in which the cyber attack took place                                                     |
| sources       | Array of the sources used to create the mapping from                                          |
| attackType    | Classification of attacker (e.g. disgruntled employee)*                                       |
| industry      | Industry of the organization that was attacked (e.g. electrical manufacturing)*               |
*The possible classifications can be found in the whitepaper

#### Cyberattacks folder
This folder contains the ATT&CK for ICS mappings for each cyber attack as an individual file. Each file is named after the GUID of the cyber attack and is fully compatible with MITRE's [attack navigator](https://mitre-attack.github.io/attack-navigator/). 


## How to use OTCAD
#### Adding new cyber attacks
A new cyber attack can be added to OTCAD by including its information in cyberattacks.json, this can either be done manually (do not forget to create an unique GUID) or through OTCADpy's UI (see next section).
Using MITRE's [attack navigator](https://mitre-attack.github.io/attack-navigator/) new mappings can be created using the ATT&CK v8 ICS layer.
![Create a new ATT&CK v8 ICS layer](https://i.imgur.com/iK2G2oG.png)

The techniques used in the new cyber attack can be selected by using the toggling the state ("Toggle state") in the right top technique controls, **do not forget to disable "select techniques across tactics" (in selection controls) as OTCAD differentiates on for what purpose a technique is used**. If an tactic is not applicable to the new cyber attack, color a single technique in that tactic (can be achieved using the background color option next to the toggle state option). This color allows to differentiate between a tactic being used but it is unknown which technique is used and a tactic being not applicable. The next screenshot is an example of the "Rootkit" technique being selected, Lateral Movement being not applicable, and for all other tactics the used technique(s) being unknown.
![Example navigator](https://i.imgur.com/FqahoMd.png)

Lastly, export the json through the "download layer as json" option and add it, named as the newly created GUID, to the cyberattacks folder.


#### OTCADpy
OTCADpy is a set of Python 3.9 scripts that can be used to easily extract information from, and add new cyber attacks to, OTCAD. OTCADpy consists of an UI to add new cyber attacks to the database and scroll through the existing ones. Furthermore, it contains scripts to get statistical data from OTCAD in multiple ways. More information can be found in the readme in the OTCADpy folder.

## How to contribute to OTCAD
Just send a merge request with your changes!

## Questions?
Do not hesitate to mail the creator of OTCAD: stash.kempinski [at] secura.com