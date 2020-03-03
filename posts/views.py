from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import PostModel

def post_list(request):
	queryset=PostModel.objects.all
	context={
		"object_list": queryset,
		"title": "List"
	}
	return render(request,"post_list.html",context)

def post_detail(request,id=None):
	instance=get_object_or_404(PostModel,id=id)
	context={
		"title":instance.casenumber,
		"instance": instance
	}
	return render(request,"post_detail.html",context)

def post_create(request):
	form=PostForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request, '建立成功')
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
		"form": form,
	}
	return render(request,"post_form.html",context)


def post_update(request,id=None):
	instance=get_object_or_404(PostModel,id=id)
	form=PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request, '更新成功')
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
		"title": instance.casenumber,
		"form": form,
		"instance":instance
	}
	return render(request,"post_form.html",context)

def post_delete(request,id=None):
	instance=get_object_or_404(PostModel,id=id)
	instance.delete()
	messages.success(request, '刪除成功')
	return redirect("posts:list")