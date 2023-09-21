class Game:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if isinstance(title, str) and 0 < len(title) and not hasattr(self, 'title'):
            self._title = title
        else:
            print("Not a valid title")
    
    title = property(get_title, set_title)

    def results(self):
      return [result for result in Result.all if result.game is self]
      
        # r_list = []
        # for result in Result.all:
        #     if isinstance(result, Result) and result.player == self:
        #         r_list.append(result)
        # return r_list
        

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        count = 0
        total_score = 0
        for result in self.results():
            if result.player is player:
                count += 1
                total_score += result.score
        if count == 0:
            return 0
        return total_score / count

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    
    def get_username(self):
        return self._username
    
    def set_username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
                self._username = username
        else:
            print("Not a valid username")
    
    username = property(get_username, set_username)
    
    def results(self):
        r_list = []
        for result in Result.all:
            if isinstance(result, Result) and result.player == self:
                r_list.append(result)
        return r_list

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
         return game in self.games_played()

    def num_times_played(self, game):
        games_played = [result.game for result in self.results()]
        return games_played.count(game)


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    def get_score(self):
        return self._score

    def set_score(self, score):
        if isinstance(score, int) and 1 <= (score) <= 5000 and not hasattr(self, "score"):
            self._score = score
        else:
            print("Not a valid score")

    
    def get_player(self):
        return self._player
    
    def set_player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            print("Not a valid player")

    def get_game(self):
        return self._game
    
    def set_game(self, game):
        if isinstance(game,Game):
            self._game = game
        else:
            print("Not a valid game")

    
    player = property(get_player, set_player)
    game = property(get_game, set_game)
    score = property(get_score, set_score)


new_game = Game("New Game")
game_1 = Game("Game 1")
game_2 = Game("Game 2")
terence = Player("Terence")
ryan = Player("Ryan")
kam = Player("Kam")

Result(terence ,new_game , 5000)
Result(ryan ,new_game , 5000)
Result(terence ,game_1 , 5000)
Result(ryan ,game_1 , 5000)
Result(kam ,game_2 , 5000)
Result(terence,game_1, 500)
