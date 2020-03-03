from django import forms
from .models import PostModel,BuildModel

class PostForm(forms.ModelForm):
	class Meta:
		model=PostModel
		fields=[
			"casenumber",
			"address",
			"auctionday",
			"auctionlevel",
			"floorprice",
			"margin",
			"creditor",
			"debtor"
		]

class BuildForm(forms.ModelForm):
	class Meta:
		model=BuildModel
		fields=[
			"postmodel",
			"buildnumber",
			"buildarea",
			"buildurl",
			"buildholdingpointperson",
			"buildholdingpointall",
			"buildtype",
			"usearea"
		]
