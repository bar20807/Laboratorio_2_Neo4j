# -*-coding:utf-8 -*-
'''
@File    :   main.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188), Alejadro Gomez (20347) y Rodrigo Barrera (20807)
@Version :   1.0
@Desc    :   Creacion y carga de datos a Neo4j
'''

from py2neo import Graph, Node, Relationship

graph = Graph("neo4j+s://f4c961e7.databases.neo4j.io", auth=("neo4j", "rv9qlnIH1-vO9YEuuFQMpJEjz1aMSLcqNveDWxMMKVg"))

def create_user(name):
    return Node("User", name=name)

def create_movie(title):
    return Node("Movie", title=title)

def create_relationship(user, movie, rating):
    return Relationship(user, "RATED", movie, rating=rating)

def add_user_to_graph(graph, name):
    user = create_user(name)
    graph.create(user)

def add_movie_to_graph(graph, title):
    movie = create_movie(title)
    graph.create(movie)

def add_rating_to_graph(graph, user_name, movie_title, rating):
    user = create_user(user_name)
    movie = create_movie(movie_title)
    rating_rel = create_relationship(user, movie, rating)
    graph.create(rating_rel)

# Add some users, movies, and ratings to the graph
add_user_to_graph(graph, "Alice")
add_user_to_graph(graph, "Bob")
add_user_to_graph(graph, "Charlie")
add_user_to_graph(graph, "Dave")
add_user_to_graph(graph, "Eve")

add_movie_to_graph(graph, "The Matrix")
add_movie_to_graph(graph, "Inception")
add_movie_to_graph(graph, "The Godfather")
add_movie_to_graph(graph, "The Shawshank Redemption")
add_movie_to_graph(graph, "Pulp Fiction")

add_rating_to_graph(graph, "Alice", "The Matrix", 4)
add_rating_to_graph(graph, "Alice", "Inception", 5)
add_rating_to_graph(graph, "Bob", "The Godfather", 5)
add_rating_to_graph(graph, "Bob", "The Shawshank Redemption", 4)
add_rating_to_graph(graph, "Charlie", "The Matrix", 3)
add_rating_to_graph(graph, "Charlie", "The Shawshank Redemption", 5)
add_rating_to_graph(graph, "Dave", "Pulp Fiction", 4)
add_rating_to_graph(graph, "Eve", "Inception", 4)
add_rating_to_graph(graph, "Eve", "The Godfather", 3)