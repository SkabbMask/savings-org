# Savings-org — Setup

A tiny savings goal tracker. Backend: FastAPI + JSON file. No database, no bullshit.

## On server

```bash
# 1. Install deps
pip install -r backend/requirements.txt

# 2. Test it works
uvicorn backend.main:app --host 0.0.0.0 --port 8741

# 3. Install as a systemd service so it starts on boot
cp savings-org.service /etc/systemd/system/savings-org.service

# Edit the service file — replace YOUR_LINUX_USER with your actual username
nano /etc/systemd/system/savings-org.service

systemctl daemon-reload
systemctl enable savings-org
systemctl start savings-org

# Check it's running
systemctl status savings-org
```

## Data

Goals are stored in `backend/data.json`. Back it up occasionally. That's it.

## Updating the frontend

The HTML file is self-contained — just edit `frontend/index.html` and restart the service
(or don't bother restarting, the file is served fresh on each request).

```bash
systemctl restart savings-org
```
