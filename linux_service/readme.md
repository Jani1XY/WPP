# How to set up this service

## Reload systemd
`sudo systemctl daemon-reload`

## Enable the service
`sudo systemctl enable wpp.service`

## Start the service
`sudo systemctl start wpp.service`


### Check status
`sudo systemctl status wpp.service`

### Check logs
`sudo journalctl -u wpp.service`