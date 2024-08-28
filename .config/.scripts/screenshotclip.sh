#!/bin/bash

scrot --select --line mode=edge /tmp/screenshot.png -e 'xclip -selection clipboard -t image/png -i /tmp/screenshot.png && rm /tmp/screenshot.png'
