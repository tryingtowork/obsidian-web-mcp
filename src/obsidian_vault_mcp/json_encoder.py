"""JSON encoder with support for date/datetime objects."""
import json
from datetime import date, datetime


class DateAwareEncoder(json.JSONEncoder):
    """JSON encoder that serializes date/datetime as ISO 8601 strings."""
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return super().default(obj)


def safe_json_dumps(data) -> str:
    """Drop-in replacement for json.dumps that handles dates."""
    return json.dumps(data, cls=DateAwareEncoder)