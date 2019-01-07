from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['mytest']
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('Inserted_id: {}'.format(result.inserted_id))

