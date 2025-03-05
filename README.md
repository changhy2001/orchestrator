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
│   ├── search
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── api_views.py
│   ├── users
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
