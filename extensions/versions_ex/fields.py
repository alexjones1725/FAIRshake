import uuid
import base64
from django.db.models import UUIDField

class CustomUUIDField(UUIDField):
  def to_python(self, value):
    if value is None:
      return None
    return uuid.UUID(bytes=base64.urlsafe_b64decode((value + '==').replace('_', '/')))

  def from_db_value(self, value, expr, connection):
    if value is None:
      return None
    return base64.urlsafe_b64encode(value.bytes).decode("utf-8").rstrip('=\n').replace('/', '_')
