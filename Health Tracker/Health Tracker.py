Name = input("Enter Your Name: ")
Gender = input("Enter Sex: ")
Age = int(input("Enter Age: "))
Height = float(input("Enter your Height in centimeter: "))
Weight = float(input("Enter your Weight in Kgs: "))
print("\nPlease Enter Workout details Below\n")
Days = []
Steps = []
hours = []
minuts = []
secs = []
Workout_days = int(input("Enter Total number of workout days : "))
for i in range(Workout_days):
    Days.append(int(input("Enter day: ")))
    Steps.append(int(input("Enter steps: ")))
    Total_time = input("Enter the time in HH:MM:SS : ").split()
    for time in Total_time:
        hour, minit, sec = [int(i) for i in time.split(":")]
        hours.append(int(hour))
        minuts.append(int(minit))
        secs.append(int(sec))

Ht = (Height/100)
Bmi = (Weight/(Ht**2))
count = 0
Distance = []

for i in range(len(Steps)):
    dist = (Steps[i] * 0.8) / 1000
    Distance.append(dist)
    if Steps[i] != 0:
        count = count + 1

hrsecs = []
mnsecs = []
Step_time = []
Speed = []

for i in range(len(hours)):
    hr = hours[i]*3600
    hrsecs.append(int(hr))
    m = minuts[i]*60
    mnsecs.append(int(m))

for i in range(len(hrsecs)):
    Step_time.append(float((hrsecs[i]+mnsecs[i]+secs[i])/3600))
    Speed.append(float(Distance[i]/Step_time[i]))

max_speed = max(Speed)
long_dist = max(Distance)
Speed.sort()
min_speed = Speed[0]
Distance.sort()
short_dist = Distance[0]
avg_speed = (sum(Speed)/len(Speed))
avg_dist = (sum(Distance)/len(Distance))

print("Hi ", Name)
print("Your BMI is: ", Bmi)
print("\nYour Weekly Achievement is as follows:\n ")
print("***** You got {}/{} award *****".format(count, Workout_days))
print("Your Fastest Speed is: ", max_speed)
print("Your Longest Distance is: ", long_dist)
print("Your Slowest Speed is: ", min_speed)
print("Your Shortest Distance is:", short_dist)
print("Your Weekly Average Speed is:", avg_speed)
print("Your Weekly Average Distance is: ", avg_dist)
