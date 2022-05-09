import datetime

#this line sets the current time in a pretty format for printing
x = datetime.datetime.now()
date = (x.strftime("%x"))

#input the chapter number you want displayed
chapter = "3"

#input the range for the number of labs that you have this example does 1-10
Lab = range(1,11)

#update this with your name (:
name = "first last"


for i in Lab:
    try:
        #Update the line with the path of where you want to files to be created ex. C:\\Documents\\python
        with open(f'PATH_TO_CREATE_FILES\\Lab_{chapter}-{i}.py', 'x') as f:
            f.write('"""\n')
            f.write(f'Lab_{chapter}-{i}\n')
            f.write(f"{name}\n")
            f.write(f"{date}\n")
            f.write('"""')
    #this skips creating the file if it exists to avoid overwriting files
    except FileExistsError:
        print(f'Lab_{chapter}-{i} already exists, skipping')