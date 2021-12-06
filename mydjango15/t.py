# 포스팅 : 제목, 내용, 글쓴이

post = ("제목", "내용",  "글쓴이", "작성일자")
post[0]
post[1]
post[2]  # 글쓴이

# namedtuple

from collections import namedtuple

Post = namedtuple('Post', 'title content author_name')
post = Post("제목", "내용", "글쓴이")
post[0], post[1], post[2]
post.title, post.content, post.author_name

def check_content(content: str) -> bool:
    if len(content) == 0:
        # error ...
    # ...


# CapitalCase
class Post:
    # 생성자 (Contructor)
    def __init__(self, ttt, content, author_name):
        self.title = ttt
        self.content = content
        self.author_name = author_name

    def check_content(self):
        if len(self.content) == 0:
            # error ...
            pass

post = Post("제목", "내용", "글쓴이")
post.title
post.content
post.author_name
post.check_content()