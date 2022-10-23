from django.db import models


class MyBoard(models.Model):
    myname = models.CharField(max_length = 100)
    mytitle = models.CharField(max_length = 500)
    mycontent = models.CharField(max_length = 2000)
    mydate = models.DateField()

    # 원하는 문자열의 형태로 보여주기.
    # java 에서 toString과 비슷하다.
    def __str__(self):
        return str({"myname" : self.myname, "mytitle" : self.mytitle, "mycontent" : self.mycontent, "mydate" : self.mydate})



class MyMember(models.Model):
    myname = models.CharField(max_length = 100)
    mypassword = models.CharField(max_length = 100)
    myemail = models.CharField(max_length=100)

    def __str__(self):
        return str({"myname" : self.myname, "mypassword" : self.mypassword, "myemail" : self.myemail})
