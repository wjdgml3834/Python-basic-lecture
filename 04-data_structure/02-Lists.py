from this import d


days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print(days_of_week[0])  # Mon

print(days_of_week.count("Thu"))  # 1

days_of_week.append('Sat')  # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

print(days_of_week)


days_of_week.reverse()

print(days_of_week)  # ['Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']

days_of_week.remove('Fri')

print(days_of_week)  # ['Sat', 'Thu', 'Wed', 'Tue', 'Mon']

days_of_week.clear()  # 리스트를 완전히 수정시켰다 === 변화하다 (mutate)

print(days_of_week)  # []
