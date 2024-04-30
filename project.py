print(
    """Welcome to Employee Salary Portal.
     Here will show you how much salary you owe to the Company.
      Please provide some info to calculate your salary."""
)

# taking name input from user. And converting hourly rate to float data type

your_name = input("\nWhat is your Name? ")
hourly_wage_rate = float(input("what is your Hourly Wage Rate? "))
hours_worked_this_week = int(input("Hours hours_worked_this_week? "))

# checking first condition:

if hours_worked_this_week > 40:
    wage_without_ot = hourly_wage_rate * 40
    ot = (hourly_wage_rate * 1.10) * (hours_worked_this_week - 40)
    total_wage = wage_without_ot + ot
    print(f"{your_name}! Your Total Wgae is {total_wage}. Gross Wage is {wage_without_ot} and Overtime is {ot}.")

# checking secondt condition:

elif hours_worked_this_week == 40:
    print(f"{your_name}! Your total wage is {hourly_wage_rate * hours_worked_this_week}.")

# writing default condition:

else:
    print(f"{your_name}! You didn't work this Week.")
