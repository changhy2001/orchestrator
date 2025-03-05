## 프로젝트 구조

```plaintext
.
├── backend
│   ├── config
│   │   └── nginx
│   │       └── myproject.conf 
│   ├── myproject
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── asgi.py
│   ├── search                      # DB 검색 기능
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── api_views.py
│   ├── users                       # 유저 관리 (회원가입, 로그인, 로그아웃)
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── api_views.py
│   ├── .env.template
│   ├── Dockerfile
│   ├── manage.py
│   └── requirements.txt
│
└── frontend
    ├── public
    │   ├── favicon.ico
    │   └── index.html 
    ├── src
    │   ├── assets
    │   ├── components
    │   ├── router
    │   ├── store
    │   ├── views
    │   ├── App.vue
    │   └── main.js
    └── Dockerfile
```

---

## 설치 단계

1. **GitHub에서 리포지토리 복제**
   ```bash
   git clone https://github.com/changhy2001/django.git
   cd django
   ```

2. **환경변수 설정: .env.template 사용하여 .env 파일 생성**
   ```bash
   cp backend/.env.example backend/.env
   ```

3. **컨테이너 빌드 및 실행**
   ```bash
   docker-compose up --build
   ```

4. **애플리케이션 접근**
   ```bash
   http://localhost
   ```
---

## 서버 플로우차트 


```plaintext
         ┌──────────────────────────────────────────────┐
         │                  Client                      │
         │          (Browser: http://localhost)         │
         └──────────────────────────────────────────────┘
                                 │   
                HTTP 요청 (포트 80)│
                                 ▼
         ┌──────────────────────────────────────────────┐
         │                     Nginx                    │
         │           (http://localhost:80)              │
         │  - 정적 파일: /usr/share/nginx/html (Vue dist) │
         │  - API 프록시: /users/api/ 요청을 Django로 전달   │
         │       (proxy_pass http://django_web:8000)    │
         └──────────────────────────────────────────────┘
                               │
                               ▼
         ┌──────────────────────────────────────────────┐
         │                    Django                    │
         │        (http://django_web:8000 또는           │
         │        http://localhost:8000)                │
         │            - 백엔드 API 처리 및 비즈니스 로직       │
         └──────────────────────────────────────────────┘
                               │
              DB 연결 (DATABASE_URL 환경변수)
                               │
                               ▼
         ┌──────────────────────────────────────────────┐
         │                   Database                   │
         │       (Railway PostgreSQL:                   │
         │      mainline.proxy.rlwy.net:43252)          │
         │          - 데이터 저장 및 조회                    │
         └──────────────────────────────────────────────┘
```

### 설명

- **Client (브라우저)**  
  - 사용자가 웹 브라우저에서 `http://localhost` 주소로 접속합니다.

- **Nginx (Reverse Proxy & 정적 파일 서버)**  
  - 포트 80에서 요청을 받고, Vue 앱의 빌드 산출물(`dist` 폴더의 내용)을 서빙합니다.  
  - `/users/api/` 등의 API 요청은 `http://django_web:8000` (또는 로컬에서 노출된 `http://localhost:8000`)으로 프록시합니다.

- **Django (백엔드 서버)**  
  - API 요청을 처리하고, 비즈니스 로직을 수행합니다.  
  - `DATABASE_URL` 환경변수를 통해 Railway의 PostgreSQL 데이터베이스에 연결합니다.

- **Database (Railway PostgreSQL)**  
  - 실제 데이터 저장소로, 주소는 `mainline.proxy.rlwy.net:43252`입니다.

이와 같이 각 서버의 주소와 역할을 명시하면, 다른 개발자들도 해당 환경을 쉽게 이해하고 재현할 수 있습니다.
