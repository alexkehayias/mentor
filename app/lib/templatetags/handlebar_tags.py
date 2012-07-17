from django import template
from django.template import TOKEN_VAR, TOKEN_BLOCK, Node

register = template.Library()

class RawNode(Node):
    def __init__(self, text):
        self.text = text

    def render(self, context):
        return self.text

@register.tag
def raw(parser, token):
    '''Tells django templates to ignore the code in this 
    block. This allows us to use handlebar templates within
    django templates without conflict.'''
    text = []
    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endraw': break
        text.append({
            TOKEN_VAR: '{{%s}}',
            TOKEN_BLOCK: '{%%%s%%}',
        }.get(token.token_type, '%s') % token.contents)
    return RawNode(''.join(text))



