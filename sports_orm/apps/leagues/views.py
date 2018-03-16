from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"baseball_leagues": League.objects.filter(sport__contains="baseball"),
		"womens_leagues": League.objects.filter(name__contains="women"),
		"hockey_leagues": League.objects.filter(sport__contains="hockey"),
		"non_football_league": League.objects.exclude(sport__contains="football"),
		"conference_leagues": League.objects.filter(name__contains="conference"),
		"atlantic_leagues": League.objects.filter(name__contains="atlantic"),
		"dallas_teams": Team.objects.filter(location="Dallas"),
		"raptors": Team.objects.filter(team_name__contains="raptors"),
		"city_teams": Team.objects.filter(location__contains="city"),
		"t_teams": Team.objects.filter(team_name__startswith="t"),
		"all_teams": Team.objects.order_by('location'),
		"reverse_teams": Team.objects.order_by('-team_name'),
		"coopers": Player.objects.filter(last_name="Cooper"),
		"joshuas": Player.objects.filter(first_name="Joshua"),
		"no_josh_coopers": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexander_wyatt": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(200)
	team_maker.gen_players(200)

	return redirect("index")