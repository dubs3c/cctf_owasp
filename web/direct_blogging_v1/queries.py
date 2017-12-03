import config
from time import gmtime, strftime

def get_all_posts():
    cur = config.query_db(
        "select * \
        from posts \
        WHERE published = 1")
    return cur

def get_post(slug):
    cur = config.query_db(
        "select * \
        from posts p \
        where p.id=?", [slug], one=True)
    return cur
