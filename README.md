# note for heroku deploy session 

## 01 필요한 모듈 설치  
```
$pip install django-corse-headers gunicorn psycopg2-binary whitenoise dj-database-url
```

django-corse-headers : corse 에러 방지
gunicorn: 배포를 위한 도구
psycopg2-binary, dj-database-url: heroku 에서 사용하는 db인, postgresql 을 사용하기 위한 도구 
whitenoise: 정적 파일의 사용을 돕는 미들웨어

  
```
$pip freeze > requirements.txt
```

## 02 settings.py 수정  
project의 settings.py 에서..  

-import os 아래에 추가하는 줄:  
```python
import dj-database-url  
```
-SECRET_KEY 다음과 같이 수정:  
```python
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','l-gh@-o9%(x+cb=n)j-vy*w+ovd+@=p=$a^5v(-u5vgsp(96c%')  
```

-DEBUG 다음과 같이 수정:  
```python
DEBUG = False  
```

-MIDDLEWARE에 whitenoise 추가: 
```python
'whitenoise.middleware.WhiteNoiseMiddleware'  
```

-DATABASE 아래쪽에 다음의 줄 추가:  
```python
db_from_env = dj_database_url.config(conn_max_age=500)   
DATABASES['default'].update(db_from_env)  
```

## 03 필요한 파일 생성 (mandatory requirements from Heroku)  
**파일을 생성하는 위치에 주의해주세요!!**  

-Procfile 생성  
위치: manage.py 가 있는 곳 !  
```
$ touch Procfile  
  

#파일 지우고 싶을 때에는 $ rm Procfile  
```

-Procfile에 다음과 같은 줄 추가  
```python
#Procfile
web: gunicorn 프로젝트이름.wsgi  
  
# 예) web: gunicorn myproject.wsgi  
```

-runtime.txt 생성  
위치: manage.py 가 있는 곳 !  
```
$touch runtime.txt  
```

-runtime.txt에 파이썬 버전 입력.  
```
#파이썬 버전 확인하기
$python --version  

#제 파이썬 버전은 3.7.7 로 확인되었습니다! 
```

-버전 확인후에 runtime.txt 파일에 다음의 줄 추가  
```python
#runtime.txt  
python-3.7.7  
```
-.gitignore 파일 만들기  
>> Heroku는 git을 통해 배포가 됩니다! 이 때 저희의 모든 코드를 배포해버릴 필요는 없겠죠?! 배포에 포함을 시키지 않을 파일들을 .gitignore 파일을 통해 기록합니다! 
  
위치: manage.py 가 있는 곳 !  

#파일 생성  
```
$touch .gitignore   
```
  

```python
#.gitignore 
*.py[cod]

.Python
myvenv/

__pycache__/ 
.DS_Store

db.sqlite3

.vscode/
```

## 04 헤로쿠 가입 및 CLI 설치  
1. 헤로쿠에 가입을 해주세요  
2. Heroku 사용을 위해서 CLI(Command Line Interface)를 설치해주세요!  
설치 페이지: <https://devcenter.heroku.com/articles/heroku-cli>  
  
## 05 git 폴더로 만들고, push 하기  
>> 앞에서도 언급했듯이, heroku는 git 을 통해 배포가 됩니다!  
>> 따라서, Heroku 에 무언가를 올리기 위해서는 **무조건 git 저장소**를 폴더에 만들어 줘야겠죠?  

```
$git init  
$git add .
$git commit -m "first commit for deploy"  
$git remote add origin 레포주소 
$git push origin master  

```
**배포 준비 완료!!**  
  
## 06 Heroku로 배포하기 
```
$heroku login  
$heroku create 웹사이트이름 
(그냥 랜덤으로 사이트 이름을 만들어줍니당.)  
```
  
**두근두근 배포배포** 
```
$git push heroku master 
``` 

## 06 배포된 사이트 migration 해주기  
>> 배포가 끝이 아니랍니다! 저희의 파일들을 완전히 'attach' 시켜주기 위해서, migrate를 해줍니다!  
>> 또한, 배포를 하면서 db가 초기화 되었기 때문에, superuser도 만들어 주어야 합니다.  
```
$heroku run python manage.py migrate  
```  

```
$heroku run python manage.py createsuperuser
```

모두 되었다면, 잘 배포가 되었는지 확인해볼까요?  
```
$heroku open
```


