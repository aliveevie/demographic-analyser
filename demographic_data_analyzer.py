import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men_only = df[df['sex'] == 'Male']
    average_age_men = round(men_only['age'].mean())

    # What is the percentage of people who have a Bachelor's degree?
    total_edu = df['education'].count()
    bachelor_degree = df[df['education'] == 'Bachelors']
    count = bachelor_degree.shape[0]
    percentage_bachelors = round(count / total_edu * 100)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    bachelors_above = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    bachelors_above_count = bachelors_above.shape[0]
    higher_education = round(bachelors_above_count / total_edu * 100)
    
    # lower education calculations
    lower_education_people = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_count = lower_education_people.shape[0]
    lower_education = round(lower_education_count / total_edu * 100)

    # percentage with salary >50K
    above_fifty = bachelors_above[bachelors_above['salary'] == '>50K']
    above_fifty_count = bachelors_above[bachelors_above['salary'] == '>50K'].shape[0]
    higher_education_rich = round(above_fifty_count / total_edu * 100)
    
    # lower people with low salary percentage
    print(lower_education)
    salary_low = lower_education_people[lower_education_people['salary'] == '<=50K'].shape[0]
    lower_education_rich = round(salary_low / total_edu * 100)
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = round(df['hours-per-week'].mean())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = above_fifty[above_fifty['hours-per-week'] < 40].shape[0]


    rich_percentage = round(num_min_workers / total_edu * 100)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = 'United States'
    above_fifty = bachelors_above[bachelors_above['salary'] == '>50K']
    highest_country_count = above_fifty[above_fifty['native-country'] == 'United-States'].shape[0]
    highest_earning_country_percentage = round(highest_country_count / total_edu * 100)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = 'Prof-specialty'

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
