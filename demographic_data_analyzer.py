import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(),1)
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    percentage_higher_ed = round((higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 1)
    percentage_lower_ed = round((lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1)

    min_work_hours = df['hours-per-week'].min()
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    rich_min_workers = len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])
    percentage_rich_min_workers = round(rich_min_workers / num_min_workers * 100, 1)

    country_salary = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean()).sort_values(ascending=False)
    highest_earning_country = country_salary.index[0]
    highest_earning_country_percentage = round(country_salary.iloc[0] * 100, 1)

    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().index[0]


    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {percentage_higher_ed}%")
        print(f"Percentage without higher education that earn >50K: {percentage_lower_ed}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich people with minimum hours: {percentage_rich_min_workers}%")
        print(f"Country with highest percentage of rich people: {highest_earning_country} with {highest_earning_country_percentage}%")
        print(f"Top occupations in India for those who earn >50K: {top_IN_occupation}")

        # Racial Group Statistics (Added this section)
        print("\n--- Racial Group Statistics ---")
        for race in df['race'].unique():
            race_df = df[df['race'] == race]
            avg_age = round(race_df['age'].mean())
            high_ed_pct = round((race_df[race_df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'] == '>50K').sum() / len(race_df) * 100, 1)
            rich_pct = round((race_df['salary'] == '>50K').sum() / len(race_df) * 100, 1)
            print(f"\n{race}:")
            print(f"  - Average Age: {avg_age}")
            print(f"  - % with Higher Education: {high_ed_pct}%")
            print(f"  - % Earning >50K: {rich_pct}%")


    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': percentage_higher_ed,
        'lower_education_rich': percentage_lower_ed,
        'min_work_hours': min_work_hours,
        'rich_percentage': percentage_rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }