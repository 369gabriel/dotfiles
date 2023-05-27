#!/bin/sh
# xrandr --output HDMI-0 --primary
volumeicon &
flameshot &
lxsession &
picom --config ~/.config/qtile/picom/picom.conf &
#picom -b --animations --animation-window-mass 0.5 --animation-for-open-window zoom --animation-stiffness 350 &
#wal -R -n
nitrogen --restore &
