import click
import MySQLdb

import sys,os,django

sys.path.append(r"C:\Users\Home\PycharmProjects\bvrit")
os.environ["DJANGO_SETTINGS_MODULE"] = "bvrit.settings"
django.setup()

from olx.models import *

@click.command()
def populate_db():
    print 'entered here'
    for user in ['user1','user2','user3']:
        test_user = User(user_name = user,user_email = user+"@abc.com",user_phone = 123456789)
        test_user.save()
        for post in ['post1','post2','post3','post4','post5','post6']:
            test_post = Post(post_created="2016-06-28",post_description= user + "created this " + post , is_sold=True,post_user= test_user)
            test_post.save()

@click.command()
@click.argument('name')
@click.argument('password')
@click.argument('dbname')
def drop_data(name, password,dbname):
    con = MySQLdb.connect(user = name,passwd = password)
    cursor = con.cursor()
    cursor.execute("drop database olxdb;")
    cursor.execute("create database olxdb;")
    con.close()

