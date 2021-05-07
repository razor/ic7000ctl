#!/bin/sh

RIGMODEL=360
SERIALDEV=/dev/ttyUSB0
MODE="USB 2400"

b160m=1840000
b80m=3573000
b40m=7074000
b30m=10136000
b20m=14074000
b17m=18100000
b15m=21074000
b12m=24915000
b10m=28047000
b6m=50313000

bandkey=$1m

eval "freq=\${b$bandkey}"

echo "set to $1m frequency $freq"

rigctl -m $RIGMODEL -r $SERIALDEV -P RTS F $freq
rigctl -m $RIGMODEL -r $SERIALDEV -P RTS M $MODE
