from datetime import date

##13.1 Write the current date as a string to the text file today.txt ##
today = date.today()
today_string = today.strftime("%Y-%m-%d")

with open("today.txt", "w") as file:
    file.write(today_string)
    
##13.2 read file
with open("today.txt", "r") as file:
    today_string = file.read().strip()

## this is optional to me, I wanted to see what it printed   
print(f"File created successfully {today_string}")

##BUG REPORT first run, I forgot to do my imports
## 2nd run I misspelled  on of my strings and it gave me an error that is not define.
