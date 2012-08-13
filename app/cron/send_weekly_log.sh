#!/bin/bash
source /home/dotcloud/env/bin/activate
cd ~/current/app
python send_weekly_log --settings=settings_production >> /home/dotcloud/log/send_weekly_log.log 2>&1


