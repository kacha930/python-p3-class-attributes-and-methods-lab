


class Song:
    # class attributes - it is the work of the class to know how many tracks are there.
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count={}
    
    def __init__(self, name, artist, genre):
        self.add_song_to_count()

        #  adds any new genres to a class attribute genres, a list. This list should contain only unique genres — no duplicates! 
        self.add_to_genres(genre)


        self.add_to_artists(artist)

        # adds to a class attribute genre_count, a dictionary in which the keys are the names of each genre. Each genre name key should point to a value that is the number of songs that have that genre.


        self.add_to_genre_count(genre)

        # creates a histogram similar to the one above, but for artists rather than genres.


        self.add_to_artist_count(artist)
        self.name = name
        self.artist = artist
        self.genre = genre
    

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
        
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] +=1
        else:
            cls.genre_count[genre] =1 
        
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist]  = 1  
        

