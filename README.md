# EduSafe – EDU-SAFE Website Blocker

A website blocker tool designed to enhance productivity and responsible internet usage for personal, parental, and organizational applications.

## Features
- URL filtering and blacklist/whitelist management
- Scheduling controls (time-based blocking)
- Usage reporting and analytics dashboard

## Tech Stack
- Python / Browser Extension (JavaScript)
- SQLite for URL rules storage
- Scheduler for time-based controls

## Setup
```bash
pip install -r requirements.txt
python main.py
```

## Usage
1. Add URLs to block in `config/blocklist.txt`
2. Set schedules in `config/schedule.json`
3. Run the blocker and view reports in the dashboard

## Applications
- **Personal**: Focus/productivity mode
- **Parental**: Child internet safety
- **Organizational**: Workplace policy enforcement
