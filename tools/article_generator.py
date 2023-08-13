"""generates template for a new article"""
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
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
        Labore reprehenderit aut qui harum velit neque voluptas, 
        dolorem id quod maiores nam? 
        Pariatur fuga laboriosam dolorem nam 
        repellendus ea totam consequuntur.
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
        Labore reprehenderit aut qui harum velit neque voluptas, 
        dolorem id quod maiores nam? 
        Pariatur fuga laboriosam dolorem nam 
        repellendus ea totam consequuntur.
        <a href="{LINK}">Read More</a>
    </p>
</div>
<hr />
"""

def get_info():
    date    = input("article publish date: ")
    link    = input("article link: ")
    creator = input("article author: ")
    title   = input("article title: ")
    tags     = input("Tags (seperate with commas): ")
    return (date, link, creator, title, tags.replace(", ", ",").strip().split(","))

def main():
    """main"""
    #print("Hello, World!")
    date,link,creator,title,tags = get_info()
    cap_tags = []
    for tag in tags:
        cap_tags.append(tag.capitalize())
        
    new_temp = TEMPLATE.format(DATE=date, LINK=link, CREATOR=creator, TITLE=title, TAG=tags, CAPITALIZED_TAG=cap_tags)
    print(new_temp)
try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("EXITING....")
