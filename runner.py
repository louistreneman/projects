from bs4 import BeautifulSoup
import json
import requests

url = "https://www.bbc.co.uk/sport/rugby-union/scores-fixtures/2025-01-31"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

html_table = "[{\"id\":\"EVP4447446\",\"startDateTime\":\"2025-01-31T20:15:00.000+00:00\",\"date\":\"Fri 31 Jan 2025\",\"status\":\"PostEvent\",\"period\":\"FT\",\"periodLabel\":{\"value\":\"FT\",\"accessible\":\"Full Time\"},\"groupedActions\":[{\"groupName\":{\"fullName\":\"Tries\",\"shortName\":\"TRIES\"},\"homeTeamActions\":[\"Attissogbe (2)\",\"Bielle-Biarrey (2)\",\"Marchand\",\"Gailleton\",\"Alldritt\"],\"awayTeamActions\":[]},{\"groupName\":{\"fullName\":\"Conversions\",\"shortName\":\"CONS\"},\"homeTeamActions\":[\"Ramos (4)\"],\"awayTeamActions\":[]}],\"tournament\":{\"id\":\"TOP480\",\"name\":\"Six Nations\",\"urn\":\"urn:bbc:sportsdata:rugby-union:tournament:six-nations\"},\"home\":{\"id\":\"TMP73743\",\"fullName\":\"France\",\"shortName\":\"France\",\"urn\":\"urn:bbc:sportsdata:rugby-union:team:france\",\"runningScores\":{\"halftime\":\"28\",\"fulltime\":\"43\"},\"score\":\"43\",\"actions\":{\"tries\":[{\"player\":{\"id\":\"PP1432389\",\"abbreviatedName\":\"Attissogbe\",\"fullName\":\"Theo Attissogbe\",\"shirtNumber\":14,\"starter\":true},\"minutesElapsed\":18,\"runningScore\":{\"home\":5,\"away\":0},\"isGolden\":false},{\"player\":{\"id\":\"PP1290807\",\"abbreviatedName\":\"Bielle-Biarrey\",\"fullName\":\"Louis Bielle-Biarrey\",\"shirtNumber\":11,\"starter\":true},\"minutesElapsed\":23,\"runningScore\":{\"home\":12,\"away\":0},\"isGolden\":false},{\"player\":{\"id\":\"PP1432389\",\"abbreviatedName\":\"Attissogbe\",\"fullName\":\"Theo Attissogbe\",\"shirtNumber\":14,\"starter\":true},\"minutesElapsed\":34,\"runningScore\":{\"home\":19,\"away\":0},\"isGolden\":false},{\"player\":{\"id\":\"PP1290807\",\"abbreviatedName\":\"Bielle-Biarrey\",\"fullName\":\"Louis Bielle-Biarrey\",\"shirtNumber\":11,\"starter\":true},\"minutesElapsed\":40,\"runningScore\":{\"home\":26,\"away\":0},\"isGolden\":false},{\"player\":{\"id\":\"PP710806\",\"abbreviatedName\":\"Marchand\",\"fullName\":\"Julien Marchand\",\"shirtNumber\":16,\"starter\":false},\"minutesElapsed\":55,\"runningScore\":{\"home\":33,\"away\":0},\"isGolden\":false},{\"player\":{\"id\":\"PP1401073\",\"abbreviatedName\":\"Gailleton\",\"fullName\":\"Emilien Gailleton\",\"shirtNumber\":23,\"starter\":false},\"minutesElapsed\":68,\"runningScore\":{\"home\":38,\"away\":0},\"isGolden\":false},{\"player\":{\"id\":\"PP899691\",\"abbreviatedName\":\"Alldritt\",\"fullName\":\"Gregory Alldritt\",\"shirtNumber\":8,\"starter\":true},\"minutesElapsed\":78,\"runningScore\":{\"home\":43,\"away\":0},\"isGolden\":false}],\"penaltyTries\":[],\"conversions\":[{\"player\":{\"id\":\"PP735779\",\"abbreviatedName\":\"Ramos\",\"fullName\":\"Thomas Ramos\",\"shirtNumber\":15,\"starter\":true},\"minutesElapsed\":19,\"runningScore\":{\"home\":7,\"away\":0}},{\"player\":{\"id\":\"PP735779\",\"abbreviatedName\":\"Ramos\",\"fullName\":\"Thomas Ramos\",\"shirtNumber\":15,\"starter\":true},\"minutesElapsed\":24,\"runningScore\":{\"home\":14,\"away\":0}},{\"player\":{\"id\":\"PP735779\",\"abbreviatedName\":\"Ramos\",\"fullName\":\"Thomas Ramos\",\"shirtNumber\":15,\"starter\":true},\"minutesElapsed\":35,\"runningScore\":{\"home\":21,\"away\":0}},{\"player\":{\"id\":\"PP735779\",\"abbreviatedName\":\"Ramos\",\"fullName\":\"Thomas Ramos\",\"shirtNumber\":15,\"starter\":true},\"minutesElapsed\":40,\"runningScore\":{\"home\":28,\"away\":0}}],\"penalties\":[],\"dropGoals\":[],\"penaltiesSummary\":[],\"triesSummary\":[\"Attissogbe (2)\",\"Bielle-Biarrey (2)\",\"Marchand\",\"Gailleton\",\"Alldritt\"],\"conversionsSummary\":[\"Ramos (4)\"],\"dropGoalsSummary\":[]}},\"away\":{\"id\":\"TMP73740\",\"fullName\":\"Wales\",\"shortName\":\"Wales\",\"urn\":\"urn:bbc:sportsdata:rugby-union:team:wales\",\"runningScores\":{\"halftime\":\"0\",\"fulltime\":\"0\"},\"score\":\"0\",\"actions\":{\"tries\":[],\"penaltyTries\":[],\"conversions\":[],\"penalties\":[],\"dropGoals\":[],\"penaltiesSummary\":[],\"triesSummary\":[],\"conversionsSummary\":[],\"dropGoalsSummary\":[]}},\"time\":{\"accessibleTime\":\"20:15\",\"displayTimeUK\":\"20:15\"},\"venue\":{\"name\":\"Stade de France\"},\"tournamentDescriptionLabel\":\"Six Nations\",\"eventGroupingLabel\":\"Six Nations\",\"sport\":\"rugby-union\",\"accessibleEventSummary\":\"France 43, Wales 0 at full time, France win 43 - 0\",\"pageTitleAccessibleText\":\"France vs Wales\",\"onwardJourneyLink\":\"https://www.bbc.co.uk/sport/rugby-union/match/EVP4447446\"}]"
