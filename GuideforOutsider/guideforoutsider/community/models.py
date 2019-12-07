from django.db import models
from django.contrib.auth.models import User

class Board_Category(models.Model):
    board_category = models.CharField(max_length=10, blank=True, default="")

    def __str__(self):
        return self.board_category

class Lecture(models.Model):
    university = models.CharField(max_length=30, blank=True, default="") # 대학
    department = models.CharField(max_length=30, blank=True, default="") # 개설학과
    grade = models.CharField(max_length=5, blank=True, default="") # 학년
    completion_division = models.CharField(max_length=10, blank=True, default="") # 이수구분
    lecture_number = models.CharField(max_length=10, blank=True, default="") # 과목번호-분반
    lecture_name = models.CharField(max_length=30, blank=True, default="") # 과목명
    credit = models.IntegerField(blank=True, null=True) # 학점
    professor_name = models.CharField(max_length=10, blank=True, default="") # 담당교수
    time_table = models.CharField(max_length=20, blank=True, default="") # 강의 시간

    year = models.IntegerField(default=2019) # 개설년도
    semester = models.IntegerField(default=2) # 개설학기
    note = models.CharField(max_length=10, blank=True, default="")
    star = models.IntegerField(default=0) # 강의 별점

    def __str__(self):
        return self.lecture_name

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board_category = models.ForeignKey(Board_Category, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, default="")
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    hits = models.IntegerField(default=0)
    good = models.IntegerField(default=0)
    anonymity = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return '[' + str(self.lecture) + '] ' + str(self.title)

    @property
    def created_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.created_at.astimezone(korean_timezone)


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    anonymity = models.BooleanField(default=False)
    good = models.IntegerField(default=0)
    re_reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.board) + '(' + str(self.user) + ')'

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    board = models.ForeignKey(Board, blank=True, on_delete=models.CASCADE)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sender) + ' -> ' + str(self.receiver)