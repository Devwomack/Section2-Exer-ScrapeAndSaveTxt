from datetime import datetime

currentText = "this is my test string"

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d.%H-%M-%S")

print(dt_string)

f = open(dt_string + ".txt", "a")
f.write(currentText)
f.close()

# filename format YYYY-MM-DD.HH-MM-SS