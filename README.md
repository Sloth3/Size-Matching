# Size-Matching

Work 1 is for Shirts
Work 2 is for Pants

***All input files extensions are txt, but format of the files are of CSV(must be comma-seperated)**

Work 1 required input files:
weightage: all possibilites of weigtage depeding on how man factors there are (e.g. waist, chest)
size: sizes of all factors (e.g. waist, chest) and size taken(to match against predicted size)

Work 1 output file:
final: contain all possible weightage and it's percentage match in decimal (e.g. chest_w:1, waist_w:1, hip_w:98, percentage_match: 0.5 which is 50% or e.g. 12/24)

Work 2 required input files:
weightage: all possibilites of weightage depeding on how many factors there are (e.g. waist, chest)
weightage have two files, one for two factors only and the other for three factors
size: sizes of **all factors** (e.g. waist, chest), **height** and **size taken**(to match against predicted size)

Work 2 output file:
final: contain all possible weightage and it's percentage match in decimal (e.g. chest_w:1, waist_w:1, hip_w:98, percentage_match: 0.5 which is 50% or e.g. 12/24)


**Need Python to run script**
1. Go into directory of the script using console
2. run "**$python3 work.py**" to run script
