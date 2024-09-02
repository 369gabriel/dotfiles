

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget

mod = "mod4"
terminal = "kitty"

import os
import subprocess

os.system("xset -dpms")
os.system("xset s off")
os.system("xset s noblank")

from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "c", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "n", lazy.spawn('thunar'), desc="Launch File Manager"),
    Key([mod], "w", lazy.spawn('firefox'), desc="Launch Browser"),
    #Key([mod], "o", lazy.spawn('notion-app'), desc="Launch notion"),
    Key([mod], "v", lazy.spawn('gpaste-client ui'), desc="Launch Gpaste"),
    Key([mod], "Print", lazy.spawn('gnome-screenshot -i'), desc="Launch screenshot menu"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "e", lazy.spawn('rofi -show power-menu -modi power-menu:rofi-power-menu'), desc="Power Menu"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show run"), desc="Spawn a command using a prompt widget"),
    # Fn Keys
    Key([mod], "F11", lazy.spawn('brightnessctl set 5%+')),
    Key([mod], "F10", lazy.spawn('brightnessctl set 5%-')),
    Key([mod], "F3", lazy.spawn('pulsemixer --change-volume +5')),
    Key([mod], "F2", lazy.spawn('pulsemixer --change-volume -5')),
]

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

group_labels = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "treetab", "floating",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


'''
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
'''

layouts = [
    layout.Columns(border_focus_stack='#ab0303', border_width=2, margin=5, border_on_single=True, fair=True, border_focus='#ab0303', border_normal='610000'),
    layout.Floating(border_focus='#ab0303', border_normal='#502323', border_width=2, fullscreen_border_width=0, max_border_width=0),
    #layout.Floating(border_focus='#ab0303', border_width=5, border_normal='#ab0303'),
]

widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize=10,
    padding=0,
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    "",
                    fontsize=25,
                    padding=10,
                    foreground='#ab0303',
                    mouse_callbacks = {'Button1': lazy.spawn("clearine")}
                ),
                #widget.CurrentLayout(),
                widget.Spacer(),
                widget.WindowTabs(
                    fontsize='11',
                   foreground='#ff2929'
                    ),
                widget.Spacer(),
                widget.GroupBox(
                    highlight_method="text",
                    this_current_screen_border='#ab0303', ##D37B8A
                    fontsize=15,
                    ),
                widget.Spacer(),
                widget.Systray(),
                widget.Sep(foreground= '#222', size_percent=50,padding=8),
                widget.Volume(fmt='  {}', volume_app="kitty --hold sh -c 'pulsemixer'", foreground= '#ab0303'),
                widget.Sep(foreground= '#222', size_percent=50,padding=8),
                widget.UPowerWidget(fill_normal='#ab0303', border_charge_colour='#6b6b69', border_colour='#DDD'),
#                widget.Battery(foreground='EB0D11', format=' {percent:1.0%}', full_char=''),
                widget.Sep(foreground= '#222', size_percent=50,padding=8),
                widget.Clock(format='%d/%m/%y %H:%M', foreground= '#ab0303'),
                #widget.QuickExit(),
            ],
            30,
            margin=[3,3,0,3],
            background='#151515',
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus='#202020',
	border_normal='#111',
	margin=10,
	border_width=2,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
