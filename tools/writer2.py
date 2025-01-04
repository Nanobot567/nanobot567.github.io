#! /bin/python3

import dearpygui.dearpygui as dpg

from datetime import datetime
from os import getcwd,chdir

chdir("..")

now = datetime.today()
now = [str(now.month),str(now.day+1),str(now.year)]
todaysdate = now[0]+"/"+now[1]+"/"+now[2][2:]

print("found date is "+todaysdate+"\n")

dpg.create_context()
dpg.create_viewport(title="writer")
dpg.setup_dearpygui()


def accept():
    htmfile = f"""<DOCTYPE !HTML>
  <html>
    <head>
        <link rel="stylesheet" type="text/css" href="../css/style.css">
        <title>
            nanobot567's website | blog | {todaysdate}
        </title>
    </head>
    <body>
        <h4 class = "backbtn"><a href="../blog.html"><-- back</a></h4>
        <h1 class = "title">nanobot567's website<span class="blink">_</span> </h1>
        <h2>blog</h2>

        <h3><u>{todaysdate}</u></h3>

INSERT_TEXT_HERE_THANKS
    </body>
  </html>
</DOCTYPE>
"""
    
    newtext = []

    text = dpg.get_value("inputtext")
    print("text: "+text)
    text = text.replace("\n\n","\n        </p>\n")

    for i in text.split("\n"):
        newtext.append("        "+i)
    
    text = "\n".join(newtext)
    
    htmfile = htmfile.replace("INSERT_TEXT_HERE_THANKS",text)

    with open("blog/"+todaysdate.replace("/","-")+".html","w+") as f:
        f.write(htmfile)
        print("wrote post to blog/"+todaysdate.replace("/","-")+".html")

    with open("blog.html", "r") as f:
        html = f.read()
        index = html.rfind("</h3>")
        html = html[:index+6] + f'        <h3><a href="blog/{todaysdate.replace("/","-")}.html" class="menu">{todaysdate}</a></h3>\n' + html[index+6:]
        print("replaced text in blog.html")
    
    with open("blog.html", "w") as f:
        f.write(html)
        print("wrote changes to blog.html")

    quit()

def insertAtCursor(text):
    inputtext = dpg.get_value("inputtext")
    inputtext += text

    dpg.set_value("inputtext", inputtext)

with dpg.window(tag="primary") as w:
    w = dpg.get_viewport_width()
    h = dpg.get_viewport_height()
    dpg.add_input_text(multiline=True, tag="inputtext", width=w, height=h, pos=[0,20])

with dpg.window(tag="tools", label="Tools", width=280, height=150, pos=[dpg.get_viewport_width()-290, 10]):
    with dpg.group(horizontal=True):
        dpg.add_button(label="HEADER1", callback=lambda: insertAtCursor("<h1></h1>"))
        dpg.add_button(label="HEADER2", callback=lambda: insertAtCursor("<h2></h2>"))
        dpg.add_button(label="HEADER3", callback=lambda: insertAtCursor("<h3></h3>"))
        dpg.add_button(label="HEADER4", callback=lambda: insertAtCursor("<h4></h4>"))

    with dpg.group(horizontal=True):
        dpg.add_button(label="REDACTED", callback=lambda: insertAtCursor("<span class=\"redacted\"></span>"))
        dpg.add_button(label="RAINBOW", callback=lambda: insertAtCursor("<span class=\"rainbow\"></span>"))
        dpg.add_button(label="BLINK", callback=lambda: insertAtCursor("<span class=\"blink\"></span>"))
        dpg.add_button(label="FASTBLINK", callback=lambda: insertAtCursor("<span class=\"fastblink\"></span>"))
    dpg.add_button(label="HIDDEN", callback=lambda: insertAtCursor("""<button onclick="hideshow('hideshowdiv')" class="btn">TEXT</button>
<div id="hideshowdiv" style="display: none;"></div>"""))

    dpg.add_button(label="DONE", callback=accept)

with dpg.viewport_menu_bar():
    with dpg.menu(label="writer"):

    #dpg.add_menu_item(label="Help", callback=print_me)
        dpg.add_menu_item(label="About dearpygui", callback=dpg.show_about)
        dpg.add_menu_item(label="Debug", callback=dpg.show_debug)

dpg.set_primary_window("primary", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
