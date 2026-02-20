from datetime import datetime, timezone
from zoneinfo import ZoneInfo
tc = datetime.now(ZoneInfo("Asia/Almaty"))
tc1 = datetime.now(timezone.utc)
print(tc)
print(tc1)