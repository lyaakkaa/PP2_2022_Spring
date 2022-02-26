from datetime import datetime
d1 = datetime.strptime(input(), '%Y-%m-%d')
d2 = datetime.strptime(input(), '%Y-%m-%d')
print((d2-d1).total_seconds())
