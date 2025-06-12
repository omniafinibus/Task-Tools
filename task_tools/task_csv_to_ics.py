import uuid 
import datetime as dt
from os.path import isfile
from lib.arguments import args

# Flags for the command
if args.nano:
    editor = "nano"
else:
    editor = "code"

# Target path handling
if not isfile(args.targetPath):
    print(f"File not found: {args.targetPath}")
    quit()


crntDate = dt.date(2025,1,1)
endDate = dt.date(2025,12,31)

f = open(args.targetPath, 'w')
f.write(
  "".join(
    [
      "BEGIN:VCALENDAR\r\n",
      "VERSION:2.0\r\n",
      "PRODID:-//SabreDAV//SabreDAV//EN\r\n",
      "BEGIN:VTODO\r\n",
      "DTSTAMP:20241223T101311Z\r\n",
      "UID:4600549086604714923\r\n",
      "CREATED:20241223T101310Z\r\n",
      "LAST-MODIFIED:20241223T101310Z\r\n",
      "SUMMARY:Read-a-thon\r\n",
      "PRIORITY:1\r\n",
      "STATUS:NEEDS-ACTION\r\n",
      "X-APPLE-SORT-ORDER:738108049\r\n",
      "DUE;VALUE=DATE:20251231\r\n",
      "DTSTART;VALUE=DATE:20250101\r\n",
      "BEGIN:VALARM\r\n",
      "TRIGGER;RELATED=END:PT0S\r\n",
      "ACTION:DISPLAY\r\n",
      "DESCRIPTION:Default Tasks.org description\r\n",
      "END:VALARM\r\n"
      "END:VTODO\r\n"
    ]
  )
)
f.close()

f = open(args.targetPath, 'a')
while(crntDate<=endDate):
  dateString = crntDate.strftime("%Y%m%d")
  description = f"read {crntDate.isocalendar()[1]} page" + "s" if crntDate.isocalendar()[1] > 1 else ""
  f.write(
    "".join(
      [
        f"BEGIN:VTODO\r\n",
        f"DTSTAMP:20241210T095028Z\r\n",
        f"UID:{str(uuid.uuid1())}\r\n",
        f"SEQUENCE:0\r\n",
        f"CREATED:20241223T202525Z\r\n",
        f"LAST-MODIFIED:20241223T000059Z\r\n",
        f"SUMMARY:{description}\r\n",
        f"STATUS:NEEDS-ACTION\r\n",
        f"RELATED-TO;RELTYPE=PARENT:4600549086604714923\r\n",
        f"DUE;VALUE=DATE:{dateString}\r\n",
        f"DTSTART;VALUE=DATE:{dateString}\r\n",
        f"BEGIN:VALARM\r\n",
        f"TRIGGER;RELATED=END:PT0S\r\n",
        f"ACTION:DISPLAY\r\n",
        f"DESCRIPTION:Default Tasks.org description\r\n",
        f"END:VALARM\r\n",
        f"END:VTODO\r\n"
      ]
    )
  )
  crntDate += dt.timedelta(days=1)

f.write("END:VCALENDAR")
f.close()