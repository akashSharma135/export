from splitwise import Splitwise
import splitwise_export as spwe
from splitwise.expense import Expense

# sObj = Splitwise(consumer_key='p5yIEYhP4mRrMxbSubZhYJTn5z7Sll9VutWfLuBv', consumer_secret='czaJnmzccnTDNtbOnQiuCLJOg26Pri4k6v5BWJ6y')

# url, secret = sObj.getAuthorizeURL()

s = spwe.authorize()
expenses = s.getExpenses()
expense_id = expenses[1].getId()
expense = s.getExpense(expense_id)
print(expense)
# expenses = spwe.get_group_expenses(s)
# print(expenses)
print(expense.getFriendshipId())
# spwe.expenses_to_csv(expenses)