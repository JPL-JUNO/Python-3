"""
@File         : readCensusExcel.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-08-31 10:49:06
@Email        : cuixuanstephen@gmail.com
@Description  : Tabulates population and number of census tracts for each county.
"""

import openpyxl, pprint

print("Opening workbook...")
wb = openpyxl.load_workbook("data/censuspopdata.xlsx")
sheet = wb["Population by Census Tract"]
county_data = {}

print("Reading rows...")
for row in range(2, sheet.max_row + 1):
    state = sheet[f"B{row}"].value
    county = sheet[f"C{row}"].value
    pop = sheet[f"D{row}"].value

    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {"tracts": 0, "pop": 0})

    county_data[state][county]["tracts"] += 1
    county_data[state][county]["pop"] += int(pop)

print("Writing results...")
result_file = open("data/census2010.py", "w")
result_file.write("allData = " + pprint.pformat(county_data))
result_file.close()
print("Done.")
