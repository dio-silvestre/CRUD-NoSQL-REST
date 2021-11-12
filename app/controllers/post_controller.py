from flask import Flask, jsonify, request
from app.models.post_model import Post
from http import HTTPStatus
from app.exceptions.post_exceptions import InvalidPostError


def init_app(app: Flask):

    @app.get('/posts')
    def read_posts():
        posts_list = Post.get_all()
        return jsonify(posts_list), HTTPStatus.OK


    @app.post('/posts')
    def create_post():
        data = request.json

        try:
            post = Post(**data)
            new_post = post.save()
            Post.update_counter()
            return new_post, HTTPStatus.CREATED
        except (InvalidPostError, TypeError):
            return {'message': 'Dados inválidos para a criação de um post.'}, HTTPStatus.BAD_REQUEST


    @app.get('/posts/<int:id>')
    def read_post_by_id(id):
        try:
            post = Post.get_one(id)
            return post, HTTPStatus.OK
        except TypeError:
            return {'message': 'Post inexistente.'}, HTTPStatus.NOT_FOUND


    @app.delete('/posts/<int:id>')
    def delete_post(id):
        try:
            post = Post.delete_one(id)
            return post, HTTPStatus.OK
        except TypeError:
            return {'message': 'Post inexistente.'}, HTTPStatus.NOT_FOUND


    @app.patch('/posts/<int:id>')
    def update_post(id):
        data = request.json
        
        if not data:
            return {'message': 'Sem dados a serem atualizados.'}, HTTPStatus.NOT_FOUND

        try:
            updated_post = Post.update_one(id, data)
            return updated_post, HTTPStatus.OK
        except TypeError:
            return {'message': 'Post inexistente.'}, HTTPStatus.NOT_FOUND
        except InvalidPostError:
            return {'message': 'Dados inválidos para atualização do post.'}, HTTPStatus.BAD_REQUEST
