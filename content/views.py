
from uuid import uuid4
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
import os
from instagram.settings import MEDIA_ROOT
from django.db.models import Q
from django.views.generic import ListView, TemplateView



""" home - home 화면 접근
    content - content 화면 접근
    UploadFeed - 게시글 업로드
    DeleteFeed - 게시글 삭제
    modify - 게시글 수정
    profile - 프로필페이지 접근
    """


# Create your views here.

def home(request): # home 화면
    if request.method == 'GET' :
        user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
        if user:
            feeds = Feed.objects.all().order_by('-created_at')
            return render(request, 'content/home.html', {'feeds': feeds})
        else:
            return redirect('/sign-in')


def content(request): # content 화면
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            feeds = Feed.objects.all().order_by('-created_at')
            return render(request, 'content/home.html', {'feeds': feeds})
        else:
            return redirect('/sign-in')


class UploadFeed(APIView): # 게시글 업로드
    def post(self, request):

        # 일단 파일 불러와
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')
        
        created_at = request.data.get('created_at')
        updated_at = request.data.get('updated_at')
        tags = request.data.get('tag','').split(',')
        
        feed_info=Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count=0, created_at=created_at, updated_at=updated_at)
        for tag in tags:
            tag = tag.strip()
            if tag !='':
                feed_info.tags.add(tag)
        

        return Response(status=200)
def search(request):
    q = request.POST.get('q', "")  # I am assuming space separator in URL like "random stuff"
    query = Q(user_id__icontains=q) | Q(content__icontains=q) | Q(tags__name__icontains=q)
    searched = Feed.objects.filter(query)
    return render(request, 'searched.html',{'searched':searched, 'q': q })



class TagCloudTV(TemplateView):
    template_name = 'taggit/tag_cloud_view.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html'
    model = Feed

    def get_queryset(self):
        return Feed.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context


def DeleteFeed(request, id): # 게시글 삭제
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/content')

def modify(request, id): # 게시글 수정
    if request.method == 'POST':
        feed = Feed.objects.get(id=id)
        feed.content = request.POST.get('content')
        feed.save()
        return redirect("/")

def profile(request): # 프로필 페이지 접금
    return render(request, 'content/profile.html')


def profile_edit_page(request): # 프로필 수정 페이지 접근
    return render(request, 'content/profile_edit.html')


def profile_edit_password(request): # 비밀번호 변경 페이지 접근
    if request.method == "GET":
        return render(request, 'content/profile_edit_password.html')