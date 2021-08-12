#!/usr/bin/python3
import subprocess

SPAN_OPEN = '<span class="ansi1 ansi36">'
SPAN_CLOSE = '</span>'

def extend_list(a, length):
    """Extends list a to make it at least length by padding with '' elements"""
    assert len(a) <= length
    a.extend([''] * (length - len(a)))

def span(line):
    return f'{SPAN_OPEN}{line}{SPAN_CLOSE}'

def span_hostname(line):
    parts = line.rstrip().partition('@')
    assert len(parts) == 3
    return f'{span(parts[0])}@{span(parts[2])}'

def span_info(line):
    parts = line.rstrip().partition(':')
    if not parts[1]:
        # This will happen for 2nd line after hostname
        return line
    return f'{span(parts[0])}:{parts[2]}'


print("""<!-- Created by plain-ascii.py -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>I use Arch, FYI</title>
<style type="text/css">
.body_foreground { color: #AAAAAA; font-size: 1.5vw; }
.body_background { background-color: #000000; }
.ansi1 { font-weight: bold; }
.ansi36 { color: #00aaaa; }
</style>
</head>
<body class="body_foreground body_background" >
<pre>""")

neofetch_info = subprocess.run(
    ['neofetch', '--off', '--stdout'],
    stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip().splitlines()
arch_logo = [
'                   -`                 ',
'                  .o+`                ',
'                 `ooo/                ',
'                `+oooo:               ',
'               `+oooooo:              ',
'               -+oooooo+:             ',
'             `/:-:++oooo+:            ',
'            `/++++/+++++++:           ',
'           `/++++++++++++++:          ',
'          `/+++ooooooooooooo/`        ',
'         ./ooosssso++osssssso+`       ',
'        .oossssso-````/ossssss+`      ',
'       -osssssso.      :ssssssso.     ',
'      :osssssss/        osssso+++.    ',
'     /ossssssss/        +ssssooo/-    ',
'   `/ossssso+/:-        -:/+osssso+-  ',
'  `+sso+:-`                 `.-/+oso: ',
' `++:.                           `-/+/',
' .`                                 `/']

max_length = max(len(neofetch_info), len(arch_logo))
extend_list(neofetch_info, max_length)
extend_list(arch_logo, max_length)

for i in range(max_length):
    if i == 0:
        info = span_hostname(neofetch_info[i])
    else:
        info = span_info(neofetch_info[i])
    print(f'{span(arch_logo[i])}  {info}')

print("""
</pre>
</div>
</body>
</html>""")

