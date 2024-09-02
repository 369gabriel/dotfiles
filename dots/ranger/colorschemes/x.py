# ~/.config/ranger/colorschemes/custom.py
from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Custom(ColorScheme):
    progress_bar_color = 9  # Vermelho

    def use(self, context):
        fg, bg, attr = default_colors
        
        if context.reset:
            return default_colors

        if context.in_browser:
            if context.selected:
                attr = reverse
            if context.empty or context.error:
                fg = 1  # Vermelho
            if context.border:
                fg = 8  # Cinza escuro
            if context.image:
                fg = 4  # Azul
            if context.video:
                fg = 2  # Verde
            if context.audio:
                fg = 5  # Magenta
            if context.document:
                fg = 124  # Ciano
            if context.directory:
                fg = 160  # Branco
                attr |= bold
            if context.executable and not context.directory:
                fg = 9  # Vermelho
                attr |= bold
            if context.link:
                fg = 14  # Azul claro
            if context.marked:
                fg = 0
                bg = 9  # Fundo vermelho
            if not context.selected and (context.cut or context.copied):
                fg = 8  # Cinza escuro
                attr |= bold
            if context.badinfo:
                fg = 9  # Vermelho

        elif context.in_titlebar:
            attr |= bold
            if context.hostname:
                fg = 196 # Verde ou Vermelho
            elif context.directory:
                fg = 7  # Branco
            elif context.tab:
                if context.good:
                    bg = 9  # Verde

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = 9  # Verde
                elif context.bad:
                    fg = 9  # Vermelho
            if context.marked:
                attr |= bold | reverse
                fg = 9  # Vermelho
            if context.message:
                if context.bad:
                    fg = 9  # Vermelho

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = 6  # Ciano

            if context.selected:
                attr |= reverse

        return fg, bg, attr

