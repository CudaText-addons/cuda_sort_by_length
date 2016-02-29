from cudatext import *

class Command:
    def run(self):
        text = ed.get_text_all()
        text = text.splitlines()
        text = [s for s in text if s]
        text = sorted(text, key = lambda x: '%5s'%len(x)+x)
        eol = '\n'
        text = eol.join(text)+eol
        ed.set_text_all(text)
