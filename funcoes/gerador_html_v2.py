#!/usr/local/bin/python3

def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == '__main__':
    print(tag_bloco('bloco', 'row', True))
    print(tag_bloco('inline', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('fail', classe='error'))