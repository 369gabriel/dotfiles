if status is-interactive
    alias s 'sudo'
    alias p 'pacman'
    alias jbl 'bluetoothctl connect 70:99:1C:A6:9E:BA'
    alias fone 'bluetoothctl connect 41:42:27:90:00:00'
    alias djbl 'bluetoothctl disconnect 70:99:1C:A6:9E:BA'
    alias dfone 'bluetoothctl disconnect 41:42:27:90:00:00'
    alias grayon 'vibrant-cli eDP-1 0.0'
    alias grayoff 'vibrant-cli eDP-1 1.0'
    
    alias files 'ranger'
    alias ..="cd .." 
    alias ...="cd ../.." 
    alias ....="cd ../../.." 
    alias .....="cd ../../../.." 
    alias ......="cd ../../../../.." 
    alias s "sudo"
    alias weather='curl wttr.in'
    alias volup='pulsemixer --change-volume +5'
    alias voldown='pulsemixer --change-volume -5'
    alias nvimconfig='nvim ~/.config/nvim'
    alias dots='nvim ~/.config'
    set CONFIG ~/.config
    starship init fish | source

set -U fish_greeting
set -x XDG_CONFIG_HOME $HOME/.config
export EDITOR=nvim
end
fish_add_path ~/.spicetify
if test -z "$DISPLAY" -a (tty) = "/dev/tty1"
    startx
end

if command -v tmux &> /dev/null && [ -z "$TMUX" ]
    # Tenta anexar a uma sessão existente
    tmux attach || tmux new
end
