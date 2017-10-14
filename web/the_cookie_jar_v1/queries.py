import config
from time import gmtime, strftime

def get_all_posts():
    cur = config.query_db(
        "select p.title, p.slug, p.content, p.created_at ,u.username as author \
        from posts p \
        JOIN users u ON u.id=p.author")
    return cur

def get_post(slug):
    cur = config.query_db(
        "select p.title, p.slug, p.content, p.created_at ,u.username as author \
        from posts p \
        JOIN users u ON u.id=p.author \
        where p.slug=?", [slug], one=True)
    return cur


def get_profile(username):
    cur = config.query_db("select username, email, created_at from users where username=?", [username], one=True)
    return cur

def register_account(username, email, password):
    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    cur = config.query_insert("insert into users(username, email, password, created_at) values(?,?,?,?)", (username,email,password,date))
    if not cur:
        return false
    return cur

def get_users():
    cur = config.query_db("select * from users")
    return cur
