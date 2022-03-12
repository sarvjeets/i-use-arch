#!/usr/bin/python3
import subprocess

SPAN_OPEN = '<span class="ansi1 ansi36">'
SPAN_CLOSE = '</span>'

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


print("""<!-- Created by plain-ascii-artix.py -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>I use Artix, FYI</title>
<style type="text/css">
.body_foreground { color: #AAAAAA; font-size: 1.5vw; }
.body_background { background-color: #000000; }
.ansi1 { font-weight: bold; }
.ansi30 { color: #000316; }
.ansi31 { color: #aa0000; }
.ansi32 { color: #00aa00; }
.ansi33 { color: #aa5500; }
.ansi34 { color: #0000aa; }
.ansi35 { color: #E850A8; }
.ansi36 { color: #00aaaa; }
.ansi37 { color: #F5F1DE; }
.ansi40 { background-color: #000316; }
.ansi41 { background-color: #aa0000; }
.ansi42 { background-color: #00aa00; }
.ansi43 { background-color: #aa5500; }
.ansi44 { background-color: #0000aa; }
.ansi45 { background-color: #E850A8; }
.ansi46 { background-color: #00aaaa; }
.ansi47 { background-color: #F5F1DE; }
.ansi38-8 { color: #7f7f7f; }
.ansi38-9 { color: #ff0000; }
.ansi38-10 { color: #00ff00; }
.ansi38-11 { color: #ffff00; }
.ansi38-12 { color: #5c5cff; }
.ansi38-13 { color: #ff00ff; }
.ansi38-14 { color: #00ffff; }
.ansi38-15 { color: #ffffff; }
.ansi48-8 { background-color: #7f7f7f; }
.ansi48-9 { background-color: #ff0000; }
.ansi48-10 { background-color: #00ff00; }
.ansi48-11 { background-color: #ffff00; }
.ansi48-12 { background-color: #5c5cff; }
.ansi48-13 { background-color: #ff00ff; }
.ansi48-14 { background-color: #00ffff; }
.ansi48-15 { background-color: #ffffff; }
</style>
</head>
<body class="body_foreground body_background" >
<pre>""")

neofetch_info = subprocess.run(
    ['neofetch', '--off', '--stdout'],
    stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip().splitlines()
neofetch_info += [ '',
("""
<span class="ansi30 ansi40">   </span>
<span class="ansi31 ansi41">   </span>
<span class="ansi32 ansi42">   </span>
<span class="ansi33 ansi43">   </span>
<span class="ansi34 ansi44">   </span>
<span class="ansi35 ansi45">   </span>
<span class="ansi36 ansi46">   </span>
<span class="ansi37 ansi47">   </span>""").replace('\n', ''),
("""
<span class="ansi38-8 ansi48-8">   </span>
<span class="ansi38-9 ansi48-9">   </span>
<span class="ansi38-10 ansi48-10">   </span>
<span class="ansi38-11 ansi48-11">   </span>
<span class="ansi38-12 ansi48-12">   </span>
<span class="ansi38-13 ansi48-13">   </span>
<span class="ansi38-14 ansi48-14">   </span>
<span class="ansi38-15 ansi48-15">   </span>""").replace('\n', '')]

artix_logo = [
"                   '                   ",
"                  'o'                  ",
"                 'ooo'                 ",
"                'ooxoo'                ",
"               'ooxxxoo'               ",
"              'oookkxxoo'              ",
"             'oiioxkkxxoo'             ",
"            ':;:iiiioxxxoo'            ",
"               `'.;::ioxxoo'           ",
"          '-.      `':;jiooo'          ",
"         'oooio-..     `'i:io'         ",
"        'ooooxxxxoio:,.   `'-;'        ",
"       'ooooxxxxxkkxoooIi:-.  `'       ",
"      'ooooxxxxxkkkkxoiiiiiji'         ",
"     'ooooxxxxxkxxoiiii:'`     .i'     ",
"    'ooooxxxxxoi:::'`       .;ioxo'    ",
"   'ooooxooi::'`         .:iiixkxxo'   ",
"  'ooooi:'`                `'';ioxxo'  ",
" 'i:'`                          '':io' ",
"'`                                   `'"]

max_length = max(len(neofetch_info), len(artix_logo))
neofetch_info.extend([''] * (max_length - len(neofetch_info)))
artix_logo.extend([' ' * len(artix_logo[0])] * (max_length - len(artix_logo)))

for i in range(max_length):
    if i == 0:
        info = span_hostname(neofetch_info[i])
    else:
        info = span_info(neofetch_info[i])
    print(f'{span(artix_logo[i])}  {info}')

print("""
</pre>
</div>
</body>
</html>""")

