#! /bin/python3

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
from os import getcwd,chdir

chdir("..")

now = datetime.today()
now = [str(now.month),str(now.day),str(now.year)]
todaysdate = now[0]+"/"+now[1]+"/"+now[2]

text = ""
html = ""

print("found date is "+todaysdate)
print("enter your blog post below now. type /q to quit\n")

root = Tk()

label = Label(root, text="Enter your comment:")
label.pack(pady=10)

textbox = ScrolledText(root, width=50, height=10, wrap=WORD)
textbox.pack(pady=10)

def accept():
    htmfile = f"""<DOCTYPE !HTML>
  <html>
    <head>
        <link rel="stylesheet" type="text/css" href="../css/style.css">
        <title>
            nanobot567's website | blog | {todaysdate}
        </title>
    </head>
    <body style="background-color:black;">
        <h4 class = "backbtn"><a href="../blog.html"><-- back</a></h4>
        <h1 class = "title">nanobot567's website<span class="blink">_</span> </h1>
        <h2>blog</h2>

        <h3><u>{todaysdate}</u></h3>
        <h4>INSERT_TEXT_HERE_THANKS
        </h4>
    </body>
  </html>
</DOCTYPE>
"""

    text = textbox.get("1.0", END)
    htmfile = htmfile.replace("INSERT_TEXT_HERE_THANKS",text)

    with open("blog/"+todaysdate.replace("/","-")+".html","w+") as f:
        f.write(htmfile)

    with open("blog.html", "r") as f:
        html = f.read()
        index = html.rfind("</h3>")
        html = html[:index+6] + f'        <h3><a href="blog/{todaysdate.replace("/","-")}.html" class="menu">{todaysdate}</a></h3>\n' + html[index+6:]
    
    with open("blog.html", "w") as f:
        f.write(html)

button = Button(root, text="Accept", command=accept)
button.pack(pady=10)

root.mainloop()
