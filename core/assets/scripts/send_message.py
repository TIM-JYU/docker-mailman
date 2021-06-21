from mailman.config import config
import smtplib
import tempfile
import subprocess
import os
import sys
import pathlib
import re

FROM_PATTERN = re.compile(r"From: (.*)")

def send_message(mlist, contents=None):
    lmtp = smtplib.LMTP()
    response = lmtp.connect(config.mta.lmtp_host, int(config.mta.lmtp_port))
    print(response)
    
    if not contents:
        tmp, tempfile_path = tempfile.mkstemp()
        os.close(tmp)
        
        path = pathlib.Path(tempfile_path)
        path.write_text(
            "From: \n"
            f"To: {mlist.fqdn_listname}\n"
            "Subject: \n"
            "\n", encoding="utf-8")
        
        proc = subprocess.Popen(["nano", str(path)], close_fds=True)
        proc.communicate()

        contents = path.read_text(encoding="utf-8")

        try:
            path.unlink()
        except FileNotFoundError:
            pass
    
    from_match = FROM_PATTERN.search(contents)
    
    if not from_match:
        print("No valid `From` specified!")
        sys.exit(1)

    from_addr = from_match.group(1).strip()

    res = lmtp.sendmail(from_addr, [mlist.fqdn_listname], contents)
    print(res)
    print("Sent!")