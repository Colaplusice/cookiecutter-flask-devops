from app import create_app
from app import celery

app = create_app()
app.app_context().push()
