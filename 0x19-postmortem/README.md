SSH Key Authentication Failure
Duration: 1 hour (Feb 14, 2024 from 3:00 PM to 4:00 PM )
Impact: I was unable to log  into my  web-01 server, causing delays


Root cause: RSA key due to improper .ssh directory permission
Timeline:
3:00 PM: I  attempted to SSH into web-01, authentication failure
3:10 PM: Confirmed SSH config and key location correct
3:15 PM: Permissions issue hypothesized and confirmed for .ssh dir
3:20 PM: .ssh dir permissions corrected
3:25 PM: Still unable to SSH, RSA keys corrupted
3:30 PM: Existing keys removed, new keys generated
3:35 PM: Tested SSH again, able to connect


Root Cause & Resolution:
Incorrect permissions on my  .ssh directory allowed corruption of the RSA keys stored there. Fixed by correcting permissions and regenerating new keys.
Corrective Actions:
Document proper .ssh directory permissions for myself
Add monitoring for SSH connection failures

