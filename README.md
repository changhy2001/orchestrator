## 프로젝트 구조

```plaintext
.
├── docker-compose.yml
├── .env.template
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
│   ├── Dockerfile
│   ├── manage.py
│   └── requirements.txt
│
└── frontend
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

## 설치 방법

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
         │        (http://django_web:8000)              │
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
  - 사용자는 웹 브라우저에서 `http://localhost` 주소로 접속

- **Nginx (Reverse Proxy & 정적 파일 서버)**  
  - 포트 80에서 요청을 받고, Vue 앱의 빌드 산출물(`dist` 폴더의 내용) 서빙  
  - `/users/api/` 등의 API 요청은 `http://django_web:8000`으로 프록시

- **Django (백엔드 서버)**  
  - API 요청을 처리하고, 비즈니스 로직 수행  
  - `DATABASE_URL` 환경변수를 통해 PostgreSQL 데이터베이스와 연동

- **Database (PostgreSQL)**  
  - 실제 데이터 저장소, 주소는 `mainline.proxy.rlwy.net:43252`


---

## 실행 방법

1. Home 화면
   <img width="1437" alt="Screenshot 2025-03-05 at 1 52 49 PM" src="https://github.com/user-attachments/assets/8ad2c8be-1d4d-4e02-b3a3-529a800ff440" />

2. About 화면
   <img width="1437" alt="Screenshot 2025-03-05 at 1 53 14 PM" src="https://github.com/user-attachments/assets/2f46b7ce-236b-4ebc-bef6-5a37fe9eb18e" />

3. Register 화면 (회원가입)
   <img width="1437" alt="Screenshot 2025-03-05 at 1 53 35 PM" src="https://github.com/user-attachments/assets/e61ee4d0-ce53-42ba-804b-0592c6dc1618" />

4. Login 화면
   <img width="1437" alt="Screenshot 2025-03-05 at 1 53 45 PM" src="https://github.com/user-attachments/assets/bf02f4cb-ddf6-430c-a4eb-6935522ebfd5" />

5. 검색 화면 (정삭적으로 로그인되었을 경우)
   username, credential, qustion, date 별 필터링 기능을 통한 검색
   <img width="1437" alt="Screenshot 2025-03-05 at 1 57 20 PM" src="https://github.com/user-attachments/assets/458d67a0-32bf-4af1-93f0-1e3b7a21482f" />

6. 로그아웃
   손모양 아이콘을 클릭하면 정상적으로 로그아웃되며 Home 화면으로 돌아감
   <img width="1437" alt="Screenshot 2025-03-05 at 1 57 39 PM" src="https://github.com/user-attachments/assets/dcc03622-e720-441a-9fa4-b1a1464fc809" />
   
---
