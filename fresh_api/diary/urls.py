from django.urls import path
from .apis import AlphaInstructView

urlpatterns = [
    path('alpha', AlphaInstructView.as_view(), name='alpha-instruct'),
]