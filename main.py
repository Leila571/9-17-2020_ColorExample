'''
Leila Lopez Marks
9/17/20
Learning to use colored text library
'''

from colored import fg, bg, attr
import colored
from colored import stylize
color = fg('#C0C0C0') + bg('#00005f')
res = attr('reset')

print ('%s Hello World !!! %s' % (fg(1), attr(0)))
print ('%s%s Hello World !!! %s' % (fg(1), bg(15), attr(0)))
print ('%s%s Hello World !!! %s' % (fg('white'), bg('yellow'), attr('reset')))

print (color + "|\---/|" + res)
print (color + "| o_o |" + res)
print (color + " \_^_/" + res)
