# -*-coding:utf-8 -*-
'''
@File    :   main.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188), Alejadro Gomez (20347) y Rodrigo Barrera (20807)
@Version :   1.0
@Desc    :   Creacion y carga de datos a Neo4j
'''

from py2neo import Graph, Node, Relationship

graph = Graph("neo4j+s://4191abc9.databases.neo4j.io", auth=("neo4j", "kfoop9SX8490ifTOARQKazVVTJ_4iAcIJS7zD8lk6_0"))


def add_user(graph, name, userID):
    user = Node("User", name=name, userID=userID)
    graph.create(user)

def add_movie(graph, title, movieID, year, plot):
    movie = Node("Movie", title=title, movieID=movieID, year=year, plot=plot)
    graph.create(movie)

def add_rating(graph, user_id, movie_id, rating, timestamp):
    user = Node("User", userID=user_id)
    movie = Node("Movie", movieID=movie_id)
    rated = Relationship(user, "RATED", movie, rating=rating, timestamp=timestamp)
    graph.create(rated)

# Se agregan usuarios, peliculas y sus respectivos ratings a la instancia de Neo4j
add_user(graph, "Alice", "1")
add_user(graph, "Bob", "2")
add_user(graph, "Charlie", "3")
add_user(graph, "Dave", "4")
add_user(graph, "Eve", "5")

add_movie(graph, "The Matrix", 1, 1999, "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.")
add_movie(graph, "Inception", 2, 2010, "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.")
add_movie(graph, "The Godfather", 3, 1972, "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.")
add_movie(graph, "The Shawshank Redemption", 4, 1994, "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.")
add_movie(graph, "Pulp Fiction", 5, 1994, "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.")

add_rating(graph, "1", 1, 4, 1649862000)
add_rating(graph, "1", 2, 5, 1649862000)
add_rating(graph, "2", 3, 5, 1649862000)
add_rating(graph, "2", 4, 4, 1649862000)
add_rating(graph, "3", 1, 3, 1649862000)
add_rating(graph, "3", 4, 5, 1649862000)
add_rating(graph, "4", 5, 4, 1649862000)
add_rating(graph, "5", 2, 4, 1649862000)
add_rating(graph, "5", 3, 3, 1649862000)