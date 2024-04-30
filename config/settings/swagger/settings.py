"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Swagger drf-spectacular Settings
"""

SPECTACULAR_SETTINGS = {
    "TITLE": "Initialize Django API",
    "DESCRIPTION": "Initialize Django API Swagger 문서 입니다.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
    },
    # available SwaggerUI versions: https://github.com/swagger-api/swagger-ui/releases
    "SWAGGER_UI_DIST": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest",  # default
    # "POSTPROCESSING_HOOKS": ["core.schema_hooks.custom_hook"], # Custom Hook
}
