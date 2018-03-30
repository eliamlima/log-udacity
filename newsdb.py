#!/usr/bin/env python3
import psycopg2
# Database code for the DB Forum, full solution!
# -*- coding: utf-8 -*-

DBNAME = "news"


def get_posts(option):
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    if option == 'top3':
        print "Question 1: What are the most popular \
three articles of all time?\n"
        c.execute("select articles.title, count(log.path) as num \
        from articles join log \
        on log.path like concat('%', articles.slug) \
        group by articles.title order by num desc limit 3;")
        posts = c.fetchall()
        result = "'%s' - %s views\n"
        result = "".join(result % (a, b) for a, b in posts)

    elif option == 'topauthors':
        print "Question 2: Who are the most popular article \
authors of all time?\n"
        c.execute("select u.name, count(l.path) as num\
        from authors u join articles a\
        on u.id = a.author join log l\
        on l.path like '%' || a.slug\
        group by u.name order by num desc;")
        posts = c.fetchall()
        result = "%s - %s views\n"
        result = "".join(result % (a, b) for a, b in posts)

    elif option == 'errors':
        print "Question 3: Which days, more than 1 %% of requests \
result in errors?\n"
        c.execute("select day, round(pcter, 2) as pcter from\
        (select te.day as day, \
        (te.errors::decimal/td.total::decimal)*100 as pcter\
        from totalerrors te join totalperday td\
        on te.day = td.day) as calc\
        where pcter > 1\
        order by pcter;")
        posts = c.fetchall()
        result = "%s - %s %% errors\n"
        result = "".join(result % (a.strftime('%B %d, %Y'), b)
                         for a, b in posts)
    else:
        return 0

    print result
    db.close()
    return posts
