import requests
from pathlib import Path
import os
import uuid

uid = uuid.uuid4()
from datetime import datetime
current_date = datetime.now()
at = current_date.isoformat()


API_KEY = os.environ.get("PDFCO_KEY")
URL = os.environ.get("RESUME_URL")

def get(fmt="Letter"):
    config = {
        "url": URL,
        "margins": "5mm",
        "paperSize": fmt,
        "orientation": "Portrait",
        "printBackground": True,
        "header": f"AUTO GENERATED FROM RESUME.BAS.WORK WITH {uid} @ {at}",
        "footer": "",
        "mediaType": "print",
        "async": False,
        "encrypt": False,
        "profiles": "{ \"CustomScript\": \";; // put some custom js script here \"}"
    }
    url = "https://api.pdf.co/v1/pdf/convert/from/url"
    r = requests.post(url, json=config, headers={"x-api-key": API_KEY})
    result = r.json()
    url = result["url"]
    r = requests.get(url)
    with open(f"resume.{fmt}.pdf", "wb") as f:
        f.write(r.content)
    return Path(f"resume.{fmt}.pdf")


if __name__ == "__main__":
    fmts = ['Letter', 'A4']
    for fmt in fmts:
        get(fmt=fmt).rename(f"static_pdf/resume.{fmt.lower()}.pdf")

