# 팀 이름

싸지방

# 프로젝트 이름

짭스타그램 (Jjapstagram)

## 팀원 소개

박준석 https://github.com/devjunseok/Jjapstagram

노우석 [https://github.com/WooSeok-Nho/](https://github.com/WooSeok-Nho/Jjapstagram.git)

성창남 [https://github.com/SungChangNam](https://github.com/SungChangNam)

양기철 https://github.com/hanmariyang/clone_instagram

이태겸 [https://github.com/poro625](https://github.com/poro625)  

## 개발 역할 분담

- 프론트엔드
    - [ ]  home.html ( 홈페이지, 게시글 올라가고, 좋아요 기능, 댓글, modal(댓글), 저장 기능, 태그기능(해시태그, 사용자태그) ) - content
    - 양기철, 박준석
    - [ ]  sign-in.html (로그인페이지) - user
    - 이태겸
    - [ ]  signup.html (회원가입페이지) -user
    - 이태겸
    - [ ]  base.html (위에 navbar, 검색창, 글쓰기버튼, 홈버튼, 알림, 베이스 html) - templates
    - 노우석
    - [ ]  profile.html (프로필 페이지, 팔로우, 팔로워 수 count) - content
    - 박준석, 성창남
    - [ ]  profileedit.html (프로필 편집 페이지 - 로그인한 본인만 볼 수 있는 페이지) - content
    - 박준석, 성창남
- 백엔드
    - [x]  회원가입, 회원탈퇴 (email, 이름, 닉네임, 비밀번호)
    - 박준석
    - [x]  로그인, 구글 API 로그인하기
    - 박준석
    - [x]  로그아웃
    - 박준석
    - [x]  글삭제(본인의 글만)
    - 양기철
    - [x]  팔로우, 팔로워
    - 성창남
    - [x]  게시글올리기(사진포함) + 게시글 수정(본인의 글만)
    - 양기철
    - [x]  내 프로필 편집
    - 박준석
    - [x]  댓글(절반만 구현)
    - 이태겸
    - [x]  검색 (태그기능 삽입)
    - 노우석
- 백엔드 역할분담
    
    user - 회원가입 로그인 로그아웃 팔로우 팔로워, 알림 (박준석 성창남)
    
    1. 유저(UserModel)
    - ID (pk)
    - tel_number
    - email
    - name
    - password
    - profile_image
    - nickname
    - follow
    - follower
    1. 알림(AlertModel)
    - ID(pk)
    - TweetModel.Foreignkey
    - UserModel.Foreignkey
    
    post - 게시글 올리기, 삭제, 수정, 댓글, 대댓글, 좋아요 , 검색, 알림 (노우석, 이태겸, 양기철님)
    
    1. 게시글(TweetModel)
    - ID (pk)
    - usermodel.Foreignkey
    - content
    - tags
    - created_at
    - updated_at
    - like
    1. 댓글 (TweetComment)
    - ID (pk)
    - TweetModel.Foreignkey
    - UserModel.Foreignkey
    - comment
    - create_at
    - like
- 구현 못한 기능들
    - [ ]  다른 유저 프로필 볼 수 있게,
    - [ ]  대댓글
    - [ ]  신고
    - [ ]  알림
    - [x]  html 손보기
    - [x]  내 프로필 편집하기
    - [x]  home.html 게시글 모달 수정
    - [ ]  신고기능
    - [ ]  알림
    - [x]  게시글 수정 모달 수정
    - [ ]  좋아요
    - [ ]  댓글 출력

## 프로젝트 소개

인스타그램 클론코딩 입니다!

## 사용하는 기술

python (3.10.4)

Django

html

css

AJAX
sqlite

git

## 와이어프레임

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3b54f3c3-5b25-4cdb-8a06-ab595096963a/Untitled.png)

[https://www.figma.com/file/MFJqOD0rR4XhZFmudkHHLz/Untitled?node-id=0%3A1](https://www.figma.com/file/MFJqOD0rR4XhZFmudkHHLz/Untitled?node-id=0%3A1)

## API 구현

[프로젝트 API 설계하기](https://www.notion.so/118601a0974d44d79b32144aa5fc758d)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/211380ef-846e-4ea1-8729-a611f92b9543/Untitled.png)