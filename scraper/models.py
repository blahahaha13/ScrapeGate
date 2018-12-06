from django.db import models

# Create your models here

class Passing(models.Model):
  name = 'Passing'
  rk = models.IntegerField()
  team = models.CharField(max_length=25)
  att = models.IntegerField()
  comp = models.IntegerField()
  pct = models.FloatField()
  yds = models.IntegerField()
  ydsa = models.FloatField()
  longest = models.IntegerField()
  td = models.IntegerField()
  inter = models.IntegerField()
  sack = models.IntegerField()
  ydls = models.IntegerField()
  rate = models.FloatField()
  ydsg = models.IntegerField()

  def __str__(self):
    return self.name

class Receiving(models.Model):
  name = 'receiving'
  rank = models.IntegerField()
  team = models.CharField(max_length=25)
  receptions = models.IntegerField()
  yards = models.IntegerField()
  average = models.FloatField()
  longest = models.IntegerField()
  total_touchdowns = models.IntegerField()
  yards_per_game = models.FloatField()
  fumbles = models.IntegerField()
  fumbles_lost = models.IntegerField()

  def __str__(self):
    return self.name

class Rushing(models.Model):
  name = 'rushing'
  rank = models.IntegerField()
  team = models.CharField(max_length=25)
  attempts = models.IntegerField()
  yards = models.IntegerField()
  yards_per_attempt = models.FloatField()
  longest = models.IntegerField()
  total_touchdowns = models.IntegerField()
  yards_per_game = models.FloatField()
  fumbles = models.IntegerField()
  fumbles_lost = models.IntegerField()

  def __str__(self):
    return self.name

class Punting(models.Model):
  name = 'punting'
  rank = models.IntegerField()
  team = models.CharField(max_length=25)
  punts = models.IntegerField()
  yards = models.IntegerField()
  longest = models.IntegerField()
  average = models.FloatField()
  net_yards_average = models.FloatField()
  blocked_punts = models.IntegerField()
  number_of_times_pinned = models.IntegerField()
  touchbacks = models.IntegerField()
  fair_catches = models.IntegerField()
  punts_returned = models.IntegerField()
  punt_return_yardage_total = models.IntegerField()
  punt_return_yardage_average = models.FloatField()

  def __str__(self):
    return self.name

class Defense(models.Model):
  name = 'Defense'
  rk = models.IntegerField()
  team = models.CharField(max_length=25)
  solo_tackles = models.IntegerField()
  assisted_tackles = models.IntegerField()
  total_tackles = models.IntegerField()
  sacks = models.FloatField()
  yards_lost_per_sack = models.IntegerField()
  passes_defensed = models.IntegerField()
  interceptions = models.IntegerField()
  interception_return_yardage = models.IntegerField()
  longest_interception_return = models.IntegerField()
  interception_return_touchdowns = models.IntegerField()
  forced_fumbles = models.IntegerField()
  fumbles_recovered = models.IntegerField()
  fumbles_returned_for_touchdowns = models.IntegerField()

  def __str__(self):
    return self.name

class Kicking(models.Model):
  name = 'kicking'
  rank = models.IntegerField()
  team = models.CharField(max_length=25)
  field_goals_made = models.IntegerField()
  field_goals_attempted = models.IntegerField()
  field_goal_percentage = models.FloatField()
  longest = models.IntegerField()
  under_20 = models.IntegerField()
  twenty_to_twentynine = models.IntegerField()
  thirty_to_thirtynine = models.IntegerField()
  forty_to_fortynine = models.IntegerField()
  over_50 = models.IntegerField()
  extra_points_made = models.IntegerField()
  extra_points_attempted = models.IntegerField()
  extra_point_percentage = models.FloatField()

  def __str__(self):
    return self.name

class Turnovers(models.Model):
  name = 'Turnovers'
  rank = models.IntegerField()
  team = models.CharField(max_length=25)
  interceptions_takeaways = models.IntegerField()
  fumbles_takeaways = models.IntegerField()
  total_turnovers_takeaways = models.IntegerField()
  interceptions_givaways = models.IntegerField()
  fumbles_givaways = models.IntegerField()
  total_turnovers_givaways = models.IntegerField()
  difference = models.IntegerField()

  def __str__(self):
    return self.name

class Returning(models.Model):
  name = 'returning'
  rank = models.IntegerField()
  team = models.CharField(max_length=25)
  attempts_kickoffs = models.IntegerField()
  yards_kickoffs = models.IntegerField()
  average_kickoffs = models.FloatField()
  longest_kickoffs = models.IntegerField()
  touchdowns_kickoffs = models.IntegerField()
  attempts_punts = models.IntegerField()
  yards_punts = models.IntegerField()
  average_punts = models.FloatField()
  longest_punts = models.IntegerField()
  touchdowns_punts = models.IntegerField()
  fair_catches = models.IntegerField()

  def __str__(self):
    return self.name