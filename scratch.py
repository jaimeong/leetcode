import random

ppl = { "Albert":2, "Evan": 1, "Henry": 1,  "Jimmy":2, "Johnny":1}
# schedule = {"Albert":[0,0,0,0], "Evan" : [0,0,0,0], "Henry": [0,0,0,0], 
# "Jimmy": [0,0,0,0], "Johnny": [0,0,0,0]}

# for each in ppl:
#     print("For " + each)
#     for i in range(ppl[each]):
#         if random.choice(list(ppl.keys())

Week 1:
Albert: Evan, Johnny 
Evan: Albert 
Henry: Jimmy 
Jimmy: Henry, 
Johnny: Albert

# schedule = {
# "Albert":[1,1,0,0,1], 
# "Evan" : [1,1,0,0,0], 
# "Henry": [0,0,1,1,0], 
# "Jimmy": [0,0,1,1,0], 
# "Johnny":[1,0,0,0,1]
# }


Week 2:
Albert: Henry
Evan: Jimmy
Henry: Albert 
Jimmy: Johnny, Evan
Johnny: Jimmy 

# schedule = {
# "Albert":[1,1,1,0,1], 
# "Evan" : [1,1,0,1,0], 
# "Henry": [1,0,1,1,0], 
# "Jimmy": [0,1,1,1,1], 
# "Johnny":[1,0,0,1,1]
# }


Week 3:
Albert: Jimmy
Evan: Johnny
Henry: None
Jimmy: Albert
Johnny: Evan

# schedule = {
# "Albert":[1,1,1,1,1], 
# "Evan" : [1,1,0,1,1], 
# "Henry": [1,0,1,1,0], 
# "Jimmy": [1,1,1,1,1], 
# "Johnny":[1,1,0,1,1]
# }

Week 4: 
Albert: Jimmy, Johnny
Evan: Henry
Henry: Evan
Jimmy: Albert
Johnny: Johnny

# schedule = {
# "Albert":[1,1,1,2,2], 
# "Evan" : [1,1,1,1,1], 
# "Henry": [1,1,1,1,0], 
# "Jimmy": [2,1,1,1,1], 
# "Johnny":[2,1,0,1,1]
# }

Week 5: 
Albert: 
Evan: 
Henry: Johnny
Jimmy: 
Johnny: Henry

# schedule = {
# "Albert":[1,1,1,2,2], 
# "Evan" : [1,1,1,1,1], 
# "Henry": [1,1,1,1,1], 
# "Jimmy": [2,1,1,1,1], 
# "Johnny":[2,1,1,1,1]
# }