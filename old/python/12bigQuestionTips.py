#!/usr/bin/python3

# Question example is in 12bigQuestion.txt

def main() -> None:
    # The 1D array TeamName[]
    # Add data to make it easier to understand
    # You do NOT Need to include this
    teamName: list = ["Sharks", "Lions", "Random"]
    # The 2D array TeamPoints[]
    teamPoints: list = [[3, 2, 0], [1, 1, 1], [2, 1, 1]]
    # League size initialisation
    leagueSize: int = len(teamName)
    # Match no initialisation
    matchNo: int = len(teamPoints[0])

    # Num of points initialisation
    # Start of inclusion
    awayWin: int = 3
    homeWin: int = 2
    drawnMatch: int = 1
    lostMatch: int = 0
    
    # Team stats dictionary
    teamStats: list = []

    for _ in range(leagueSize):
        teamStats.append({
            "totalPoints": 0,
            "awayWins": 0,
            "homeWin": 0,
            "drawnMatch": 0,
            "lostMatch": 0,
        })
    # First and Second requirement: calculate the total points of all matches, and the number of away wins, home matches, drawn matches and lost matches
    for i in range(leagueSize):
        for j in range(matchNo):
            points = teamPoints[i][j]
            teamStats[i]["totalPoints"] += points
            if points == awayWin:
                teamStats[i]["awayWins"] += 1
            elif points == homeWin:
                teamStats[i]["homeWin"] += 1
            elif points == drawnMatch:
                teamStats[i]["drawnMatch"] += 1
            else:
                teamStats[i]["lostMatch"] += 1

    # Fourth requirement: finding the lowest and highest amount of wins
    lowest = [(teamName[0], teamStats[0]["totalPoints"])]
    highest = [(teamName[0], teamStats[0]["totalPoints"])]

    for i in range(1, leagueSize):
        if teamStats[i]["totalPoints"] < lowest[0][1]:
            lowest = [(teamName[i], teamStats[i]["totalPoints"])]
        elif teamStats[i]["totalPoints"] == lowest[0][1]:
            lowest.append((teamName[i], teamStats[i]["totalPoints"]))
        
        if teamStats[i]["totalPoints"] > highest[0][1]:
            highest = [(teamName[i], teamStats[i]["totalPoints"])]
        elif teamStats[i]["totalPoints"] == highest[0][1]:
            highest.append((teamName[i], teamStats[i]["totalPoints"]))

    # Third requirement: Output
    for i in range(leagueSize):
        print(teamName[i])
        print("total points: ", teamStats[i]["totalPoints"])
        print("number of away wins: ", teamStats[i]["awayWins"])
        print("number of home wins: ",  teamStats[i]["homeWin"])
        print("number of drawn matches: ",  teamStats[i]["drawnMatch"])
        print("nunmber of lost matches: ",  teamStats[i]["lostMatch"])
        print()

    print(f"highest points team: {highest[0][0]} \nnumber of points: {highest[0][1]}")
    print(f"lowest points team: {lowest[0][0]} \nnumber of points: {lowest[0][1]}")

if __name__ == "__main__":
    main()

# Output

# > python3 12bigQuestionTips.py
# Sharks
# total points:  5
# number of away wins:  1
# number of home wins:  1
# number of drawn matches:  0
# nunmber of lost matches:  1
# 
# Lions
# total points:  3
# number of away wins:  0
# number of home wins:  0
# number of drawn matches:  3
# nunmber of lost matches:  0
# 
# Random
# total points:  4
# number of away wins:  0
# number of home wins:  1
# number of drawn matches:  2
# nunmber of lost matches:  0
# 
# highest points team: Sharks
# number of points: 5
# lowest points team: Lions
# number of points: 3
