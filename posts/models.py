from datetime import date
from django.db import models
from django.urls import reverse


class PostModel(models.Model):
	AUCTIONLEVEL_LIST=(
		('第一拍','第一拍'),
		('第二拍','第二拍'),
		('第三拍','第三拍'),
		('第四拍','第四拍'),		
	)
	casenumber=models.CharField(u'案號',max_length=100)
	address=models.CharField(u'住址',max_length=100)
	auctionday=models.DateField(u'拍賣日',default=date.today)
	auctionlevel=models.CharField(u'拍賣次數',choices=AUCTIONLEVEL_LIST,max_length=5)
	floorprice=models.IntegerField(u'底價')
	margin=models.IntegerField(u'保証金')
	creditor=models.CharField(u'債務人',max_length=100)
	debtor=models.CharField(u'債權人',max_length=100)

	def __str__(self):
		return self.casenumber

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"id": self.id})

	def get_ping(self):
		return self.floorprice * self.margin


class BuildModel(models.Model):
	CLASS_LIST=(
		('1公寓(5樓含以下無電梯)','1公寓(5樓含以下無電梯)'),
		('2透天厝','2透天厝'),
		('3店面(店舖)','3店面(店舖)'),
		('4辦公商業大樓','4辦公商業大樓'),
		('5住宅大樓(11層含以上有電梯)','5住宅大樓(11層含以上有電梯)'),
		('6華廈(10層含以下有電梯)','6華廈(10層含以下有電梯)'),
		('7套房(1房(1廳)1衛)','7套房(1房(1廳)1衛)'),
		('8工廠','8工廠'),
		('9廠辦','9廠辦'),
		('10農舍','10農舍'),
		('11倉庫','11倉庫'),
		('Z其他等型態','Z其他等型態'),
	)	

	AREA_LIST=(
		('第一種住宅區','第一種住宅區'),
		('第二種住宅區','第二種住宅區'),
		('第三種住宅區','第三種住宅區'),
		('第四種住宅區','第四種住宅區'),
		('第一種商業區','第一種商業區'),
		('第二種商業區','第二種商業區'),
		('第三種商業區','第三種商業區'),
		('第四種商業區','第四種商業區'),
		('第二種工業區','第二種工業區'),
	)

	postmodel=models.ForeignKey(PostModel,on_delete=models.CASCADE)
	buildnumber=models.CharField(max_length=100,blank=True,null=True)
	buildarea=models.DecimalField(max_digits=6, decimal_places=2)
	buildurl=models.CharField(max_length=255,blank=True,null=True)
	buildholdingpointperson=models.PositiveIntegerField()
	buildholdingpointall=models.PositiveIntegerField()
	buildtype=models.CharField(max_length=50,choices=CLASS_LIST,blank=True,null=True)
	usearea=models.CharField(max_length=20,choices=AREA_LIST,blank=True,null=True)

	def __str__(self):
		return self.buildnumber

 

