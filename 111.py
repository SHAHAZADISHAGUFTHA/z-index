import csv
import pandas as pd
import plotly_express as px 
import statistics as st
import plotly.figure_factory as ff 
import random 
import plotly.graph_objects as go 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean = st.mean(data)
std = st.stdev(data)

def random_set_of_means(counter):
    dataset=[]
    for i in range (0,counter):
        random_index = []
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean
mean_list = []
for _i in range(0,1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)
standard_dev = st.stdev(mean_list)
mean_of_samples = st.mean(mean_list) 
print("Mean: ",mean_of_samples)
fig = ff.create_distplot([mean_list],["reading time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Reading time"))
SD1_start,SD1_end=mean_of_samples-standard_dev,mean_of_samples+standard_dev
SD2_start,SD2_end=mean_of_samples-(2*standard_dev),mean_of_samples+(2*standard_dev)
SD3_start,SD3_end=mean_of_samples-(3*standard_dev),mean_of_samples+(3*standard_dev)
list_of_data_1SD = [result for result in sum if result>SD1_start and result<SD1_end]
list_of_data_2SD = [result for result in sum if result>SD2_start and result<SD2_end]
list_of_data_3SD = [result for result in sum if result>SD3_start and result<SD3_end]
mean_of_data1SD = st.stdev(list_of_data1SD)
print("mean_of_data1SD:",mean_of_data1SD)
mean_of_data2SD = st.stdev(list_of_data2SD)
print("mean_of_data2SD:",mean_of_data2SD)
mean_of_data3SD = st.stdev(list_of_data3SD)
print("mean_of_data3SD:",mean_of_data3SD)

fig = ff.create_distplot([mean_list],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_of_data1SD,mean_of_data1SD],y=[0,0.17],mode="lines",name="Mean1"))
fig.add_trace(go.Scatter(x=[mean_of_data2SD,mean_of_data2SD],y=[0,0.17],mode="lines",name="Mean2"))
fig.add_trace(go.Scatter(x=[mean_of_data3SD,mean_of_data3SD],y=[0,0.17],mode="lines",name="Mean3"))
fig.show()