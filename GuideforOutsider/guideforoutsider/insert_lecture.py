import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guideforoutsider.settings")
import django
django.setup()
from community.models import *
import csv

if __name__=='__main__':
    with open('lecture_data/timetable.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        data=list(csv.reader(csvDataFile))

        for i in range(1, len(data)):
            Lecture(university=data[i][0], department=data[i][1], grade=data[i][2], completion_division=data[i][3], lecture_number=data[i][4], 
                    lecture_name=data[i][5], credit=data[i][6], professor_name=data[i][7], time_table=data[i][9]).save()