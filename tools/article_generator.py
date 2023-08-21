"""generates template for a new article"""
from sys import argv
import datetime
import os
import get_first_article_paragraph
TEMPLATE = """
<div>
    <p class="article-date"><b>Posted:</b> {DATE}</p>
    <h2 class="article-title">
        <a href="{LINK}">
            {TITLE}
        </a>
        <br />
        <p class="tag creator" title="Creator">
            {CREATOR}
        </p>
        <p class="tag {TAG[0]}">{CAPITALIZED_TAG[0]}</p>
        <p class="tag {TAG[1]}">{CAPITALIZED_TAG[1]}</p>
        <p class="tag {TAG[2]}">{CAPITALIZED_TAG[2]}</p>
    </h2>
    <p class="article-desc">
        {TEXT}
        <a href="{LINK}">Read More</a>
    </p>
</div>
<hr />
"""

def get_info():
    """gets info"""
    date    = input("article publish date: ") or "TBA <DATE>"
    creator = input("article author: ") or "TBA <CREATOR>"
    title   = input("article title: ") or "TBA <TITLE>"
    tags    = input("Tags (seperate with commas): ") or "TBA,TBA,TBA"
    return (date, creator, title, tags.replace(", ", ",").strip().split(","))

def gen(link,text):
    """generates HTML"""
    date,creator,title,tags = get_info()
    cap_tags = []
    for tag in tags:
        cap_tags.append(tag.capitalize())
    new_temp = TEMPLATE.format(DATE=date, LINK=link, CREATOR=creator, TITLE=title, TAG=tags, CAPITALIZED_TAG=cap_tags, TEXT=text)
    return (new_temp,title,link)

def double_check(site,text,count:int=0):
    """makes sure text intro intro is fine"""
    print(text)
    choice = input("use text as introduction?[Y/n]: ") or "Y"
    if choice.lower() != "y":
        count += 1
        _,text = get_first_article_paragraph.get_para(site, count)
        double_check(site,text,count)
        

def main():
    """main"""
    #sites = ["https://maia.crimew.gay/posts/kick.com-sucks/", "https://notnite.com/blog/ffxiv-modloader-ace/", "https://kenschutte.com/python-swap-ints/"]
    if len(argv) <= 1:
        sites = [input("article URL: ")]
    else: sites = [argv[1]]
    for site in sites: 
        link, text = get_first_article_paragraph.get_para(site)
        if "ERROR" in text:
            print(text)
            continue
        double_check(site,text)
        HTML,title,link = gen(link,text)

        if not os.path.isdir("html_out"):
            os.mkdir("html_out")

        with open(f"html_out/{title}.html", "w") as f:
            f.write(HTML)
            print(f"saved to {title}.html")
        with open(".sites_created.csv", "a") as site_log:
            site_log.write(f"{title}, {link}, {datetime.datetime.now()}\n")
try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("EXITING....")
