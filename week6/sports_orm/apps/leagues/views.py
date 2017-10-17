from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {

		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(sport__startswith="base"),
		"womens_leagues": League.objects.filter(name__contains="women"),
		"hockey_leagues": League.objects.filter(sport__contains="hoc"),
		"non_football": League.objects.exclude(sport__startswith="foot"),
		"conferences": League.objects.filter(name__contains="conference"),
		"atlantic_region": Team.objects.filter(location__contains="Atl"),
		"dallas_teams": Team.objects.filter(location="Dallas"),
		"raptors":Team.objects.filter(team_name__contains="Raptor"),
		"cities": Team.objects.filter(location__contains="city"),
		"t_team": Team.objects.filter(team_name__startswith="T"),
		"by_loc": Team.objects.order_by("location"),
		"team_name": Team.objects.order_by("-team_name"),
		"all_coopers": Player.objects.filter(last_name__iexact="cooPeR"),
		"all_joshuas": Player.objects.filter(first_name__iexact="jOshUA"),
		"not_joshua_cooper": Player.objects.filter(last_name__exact="Cooper").exclude(first_name="Joshua"),
		"alexander_or_wyatt": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")