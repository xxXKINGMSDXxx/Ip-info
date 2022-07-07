import requests
import pprint

print("'||' '||''|.  ' '||' '|.   '|' '||''''|  ..|''||   ")
print(" ||   ||   ||    ||   |'|   |   ||  .   .|'    ||  ")
print(" ||   ||...|'    ||   | '|. |   ||''|   ||      || ")
print(" ||   ||         ||   |   |||   ||      '|.     || ")
print(".||. .||.       .||. .|.   '|  .||.      ''|...|'  ")
print("\n")
print("MADE BY MSD")
print('\n')
print('\n')






ip = input("enter victim ip    : ")






url = f"https://ipapi.co/{ip}/json/"

re = requests.get(url)

pprint.pprint(re.json())