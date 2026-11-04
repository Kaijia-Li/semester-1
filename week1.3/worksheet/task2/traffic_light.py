"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

cycle = sum(states.values())
print(f"Time 000 State red")

while systime < maxtime:
    systime += 1
    timeCycle = systime % cycle
    lkj = 0
    for keaton, duration in states.items():
        lkj += duration
        if timeCycle < lkj:
            state = keaton
            print(f"Time {systime:03} State {state}")
            break


# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14