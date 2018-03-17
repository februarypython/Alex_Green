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
		"alexander_wyatt": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt"),
		"atlantic_soccer_teams": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"penguin_players": Player.objects.filter(curr_team__team_name="Penguins").filter(curr_team__location="Boston"),
		"icbc_players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"lopezes": Player.objects.filter(last_name="Lopez").filter(curr_team__league__name="American Conference of Amateur Football"),
		"all_football_players": Player.objects.filter(curr_team__league__sport="Football"),
		"teams_with_sophia": Player.objects.filter(first_name__contains="sophia"),
		"smooth_flores": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders").exclude(curr_team__location="Washington"),
		"samuel_evans": Player.objects.filter(first_name="Samuel").filter(last_name="Evans"),
		"all_tiger_cats": Player.objects.filter(all_teams__location="Manitoba").filter(all_teams__team_name="Tiger-Cats"),
		"some_vikings": Player.objects.filter(all_teams__location="Wichita").filter(all_teams__team_name="Vikings").exclude(curr_team__team_name__contains="Vikings"),
		"jacob_gray": Player.objects.filter(first_name="Jacob").filter(last_name="Gray"),
		"baseball_joshes": Player.objects.filter(first_name="Joshua").filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(200)
	team_maker.gen_players(200)

	return redirect("index")