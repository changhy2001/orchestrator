## 프로젝트 구조

```plaintext
.
├── docker-compose.yml
├── .env.template
├── backend
│   ├── config
│   │   └── nginx
│   │       └── project.conf 
│   ├── core
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── asgi.py
│   ├── search                      # DB 검색 기능
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── users                       # 유저 관리 (회원가입, 로그인, 로그아웃)
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
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
   git clone https://github.com/changhy2001/orchestrator.git
   cd orchestrator
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
         │  - API 프록시: /users/ 요청을 Django로 전달       │
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
  - `/users/` 등의 API 요청은 `http://django_web:8000`으로 프록시

- **Django (백엔드 서버)**  
  - API 요청을 처리하고, 비즈니스 로직 수행  
  - `DATABASE_URL` 환경변수를 통해 PostgreSQL 데이터베이스와 연동

- **Database (PostgreSQL)**  
  - 실제 데이터 저장소, 주소는 `mainline.proxy.rlwy.net:43252`


---

## 실행 방법

1. Home 화면
   <img width="1440" alt="Screenshot 2025-03-09 at 8 52 13 PM" src="https://github.com/user-attachments/assets/dcf745fb-7ab4-4580-ba00-c95e41105b65" />


2. About 화면
   <img width="1440" alt="Screenshot 2025-03-09 at 8 49 39 PM" src="https://github.com/user-attachments/assets/ff885853-8ab7-452c-a798-ecc59566e339" />


3. Register 화면 (회원가입)
   <img width="1440" alt="Screenshot 2025-03-09 at 8 49 53 PM" src="https://github.com/user-attachments/assets/86b786d8-7c02-4d6b-9908-5bd8d90a60f4" />


4. Login 화면
   <img width="1440" alt="Screenshot 2025-03-09 at 8 50 40 PM" src="https://github.com/user-attachments/assets/9ca9c942-a1d1-4a15-a39a-30fa8a8dcf4e" />


5. 검색 화면 (정삭적으로 로그인되었을 경우) - username, credential, qustion, date 별 필터링 기능을 통한 검색
   <img width="1440" alt="Screenshot 2025-03-12 at 8 06 29 PM" src="https://github.com/user-attachments/assets/3449edbd-1d37-405b-b80c-a27be2eb998d" />


6. 유저 클릭 시 테이블 상세 data 확인
   <img width="1440" alt="Screenshot 2025-03-12 at 8 06 39 PM" src="https://github.com/user-attachments/assets/f532d1c5-3b15-4854-8474-6faf04c80710" />


8. 로그아웃 - 로그아웃 텍스트 클릭 시 정상적으로 로그아웃되며 Home 화면으로 돌아감
   
   
---
