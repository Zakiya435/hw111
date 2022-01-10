import plotly.figure_factory as ff, statistics, random, pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()
population_mean = statistics.mean(data) 
print(population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([df],["average"],show_hist = False)
    first_std_start,first_std_end = mean - std, mean + std
    second_std_start,second_std_end = mean -(2*std), mean + (2*std)
    third_std_start,third_std_end = mean -(3*std), mean + (3*std)

    print("std1: ",first_std_start,first_std_end)
    print("std2: ",second_std_start,second_std_end)
    print("std3: ",third_std_start,third_std_end)

    
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

    fig.add_trace(go.Scatter(x=[first_std_start,first_std_start],y=[0,0.17],mode="lines",name="std1"))
    fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="std1"))

    fig.add_trace(go.Scatter(x=[second_std_start,second_std_start],y=[0,0.17],mode="lines",name="std2"))
    fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="std2"))
    
    fig.add_trace(go.Scatter(x=[third_std_start,third_std_start],y=[0,0.17],mode="lines",name="std3"))
    fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="std3"))
    fig.show()

    z_score = (mean-mean)/std
    print(z_score)
    

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("sampling mean:- ", statistics.mean(mean_list))

setup()