
setxkbmap -layout br&
nitrogen --restore &
exec dwm&
picom&
slstatus&
xrdb .Xresources&

while :; do
	dwm 2> ~/.dwm.log
done
