# initialize_django_backdjango

## Introduce
- Django Initialize 프로젝트를 통해 자신의 환경값을 가져보기

## Environment
- Backend: Python 3.11.6, Django 5.0.4, DRF 3.15.1
- Database: SQLite3

## Getting Start
1. `python -m venv .venv`
    1. Python 3.11.6 version
    2. pip 24.0 version
2. `source .venv/bin/activate`
3. `pip install --upgrade pip`
4. `pip install -r requirements.txt`
5. `python manage.py runserver --settings=config.django.local`
 
## 구현한 기능
- Custom 기능
    - Exception
    - Authentication (PyJWT)
    - Pagination (페이지넘버 부분)
    - Renderer
    - Response
    - Swagger의 공통 응답 스키마 부분
- CRUD 및 테스트 해보는 앱
    - Auth
    - Board

## License
- Copyright ⓒ DBrider3 Inc. All Rights Reserved.
