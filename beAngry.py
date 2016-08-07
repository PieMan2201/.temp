import random
number = random.randint(3,12)
marks = [".", ",", "?", "!", ";", ":"
    ]

marks_string ="."
marks_string = str("")

for x in range(0,number
):
    marks_string = marks_string + random.choice ( marks)
print    marks_string
