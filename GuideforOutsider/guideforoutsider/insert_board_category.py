import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guideforoutsider.settings")
import django
django.setup()
from community.models import *

if __name__=='__main__':
    Board_Category(board_category="스터디").save()
    Board_Category(board_category="팀플").save()
    Board_Category(board_category="강의 후기").save()