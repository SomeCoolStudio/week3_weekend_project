
class FourSquareMethod:


    def rental_income(self):

        return input ("\nWhat is your total monthy rental income? Usually this means adding up funds you get from rent" \
                " but can also include other misc income such as money from laundry machines, storage sheds, etc...\n" \
                "$ ")
    

    def expenses(self):

        return input ("\nWhat are your monthly expenses? Common expenses usually include property taxes, HOA fees, lawn care," \
               " vacancy savings, capital expenditures, property management cost, mortgage etc...\n" \
                "$ ")


    def cash_flow(self, income, expenses):

        return (int(income) - int(expenses)) * 12


    def total_investment(self):
        return input ("\nFinally, lets look at total investment costs. In other words lets total up your down payment," \
                " closing cost, appraisal cost, cost for repairs, etc...\n" \
                "$ ")


    def run_four_square_method(self):

        annual_cash_flow = self.cash_flow(self.rental_income(), self.expenses())

        return print (f"\nBased on your annual cash flow of ${annual_cash_flow}, your cash on cash ROI is: {(annual_cash_flow / int(self.total_investment())) * 100}%")


rental_property = FourSquareMethod()

rental_property.run_four_square_method()