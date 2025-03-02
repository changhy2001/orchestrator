# Option 1
## 설치 단계

1. **GitHub에서 리포지토리 복제**
   ```bash
   git clone https://github.com/changhy2001/django.git
   cd django
   ```

2. **가상환경 생성 및 활성화**
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   # Windows의 경우: venv\Scripts\activate
   ```

3. **필요한 패키지 설치**
   ```bash
   pip install -r requirements.txt
   ```
---

## 실행 준비

1. **Working directory 들어가기**
   ```bash
   cd myproject
   ```

2. **.env 파일 생성**
   ```bash
   # 아래 템플렛을 바탕으로 생성
   DEBUG=True
   SECRET_KEY=''

   DATABASE_URL=
   ```
---

## 실행 방법 (Daphne와 Nginx 사용)
   
1. **Daphne (ASGI 서버) 실행**
   ```bash
   daphne myproject.asgi:application --port 8000
   ```

2. **Nginx 설정 및 실행**
   ```bash
   brew services start nginx
   ```
   
3. **브라우저 접속**
   ```bash
   http://127.0.0.1/
   ```
---
# Option 2: Docker Image
## 실행 방법
   
1. **도커 이미지 로드**
   ```bash
   docker load -i django-image.tar
   ```

2. **컨테이너 실행**
   ```bash
   docker run -p 8000:8000 my_django_app
   ```
   
---
# Option 3: Docker Compose file
## 실행 방법
   
1. **Docker Compose로 컨테이너 빌드 및 실행**
   ```bash
   docker-compose up --build
   ```

2. **컨테이너 실행**
   ```bash
   http://localhost:8000
   ```
   
