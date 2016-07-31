from read_data import *


dataset = {}
activity_prob = {}
mood_prob = {"rad": 0, "good": 0, "meh": 0, "not great": 0, "awful": 0}

def naive_bayes(item):
    print item
    for mood_type in mood_prob.keys():
        
        prob = mood_prob[mood_type]
        if (prob != 0):
            for activity in item.get_activities():
                p = dataset[activity][mood_type]/float(dataset[activity]["total"])
                p *= activity_prob[activity] / float(mood_prob[mood_type])
                prob *= p
            print mood_type, prob
        else:
            print mood_type, 0

def train(data):
    total_activities = 0.0
    for entry in data:
        for activity in entry.get_activities():
            if activity not in dataset.keys():
                dataset[activity] = {"rad": 0, "good": 0, "meh": 0, "not great": 0, "awful": 0, "total": 0}
                activity_prob[activity] = 0
        
            dataset[activity][entry.get_mood()] += 1
            dataset[activity]["total"] += 1
            activity_prob[activity] += 1
            total_activities += 1
        mood_prob[entry.get_mood()] += 1
    
    for activity in activity_prob.keys():
        activity_prob[activity] /= total_activities

    total_entries = float(len(data))
    for mood in mood_prob.keys():
        mood_prob[mood] /= total_entries
    
    print dataset
    print
    print activity_prob
    print
    print mood_prob
   
entries = read_data(sys.argv[1])
inputs = read_data(sys.argv[2])


train(entries)    
for item in inputs:
    naive_bayes(item)
    
