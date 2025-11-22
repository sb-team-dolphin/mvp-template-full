# MyApp Backend - FastAPI

FastAPI 기반 백엔드 API 서버

## Features

- ✨ FastAPI 프레임워크
- 📝 자동 Swagger 문서화 (OpenAPI 3.0)
- 🗄️ SQLAlchemy ORM + MySQL
- 🔒 XSS 방지 (bleach)
- 🚀 비동기 처리 지원
- 🐳 Docker 지원
- ⚙️ GitHub Actions CI/CD

## Tech Stack

- **Framework**: FastAPI 0.104+
- **Python**: 3.11+
- **ORM**: SQLAlchemy 2.0
- **Database**: MySQL 8.0
- **Validation**: Pydantic 2.5
- **Server**: Uvicorn

## Project Structure

```
backend_fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 앱
│   ├── config.py            # 환경 설정
│   ├── database.py          # DB 연결
│   ├── models/              # SQLAlchemy 모델
│   ├── schemas/             # Pydantic 스키마
│   ├── routers/             # API 라우터
│   └── services/            # 비즈니스 로직
├── requirements.txt
├── Dockerfile
└── .env.example
```

## Installation

### 1. Python 가상환경 생성

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정

```bash
cp .env.example .env
# .env 파일을 편집하여 데이터베이스 설정
```

### 4. 데이터베이스 준비

MySQL 데이터베이스 생성:

```sql
CREATE DATABASE myappdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Running

### 개발 서버 실행

```bash
uvicorn app.main:app --reload --port 8080
```

또는:

```bash
python -m app.main
```

### Docker로 실행

```bash
docker build -t backend-fastapi .
docker run -p 8080:8080 backend-fastapi
```

## API Documentation

애플리케이션 실행 후 다음 URL로 접속:

- **Swagger UI**: http://localhost:8080/swagger-ui.html
- **OpenAPI JSON**: http://localhost:8080/api-docs
- **ReDoc**: http://localhost:8080/redoc

## API Endpoints

### Health Check

- `GET /health` - 기본 헬스 체크
- `GET /health/detail` - 상세 헬스 체크

### Feedback API

- `POST /api/feedbacks` - 피드백 생성
- `GET /api/feedbacks` - 피드백 목록 조회 (페이지네이션)

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ENVIRONMENT` | 환경 (local/prod) | `local` |
| `DB_HOST` | 데이터베이스 호스트 | `localhost` |
| `DB_PORT` | 데이터베이스 포트 | `3306` |
| `DB_NAME` | 데이터베이스 이름 | `myappdb` |
| `DB_USERNAME` | 데이터베이스 사용자명 | `root` |
| `DB_PASSWORD` | 데이터베이스 비밀번호 | - |
| `SERVER_PORT` | 서버 포트 | `8080` |

## Testing

```bash
pytest -v
```

## Deployment

GitHub Actions를 통한 자동 배포:

1. 코드를 `main` 또는 `develop` 브랜치에 푸시
2. `backend_fastapi/` 경로 변경 감지
3. CI: 테스트 실행
4. Docker 이미지 빌드 및 ECR 푸시
5. ECS 서비스 업데이트

## Spring Boot vs FastAPI 차이점

| Feature | Spring Boot | FastAPI |
|---------|-------------|---------|
| 언어 | Java | Python |
| 성능 | 좋음 | 매우 빠름 (비동기) |
| 학습 곡선 | 가파름 | 완만함 |
| 타입 검증 | Jakarta Validation | Pydantic |
| ORM | JPA/Hibernate | SQLAlchemy |
| 의존성 관리 | Maven/Gradle | pip |
| 컨테이너 크기 | 큼 (~500MB) | 작음 (~200MB) |
| Swagger | SpringDoc 추가 필요 | 자동 생성 |

## License

MIT
