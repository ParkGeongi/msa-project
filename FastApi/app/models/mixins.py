from datetime import datetime, timedelta

from sqlalchemy import Column, TIMESTAMP as Timestamp, text


class TimstampMixin(object):
    kst = datetime.utcnow() + timedelta(hours=9)  # 한국 표준시인 KST는 UTC로부터 9시간을 더하면 된다
    now = kst.strftime("%Y-%m-%d %H:%M:%S")
    created = Column(Timestamp,nullable=True, server_default =text("current_timestamp"))
    modified = Column(Timestamp,nullable=True, server_default =text("current_timestamp on update current_timestamp"))

