# -*- coding: utf-8 -*-

import codecs
import glob
# Subtitles downloaded from https://www.tusubtitulo.com/show/1261

def get_all_lines_in_srt_file(fname):
    content = ""
    all_lines = codecs.open(fname, 'r', encoding='iso-8859-1').read()
    for line in all_lines.split("\n"):
        line = line.strip()
        if line:
            start_char = line[0]
            if not(start_char.isdigit() ):
                content += line + "\n"
                print(line)
    return content


if __name__ == '__main__':
    file_names = glob.glob("*.srt")
    for fn in file_names:
        res = get_all_lines_in_srt_file(fn)
        print(res)
    # TODO: Don't forget to remove the following lines from the resulting file:
    """
    www.SUBTITULOS.es
    -DIFUNDE LA PALABRA-
    """
