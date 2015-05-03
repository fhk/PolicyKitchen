"""
script that makes nice csvs with data on a district level
using then census data and api
e.g.
'',area01, area02 ...
pop, 1234, 456789 ...
...
"""


import sys
import csv

from census import Census
from us import states


def query_census(thing, c, results):
    for (k, v, join) in thing:
        # no validation on query for state being a fip
        for state in states.STATES:
            data = c.acs5.state(
                ('NAME', k),
                state.fips
            )
            results.append([v, join, state, data[0][k]])

    return results


def write_csv(filename, data):
    with open(filename, 'wb') as w:
        writer = csv.writer(w)
        writer.writerows(data)


def main():
    """
    """
    key_pop_sum = [
        ('B02001_001E', 'Total Population', 'All'),
        ('B02001_002E', 'White', 'All'),
        ('B02001_003E', 'Black or African American alone','All'),
        ('B02001_004E', 'American Indian and Alaska Native alone', 'All'),
        ('B02001_005E', 'Asian', 'All'),
        ('B02001_006E', 'Hawaiian and Other Pacific Islander', 'All'),
        ('B02001_007E', 'Other race', 'All'),
        ('B02001_008E', 'Two or more races:', 'All'),
    ]

    education = [
        ('B06009_002E', 'Less than high school graduate', 'All'),
        ('B06009_003E', 'High school graduate (includes equivalency)', 'All'),
        ('B06009_004E', 'Some college or associates degree', 'All'),
        ('B06009_005E', 'Bachelors degree', 'All'),
        ('B06009_006E', 'Graduate or professional degree', 'All'),
    ]

    income = [
        ('B06010_002E', 'No income', 'All'),
        ('B06010_003E', 'With income:', 'All'),
        ('B06010_004E', '$1 to $9,999 or loss', 'All'),
        ('B06010_005E', '$10,000 to $14,999', 'All'),
        ('B06010_006E', '$15,000 to $24,999', 'All'),
        ('B06010_007E', '$25,000 to $34,999', 'All'),
        ('B06010_008E', '$35,000 to $49,999', 'All'),
        ('B06010_009E', '$50,000 to $64,999', 'All'),
        ('B06010_010E', '$65,000 to $74,999', 'All'),
        ('B06010_011E', '$75,000 or more', 'All'),
    ]

    work_industry = [
        ('B08126_002E', 'Agriculture, forestry, fishing and hunting, and mining', 'All'),
        ('B08126_003E', 'Construction', 'All'),
        ('B08126_004E', 'Manufacturing', 'All'),
        ('B08126_005E', 'Wholesale trade', 'All'),
        ('B08126_006E', 'Retail trade', 'All'),
        ('B08126_007E', 'Transportation and warehousing, and utilities', 'All'),
        ('B08126_008E', 'Information', 'All'),
        ('B08126_009E', 'Finance and insurance, and real estate and rental and leasing', 'All'),
        ('B08126_010E', 'Professional, scientific, and management, and administrative and waste management services', 'All'),
        ('B08126_011E', 'Educational services, and health care and social assistance', 'All'),
        ('B08126_012E', 'Arts, entertainment, and recreation, and accommodation and food services', 'All'),
        ('B08126_013E', 'Other services (except public administration)', 'All'),
        ('B08126_014E', 'Public administration', 'All'),
        ('B08126_015E', 'Armed forces', 'All'),
    ]

    food_stamps = [
        ('B22001_001E', 'Total:', 'All'),
        ('B22001_002E', 'Household received Food Stamps/SNAP in the past 12 months:', 'All'),
        ('B22001_003E', 'At least one person in household 60 years or over', 'All'),
        ('B22001_004E', 'No people in household 60 years or over', 'All'),
        ('B22001_005E', 'Household did not receive Food Stamps/SNAP in the past 12 months', 'All'),
        ('B22001_006E', 'At least one person in household 60 years or over', 'All'),
        ('B22001_007E', 'No people in household 60 years or over', 'All'),
    ]

    less_high_school_edu_by_emp = [
        ('B23006_003E', 'Less than high school', 'In labor force'),
        ('B23006_004E', 'Less than high school', 'In Armed Forces'),
        ('B23006_005E', 'Less than high school', 'Civilian'),
        ('B23006_006E', 'Less than high school', 'Employed'),
        ('B23006_007E', 'Less than high school', 'Unemployed'),
        ('B23006_008E', 'Less than high school', 'Not in labor force'),
    ]

    high_school = [
        ('B23006_010E', 'Finished high school', 'In labor force:'),
        ('B23006_011E', 'Finished high school', 'In Armed Forces'),
        ('B23006_012E', 'Finished high school', 'Civilian'),
        ('B23006_013E', 'Finished high school', 'Employed'),
        ('B23006_014E', 'Finished high school', 'Unemployed'),
        ('B23006_015E', 'Finished high school', 'Not in labor force'),
    ]

    college_degree = [
        ('B23006_017E', 'Some college or associates degree', 'In labor force'),
        ('B23006_018E', 'Some college or associates degree', 'In Armed Forces'),
        ('B23006_019E', 'Some college or associates degree', 'Civilian'),
        ('B23006_020E', 'Some college or associates degree', 'Employed'),
        ('B23006_021E', 'Some college or associates degree', 'Unemployed'),
        ('B23006_022E', 'Some college or associates degree', 'Not in labor force'),
    ]

    bach_or_more = [
        ('B23006_024E', 'Bach or higher', 'In labor force:'),
        ('B23006_025E', 'Bach or higher', 'In Armed Forces'),
        ('B23006_026E', 'Bach or higher', 'Civilian:'),
        ('B23006_027E', 'Bach or higher', 'Employed'),
        ('B23006_028E', 'Bach or higher', 'Unemployed'),
        ('B23006_029E', 'Bach or higher', 'Not in labor force'),
    ]

    #TODO: Remove token and make it an arg
    c = Census(sys.argv[1], year=sys.argv[2])

    results = []
    query_census(key_pop_sum, c, results)
    query_census(work_industry, c, results)
    query_census(bach_or_more, c, results)
    query_census(less_high_school_edu_by_emp, c, results)
    query_census(high_school, c, results)
    query_census(college_degree, c, results)
    query_census(income, c, results)
    query_census(education, c, results)

    write_csv('CENSUS_DG_%s.csv' % sys.argv[2], results)


if __name__ == '__main__':
    main()
