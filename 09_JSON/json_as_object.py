import json


class Show:

    def __init__(self, filepath):
        self.filepath = filepath
        show_info = self._open_json_show()
        self.title = show_info.get("Director")
        self.year = show_info.get("Release Year")
        self.seasons = show_info.get("No. of Seasons")
        self.ratings = show_info.get("Ratings")

    def _open_json_show(self) -> dict:
        with open(self.filepath) as show_file:
            return json.load(show_file)

    def get_average_rating(self) -> float:
       total = 0
       for rating in self.ratings.values():
        total += rating
       return total / len(self.ratings)


mr_robot = Show("show.json")
print(mr_robot.title)
print(mr_robot.year)
print(mr_robot.seasons)
print(mr_robot.get_average_rating())