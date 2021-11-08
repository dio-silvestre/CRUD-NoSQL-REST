from pymongo import MongoClient
import datetime
from app.exceptions.post_exceptions import InvalidPostError


client = MongoClient('mongodb://localhost:27017/')

db = client['kenzie']


class Post():
    def __init__(self, title, author, tags, content):
        posts_list = list(db.posts.find())
        if len(posts_list) == 0:
            self._id = 1
        else:
            self._id = posts_list[-1]['_id'] + 1
        self.created_at = datetime.datetime.utcnow()
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content


    @staticmethod
    def get_all():
        posts_list = list(db.posts.find())
        for post in posts_list:
            post['_id'] = str(post['_id'])
        return posts_list


    def save(self):
        _id = db.posts.insert_one(self.__dict__).inserted_id

        if not _id:
            raise InvalidPostError
        
        new_post = db.posts.find_one({'_id': _id})

        return new_post


    @staticmethod
    def get_one(id):
        post = db.posts.find_one({'_id': id})
        return post
        
    
    @staticmethod
    def delete_one(id):
        post = db.posts.find_one({'_id': id})

        if not post:
            raise TypeError

        db.posts.delete_one({'_id': id})
        return post
    

    @staticmethod
    def update_one(id, data):
        post = db.posts.find_one({'_id': id})

        if not post:
            raise TypeError
        elif data.keys() != post.keys():
            raise InvalidPostError

        db.posts.update_one({'_id': id}, {'$set': data, '$set': {'updated_at': datetime.datetime.utcnow()}})

        post = db.posts.find_one({'_id': id})
        return post
