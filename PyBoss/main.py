#This program takes .csv files as input with five fields Emp ID,Name,DOB,SSN,
#State. The input files should reside in the same dir as this program resides.
#It outputs a file in the output directory which resides immediately outside the 
# dir where the code resides. The output files will have the fields formated as follows: 
#Emp ID remains unchanged, Name gets replaced by the first name and last name,
#DOB gets translated from 'YYYYMMDD' into 'MMDDYYYY', US State gets replaced by
#the corresponding State abbreviation.

import os
import csv
import datetime 

#Dictionary for US State Abbreviations
USStateAbbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Establish the root path and resource path
#resource_path = os.path.join(os.getcwd(), "Resources")
resource_path = os.getcwd()

# Iterate through the listdir results
filepaths = []
for file in os.listdir(resource_path):
    if file.endswith(".csv"):
        filepaths.append(os.path.join(resource_path, file))

# Read each csv into a dictionary and create an email address using the first
# initial and lastname "John Glenn" becomes "jglenn@example.com"
for file in filepaths:
	newEmpData = []

    # Read data into dictionary and create a new email field
	with open(file) as csvfile:
		csvRead = csv.DictReader(csvfile)
		for row in csvRead:
			#first name
			firstName = row["Name"].split()[0]
			lastName = row["Name"].split()[1]
			dateOfBirth = datetime.datetime.strptime(row["DOB"], '%Y-%m-%d').strftime('%m/%d/%y')
			socialSecNum = row["SSN"][:0] + "***-**-" + row["SSN"][7:]
			state = USStateAbbrev[row["State"]]
			empDict = {"Emp ID": "{Emp ID}".format(**row), "First Name": firstName,  "Last Name": lastName, "DOB":dateOfBirth, "SSN": socialSecNum,"State": state }
			newEmpData.append({**empDict})

    #  Write updated data to csv file
	output_path = os.path.join(resource_path, "output")

    # Grab the filename from the original path
	_, filename = os.path.split(file)
	csvpath = os.path.join(output_path, filename)

	#Write above dictionary newEmpData to output file
	with open(csvpath, "w") as csvfile:
		fieldnames = ["Emp ID", "First Name", "Last Name","DOB","SSN","State"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
		writer.writeheader()
		writer.writerows(newEmpData)