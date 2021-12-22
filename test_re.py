import re
regexp_cpu='(Core|Ryzen).* (i\d-\d{3,5}.?|\d \d{3,5}.?)'
cpu='Sempron 3500+'
result=re.search(regexp_cpu, cpu)
if result is not None:
    print(result.group(1)+' '+result.group(2))
else:
    print('ops')
    