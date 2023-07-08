import datetime
import time
from django import template

register = template.Library()

# @register.filter(name='get_real_time_date_format')
@register.simple_tag
def get_real_time_date_format(date):
  """
  Get the real-time date format for a Django template.

  Args:
    date: The date to format.

  Returns:
    The formatted date.
  """

  now = datetime.datetime.now()
  difference = now - date
  minutes_ago = difference.total_seconds() // 60

  if minutes_ago == 0:
    return "Just now"
  elif minutes_ago == 1:
    return "1 min ago"
  elif minutes_ago <= 59:
    return f"{minutes_ago} mins ago"
  elif minutes_ago <= 1440:
    return "Today"
  elif minutes_ago <= 43200:
    return "Yesterday"
  else:
    return f"{date.strftime('%B %d')} ({minutes_ago // 43200} months ago)"