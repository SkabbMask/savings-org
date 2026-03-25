# Savings-org — Setup

A tiny savings goal tracker. Backend: FastAPI + JSON file. No database, no bullshit.

## On your Linux server

```bash
# 1. Copy the project folder to the server
scp -r savings-org/ user@your-server:/opt/savings-org

# 2. Create a virtualenv and install deps
cd /opt/savings-org
python3 -m venv venv
venv/bin/pip install -r backend/requirements.txt

# 3. Test it works
venv/bin/uvicorn backend.main:app --host 0.0.0.0 --port 8741
# Open http://your-tailscale-ip:8741 — you should see the app
# Ctrl+C when done testing

# 4. Install as a systemd service so it starts on boot
cp savings-org.service /etc/systemd/system/savings-org.service

# Edit the service file — replace YOUR_LINUX_USER with your actual username
nano /etc/systemd/system/savings-org.service

systemctl daemon-reload
systemctl enable savings-org
systemctl start savings-org

# Check it's running
systemctl status savings-org
```

## Access from any device on Tailscale

```
http://your-server-tailscale-ip:8741
```

or if you've set a Tailscale MagicDNS hostname:

```
http://your-server-hostname:8741
```

Bookmark it on your phone's browser — done.

## Data

Goals are stored in `backend/data.json`. Back it up occasionally. That's it.

## Updating the frontend

The HTML file is self-contained — just edit `frontend/index.html` and restart the service
(or don't bother restarting, the file is served fresh on each request).

```bash
systemctl restart savings-org
```
