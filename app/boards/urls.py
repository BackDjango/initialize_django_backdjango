"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Board Urls
"""

# System
from django.urls import path, include

# Project
from app.boards.views import BoardViewSet

auth_urls = [
    path(
        "",
        BoardViewSet.as_view({"get": "list_board", "post": "create_board"}),
        name="create-list-board",
    ),
    path(
        "/<int:board_id>",
        BoardViewSet.as_view({"get": "detail_board", "put": "update_board", "delete": "delete_board"}),
        name="detail-update-delete-board",
    ),
]

urlpatterns = [
    path("/boards", include(auth_urls)),
]
