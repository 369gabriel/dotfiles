
setxkbmap -layout br&
nitrogen --restore &
exec dwm&
picom --config ~/.config/picom/picom.conf&
slstatus&
xrdb .Xresources&

while :; do
	dwm 2> ~/.dwm.log
done
