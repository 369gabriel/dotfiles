if status is-interactive
    alias JBL 'bluetoothctl connect 70:99:1C:A6:9E:BA'
    alias fone 'bluetoothctl connect B4:F3:18:32:1C:00'
    alias files 'ranger'
    alias ..="cd .." 
    alias ...="cd ../.." 
    alias ....="cd ../../.." 
    alias .....="cd ../../../.." 
    alias ......="cd ../../../../.." 
    alias weather='curl wttr.in'
    alias volup='pulsemixer --change-volume +5'
    alias voldown='pulsemixer --change-volume -5'
    set CONFIG ~/.config
    starship init fish | source

set -U fish_greeting

end
fish_add_path /home/gabriel/.spicetify
