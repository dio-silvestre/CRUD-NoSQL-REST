from pymongo import MongoClient
import datetime
from app.exceptions.post_exceptions import InvalidPostError


client = MongoClient('mongodb://localhost:27017/')

db = client['kenzie']

db.counters.insert_one({'count': 1})


class Post():
    def __init__(self, title, author, tags, content):
        id_number = db.counters.find()[0]['count']
        self._id = id_number
        self.created_at = datetime.datetime.utcnow()
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content
        

    @staticmethod
    def update_counter():
        id_number = db.counters.find()[0]
        update = db.counters.find_one_and_update(id_number, {'$inc': {'count': 1}})
        return update


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

        if not post:
            raise TypeError

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

        for _ in post.keys():
            for keys in data.keys():
                if keys not in post.keys():
                    raise InvalidPostError

        db.posts.update_one(post, {'$set': data})
        db.posts.update_one(post, {'$set': {'updated_at': datetime.datetime.utcnow()}})

        updated_post = db.posts.find_one({'_id': id})
        return updated_post
