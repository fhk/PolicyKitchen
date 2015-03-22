import sys

from census import Census
from us import states


def main():
    """
    """
    #TODO: Remove token and make it an arg
    c = Census("inserttoken")


    key_pop_sum = {
        'B02001_001E': 'Total Population', 
        'B02001_002E': 'White',
        'B02001_003E': 'Black or African American alone',
        'B02001_004E': 'American Indian and Alaska Native alone',
        'B02001_005E': 'Asian',
        'B02001_006E': 'Hawaiian and Other Pacific Islander',
        'B02001_007E': 'Other race',
        'B02001_008E': 'Two or more races:',
    }

    key_med_age_by_pop = {
        'B01002_001E': 'Total Pop. Median age, male and female',
        'B01002_002E': 'Total Pop. Median age, male',
        'B01002_003E': 'Median age, female',
        'B01002A_001E': 'White Median age, male and female',
        'B01002A_002E': 'White Median age, male',
        'B01002A_003E': 'White Median age, female',
        'B01002B_001E': 'Black/African Amer. Median age, male and female',
        'B01002B_002E': 'Median age, male',
        'B01002B_003E': 'Median age, female',
        'B01002C_001E': 'A. Indidan/Alaska Median age, male and female',
        'B01002C_002E': 'A. Indidan/Alaska Median age, male',
        'B01002C_003E': 'A. Indidan/Alaska Median age, female',
        'B01002D_001E': 'Asian Median age, male and female',
        'B01002D_002E': 'Asian Median age, male',
        'B01002D_003E': 'Asian Median age, female',
        'B01002E_001E': 'Hawaiian/Pac. Islander Median age, male and female',
        'B01002E_002E': 'Hawaiian/Pac. Islander Median age, male',
        'B01002E_003E': 'Hawaiian/Pac. Islander Median age, female',
        'B01002F_001E': 'Other Median age, male and female',
        'B01002F_002E': 'Other Median age, male',
        'B01002F_003E': 'Other Median age, female',
        'B01002G_001E': 'Two or More Median age, male and female',
        'B01002G_002E': 'Two or More Median age, male',
        'B01002G_003E': 'Two or More Median age, female',
    }

    education = {
        'B06009_002E': 'Less than high school graduate',
        'B06009_003E': 'High school graduate (includes equivalency)',
        'B06009_004E': 'Some college or associates degree',
        'B06009_005E': 'Bachelors degree',
        'B06009_006E': 'Graduate or professional degree',

    }

    income = {
        'B06010_002E': 'No income',
        'B06010_003E': 'With income:',
        'B06010_004E': '$1 to $9,999 or loss',
        'B06010_005E': '$10,000 to $14,999',
        'B06010_006E': '$15,000 to $24,999',
        'B06010_007E': '$25,000 to $34,999',
        'B06010_008E': '$35,000 to $49,999',
        'B06010_009E': '$50,000 to $64,999',
        'B06010_010E': '$65,000 to $74,999',
        'B06010_011E': '$75,000 or more',
    }

    transportation_to_work = {
        'B08006_002E': 'Car, truck, or van:',
        'B08006_003E': 'Drove alone',
        'B08006_004E': 'Carpooled:',
        'B08006_005E': 'In 2-person carpool',
        'B08006_006E': 'In 3-person carpool',
        'B08006_007E': 'In 4-or-more-person carpool',
        'B08006_008E': 'Public transportation (excluding taxicab):',
        'B08006_009E': 'Bus or trolley bus',
        'B08006_010E': 'Streetcar or trolley car (carro publico in Puerto Rico)',
        'B08006_011E': 'Subway or elevated',
        'B08006_012E': 'Railroad',
        'B08006_013E': 'Ferryboat',
        'B08006_014E': 'Bicycle',
        'B08006_015E': 'Walked',
        'B08006_016E': 'Taxicab, motorcycle, or other means',
        'B08006_017E': 'Worked at home',
    }

    work_industry = {
        'B08126_002E': 'Agriculture, forestry, fishing and hunting, and mining',
        'B08126_003E': 'Construction',
        'B08126_004E': 'Manufacturing',
        'B08126_005E': 'Wholesale trade',
        'B08126_006E': 'Retail trade',
        'B08126_007E': 'Transportation and warehousing, and utilities',
        'B08126_008E': 'Information',
        'B08126_009E': 'Finance and insurance, and real estate and rental and leasing',
        'B08126_010E': 'Professional, scientific, and management, and administrative and waste management services',
        'B08126_011E': 'Educational services, and health care and social assistance',
        'B08126_012E': 'Arts, entertainment, and recreation, and accommodation and food services',
        'B08126_013E': 'Other services (except public administration)',
        'B08126_014E': 'Public administration',
        'B08126_015E': 'Armed forces',
    }

    food_stamps = {
        'B22001_001E': 'Total:',
        'B22001_002E': 'Household received Food Stamps/SNAP in the past 12 months:',
        'B22001_003E': 'At least one person in household 60 years or over',
        'B22001_004E': 'No people in household 60 years or over',
        'B22001_005E': 'Household did not receive Food Stamps/SNAP in the past 12 months',
        'B22001_006E': 'At least one person in household 60 years or over',
        'B22001_007E': 'No people in household 60 years or over',
    }

    less_high_school_edu_by_emp = {
        'B23006_002E': 'Less than high school graduate:',
        'B23006_003E': 'In labor force:',
        'B23006_004E': 'In Armed Forces',
        'B23006_005E': 'Civilian:',
        'B23006_006E': 'Employed',
        'B23006_007E': 'Unemployed',
        'B23006_008E': 'Not in labor force',
    }

    high_scholl = {
        'B23006_010E': 'In labor force:',
        'B23006_011E': 'In Armed Forces',
        'B23006_012E': 'Civilian:',
        'B23006_013E': 'Employed',
        'B23006_014E': 'Unemployed',
        'B23006_015E': 'Not in labor force',
    }

    college_degree = {
        'B23006_016E': 'Some college or associates degree:',
        'B23006_017E': 'In labor force:',
        'B23006_018E': 'In Armed Forces',
        'B23006_019E': 'Civilian:',
        'B23006_020E': 'Employed',
        'B23006_021E': 'Unemployed',
        'B23006_022E': 'Not in labor force',
    }

    bach_or_more = {
        'B23006_023E': 'Bachelors degree or higher:',
        'B23006_024E': 'In labor force:',
        'B23006_025E': 'In Armed Forces',
        'B23006_026E': 'Civilian:',
        'B23006_027E': 'Employed',
        'B23006_028E': 'Unemployed',
        'B23006_029E': 'Not in labor force',
    }

    for k, v in edu_by_emp.items():
        for i in range(1, 2):
            data = c.acs5.state_district(
                ('NAME', k),
                states.CA.fips,
                str(i).zfill(2)
            )

            print data
            print data[0][k]


if __name__ == '__main__':
    main()
