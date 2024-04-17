def calculate_income(rental_income, laundry_income, storage_income, misc_income):
    return rental_income + laundry_income + storage_income + misc_income

def calculate_expenses(taxes, insurance, water_sewer, garbage, electricity, gas, hoa_fees, lawn_snow, vacancy, repairs, capex, prop_management, mortgage):
    return taxes + insurance + water_sewer + garbage + electricity + gas + hoa_fees + lawn_snow + vacancy + repairs + capex + prop_management + mortgage

def calculate_cash_flow(total_income, total_expenses):
    return total_income - total_expenses

def calculate_annual_cash_flow(total_cash_flow):
    return total_cash_flow * 12

def calculate_cash_on_cash_return(down_payment, closing_costs, rehab_budget, misc_other):
    return down_payment + closing_costs + rehab_budget + misc_other

def calculate_cash_on_cash_percentage(annual_cash_flow, total_investment):
    return (annual_cash_flow / total_investment) * 100

# Inputs
rental_income = float(input("Enter Rental Income: "))
laundry_income = float(input("Enter Laundry Income: "))
storage_income = float(input("Enter Storage Income: "))
misc_income = float(input("Enter Misc Income: "))

taxes = float(input("Enter Taxes: "))
insurance = float(input("Enter Insurance: "))
water_sewer = float(input("Enter Water/Sewer: "))
garbage = float(input("Enter Garbage: "))
electricity = float(input("Enter Electricity: "))
gas = float(input("Enter Gas: "))
hoa_fees = float(input("Enter HOA Fees: "))
lawn_snow = float(input("Enter Lawn/Snow: "))
vacancy = float(input("Enter Vacancy: "))
repairs = float(input("Enter Repairs: "))
capex = float(input("Enter CapEx: "))
prop_management = float(input("Enter Prop. Management: "))
mortgage = float(input("Enter Mortgage: "))

down_payment = float(input("Enter Down Payment: "))
closing_costs = float(input("Enter Closing Costs: "))
rehab_budget = float(input("Enter Rehab Budget: "))
misc_other = float(input("Enter Misc Other: "))

# Calculations
total_income = calculate_income(rental_income, laundry_income, storage_income, misc_income)
total_expenses = calculate_expenses(taxes, insurance, water_sewer, garbage, electricity, gas, hoa_fees, lawn_snow, vacancy, repairs, capex, prop_management, mortgage)
total_cash_flow = calculate_cash_flow(total_income, total_expenses)
annual_cash_flow = calculate_annual_cash_flow(total_cash_flow)
total_investment = calculate_cash_on_cash_return(down_payment, closing_costs, rehab_budget, misc_other)
cash_on_cash_return = calculate_cash_on_cash_percentage(annual_cash_flow, total_investment)

# Results
print("Total Monthly Income:", total_income)
print("Total Monthly Expenses:", total_expenses)
print("Total Annual Cash Flow:", annual_cash_flow)
print("Cash on Cash Return (%):", cash_on_cash_return)

