"""
script that makes nice csvs with data on a district level
using then census data and api
e.g.
'',area01, area02 ...
pop, 1234, 456789 ...
...
"""


import sys
from collections import defaultdict
import csv

from census import Census
from us import states


def query_census(thing, num_dists, c, results):
    for (k, v) in thing:

        for i in range(12, 13):
            dist_id = str(i).zfill(2)
            data = c.acs5.state_district(
                ('NAME', k),
                states.CA.fips,
                dist_id
            )

            results[dist_id].append((v, data[0][k]))

    return results


def write_csv(filename, data):
    csv_output = [['', ], ]
    for i, (k, v) in enumerate(data.items()):
        if i == 0:
            csv_output[0].append(k)
            for i, (thing, number) in enumerate(v):
                csv_output.append([thing])
                csv_output[i + 1].append(number)
        else:
            csv_output[0].append(k)
            for j, (_, number) in enumerate(v):
                csv_output[j + 1].append(number)

    with open(filename, 'wb') as w:
        writer = csv.writer(w)
        writer.writerows(csv_output)


def main():
    """
    """
    key_pop_sum = [
        ('B02001_001E', 'Total Population'),
        ('B02001_002E', 'White'),
        ('B02001_003E', 'Black or African American alone'),
        ('B02001_004E', 'American Indian and Alaska Native alone'),
        ('B02001_005E', 'Asian'),
        ('B02001_006E', 'Hawaiian and Other Pacific Islander'),
        ('B02001_007E', 'Other race'),
        ('B02001_008E', 'Two or more races:'),
    ]

    key_med_age_by_pop = [
        ('B01002_001E', 'Total Pop. Median age, male and female'),
        ('B01002_002E', 'Total Pop. Median age, male'),
        ('B01002_003E', 'Median age, female'),
        ('B01002A_001E', 'White Median age, male and female'),
        ('B01002A_002E', 'White Median age, male'),
        ('B01002A_003E', 'White Median age, female'),
        ('B01002B_001E', 'Black/African Amer. Median age, male and female'),
        ('B01002B_002E', 'Median age, male'),
        ('B01002B_003E', 'Median age, female'),
        ('B01002C_001E', 'A. Indidan/Alaska Median age, male and female'),
        ('B01002C_002E', 'A. Indidan/Alaska Median age, male'),
        ('B01002C_003E', 'A. Indidan/Alaska Median age, female'),
        ('B01002D_001E', 'Asian Median age, male and female'),
        ('B01002D_002E', 'Asian Median age, male'),
        ('B01002D_003E', 'Asian Median age, female'),
        ('B01002E_001E', 'Hawaiian/Pac. Islander Median age, male and female'),
        ('B01002E_002E', 'Hawaiian/Pac. Islander Median age, male'),
        ('B01002E_003E', 'Hawaiian/Pac. Islander Median age, female'),
        ('B01002F_001E', 'Other Median age, male and female'),
        ('B01002F_002E', 'Other Median age, male'),
        ('B01002F_003E', 'Other Median age, female'),
        ('B01002G_001E', 'Two or More Median age, male and female'),
        ('B01002G_002E', 'Two or More Median age, male'),
        ('B01002G_003E', 'Two or More Median age, female'),
    ]

    education = [
        ('B06009_002E', 'Less than high school graduate'),
        ('B06009_003E', 'High school graduate (includes equivalency)'),
        ('B06009_004E', 'Some college or associates degree'),
        ('B06009_005E', 'Bachelors degree'),
        ('B06009_006E', 'Graduate or professional degree'),
    ]

    income = [
        ('B06010_002E', 'No income'),
        ('B06010_003E', 'With income:'),
        ('B06010_004E', '$1 to $9,999 or loss'),
        ('B06010_005E', '$10,000 to $14,999'),
        ('B06010_006E', '$15,000 to $24,999'),
        ('B06010_007E', '$25,000 to $34,999'),
        ('B06010_008E', '$35,000 to $49,999'),
        ('B06010_009E', '$50,000 to $64,999'),
        ('B06010_010E', '$65,000 to $74,999'),
        ('B06010_011E', '$75,000 or more'),
    ]

    transportation_to_work = [
        ('B08006_002E', 'Car, truck, or van:'),
        ('B08006_003E', 'Drove alone'),
        ('B08006_004E', 'Carpooled:'),
        ('B08006_005E', 'In 2-person carpool'),
        ('B08006_006E', 'In 3-person carpool'),
        ('B08006_007E', 'In 4-or-more-person carpool'),
        ('B08006_008E', 'Public transportation (excluding taxicab):'),
        ('B08006_009E', 'Bus or trolley bus'),
        ('B08006_010E', 'Streetcar or trolley car (carro publico in Puerto Rico)'),
        ('B08006_011E', 'Subway or elevated'),
        ('B08006_012E', 'Railroad'),
        ('B08006_013E', 'Ferryboat'),
        ('B08006_014E', 'Bicycle'),
        ('B08006_015E', 'Walked'),
        ('B08006_016E', 'Taxicab, motorcycle, or other means'),
        ('B08006_017E', 'Worked at home'),
    ]

    work_industry = [
        ('B08126_002E', 'Agriculture, forestry, fishing and hunting, and mining'),
        ('B08126_003E', 'Construction'),
        ('B08126_004E', 'Manufacturing'),
        ('B08126_005E', 'Wholesale trade'),
        ('B08126_006E', 'Retail trade'),
        ('B08126_007E', 'Transportation and warehousing, and utilities'),
        ('B08126_008E', 'Information'),
        ('B08126_009E', 'Finance and insurance, and real estate and rental and leasing'),
        ('B08126_010E', 'Professional, scientific, and management, and administrative and waste management services'),
        ('B08126_011E', 'Educational services, and health care and social assistance'),
        ('B08126_012E', 'Arts, entertainment, and recreation, and accommodation and food services'),
        ('B08126_013E', 'Other services (except public administration)'),
        ('B08126_014E', 'Public administration'),
        ('B08126_015E', 'Armed forces'),
    ]

    food_stamps = [
        ('B22001_001E', 'Total:'),
        ('B22001_002E', 'Household received Food Stamps/SNAP in the past 12 months:'),
        ('B22001_003E', 'At least one person in household 60 years or over'),
        ('B22001_004E', 'No people in household 60 years or over'),
        ('B22001_005E', 'Household did not receive Food Stamps/SNAP in the past 12 months'),
        ('B22001_006E', 'At least one person in household 60 years or over'),
        ('B22001_007E', 'No people in household 60 years or over'),
    ]

    less_high_school_edu_by_emp = [
        ('B23006_003E', 'Less than high school In labor force:'),
        ('B23006_004E', 'Less than high school In Armed Forces'),
        ('B23006_005E', 'Less than high school Civilian:'),
        ('B23006_006E', 'Less than high school Employed'),
        ('B23006_007E', 'Less than high school Unemployed'),
        ('B23006_008E', 'Less than high school Not in labor force'),
    ]

    high_school = [
        ('B23006_010E', 'Finished high school In labor force:'),
        ('B23006_011E', 'Finished high school In Armed Forces'),
        ('B23006_012E', 'Finished high school Civilian:'),
        ('B23006_013E', 'Finished high school Employed'),
        ('B23006_014E', 'Finished high school Unemployed'),
        ('B23006_015E', 'Finished high school Not in labor force'),
    ]

    college_degree = [
        ('B23006_017E', 'Some college or associates degree, In labor force:'),
        ('B23006_018E', 'Some college or associates degree, In Armed Forces'),
        ('B23006_019E', 'Some college or associates degree, Civilian:'),
        ('B23006_020E', 'Some college or associates degree, Employed'),
        ('B23006_021E', 'Some college or associates degree, Unemployed'),
        ('B23006_022E', 'Some college or associates degree, Not in labor force'),
    ]

    bach_or_more = [
        ('B23006_024E', 'Bach or higher In labor force:'),
        ('B23006_025E', 'Bach or higher In Armed Forces'),
        ('B23006_026E', 'Bach or higher Civilian:'),
        ('B23006_027E', 'Bach or higher Employed'),
        ('B23006_028E', 'Bach or higher Unemployed'),
        ('B23006_029E', 'Bach or higher Not in labor force'),
    ]

    #TODO: Remove token and make it an arg
    c = Census("fc66937306461fac65ad897de2055460013f5075")

    results = defaultdict(list)
    query_census(key_pop_sum, 54, c, results)
    query_census(key_med_age_by_pop, 54, c, results)
    query_census(work_industry, 54, c, results)
    query_census(bach_or_more, 54, c, results)
    query_census(less_high_school_edu_by_emp, 54, c, results)
    query_census(high_school, 54, c, results)
    query_census(college_degree, 54, c, results)
    query_census(income, 54, c, results)
    query_census(education, 54, c, results)

    write_csv('data.csv', results)


if __name__ == '__main__':
    main()
