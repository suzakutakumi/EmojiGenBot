# /usr/bin/bash
if [ -e /etc/systemd/system/emojigenbot.service ]; then
    sudo rm -r /etc/systemd/system/emojigenbot.service
fi

if [ -e /opt/emojigenbot ]; then
    sudo rm -r /opt/emojigenbot/
fi

sudo cp -r . /opt/emojigenbot/
sudo cp ./emojigenbot.service /etc/systemd/system/

sudo chmod 755 /opt/emojigenbot/main.py

sudo systemctl enable emojigenbot.service
