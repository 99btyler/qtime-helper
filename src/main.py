

def ask(question, requires_number=False):
	answer = input(f"{question}: ")
	while requires_number and not answer.isdigit():
		answer = input(f"{question}: ") # asking again
	return int(answer) if requires_number else answer


print("\n---- qtime-helper ----\n")

column_name = ask("column_name")
row_first = ask("\nrow_first", True)
row_last = ask("row_last", True)
goods = ask("\ngoods(separated by comma)")

string_all = ""
for i in range(row_first, row_last+1):
	string_all += f"{column_name}{i}+"
print(f"\n{string_all[:-1]}")

string_goods = ""
for good in [good.strip() for good in goods.split(",")]:
	string_goods += f"{column_name}{good}+"
print(f"{string_goods[:-1]}")

print("\n----------------------\n")

