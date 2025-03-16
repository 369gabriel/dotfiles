#!/bin/bash

setxkbmap -layout br&
numlockx &
nitrogen --restore &
dunst&
export __NV_PRIME_RENDER_OFFLOAD=1
exec dwm&
picom --config ~/.config/picom/picom.conf&
slstatus&
xrdb .Xresources&

while :; do
	dwm 2> ~/.dwm.log
done
