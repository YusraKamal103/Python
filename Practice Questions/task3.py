#2D array
LeagueSize=4
MatchNo=2

TeamName=["inter miami","manchester city","al nassr","real madrid"]
Teampoints=[

   [3,2],
   [0,1],
   [2,1],
   [3,0],

]

away=0
home=0
draw=0
lost=0

for i in range(LeagueSize):
    
    for j in range(MatchNo):
     totalpoints=sum  (Teampoints[j])
     print(TeamName)
     print(totalpoints)
    
 
