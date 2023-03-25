#Population migration distribution between two Indian states.

#2 indian states  - Bangalore ,Chennai 
#Can migrate to any one of the two Indian states 
#To pedict the migration distribution between 2 indian states 
import numpy as np
import random as rm

#encoding indian_state to numbers
indian_state = {
    0:"Bangalore",
    1:"Chennai",
}
indian_state  

#Transition Matrix
T= np.array([[0.2,0.8],[0.4,0.6]])

#Random Walk on Markov Chains

#when start_indian_state = 0  ,present location is Bangalore
#when start_indian_state = 1  ,present location is Chennai
for  start_indian_state in range(2):
    print("\nMigration Prediction of population staying in",indian_state[start_indian_state],"for next 5 times")
    n=6                #for next 5 predictions
    print(indian_state[start_indian_state],"--->",end=" ")                         
    prev_indian_state = start_indian_state       

    while n-1:                     #continue the loop for n-1 times, as we are starting fron current  indian_state we are staying
        curr_indian_state = np.random.choice([0,1],p=T[prev_indian_state])       #which indian_state population might migrate next by folling the transition probability (probabilty of going to indian_states bangalore or chennai from previous indian_state)
        print(indian_state[curr_indian_state],"--->",end=" ")
        prev_indian_state=curr_indian_state
        n-=1
    print("stop")


#A stationary distribution of a Markov chain is a probability distribution that remains unchanged in the Markov chain as time progresses.
steps = 10**5       #accuracy increses with number of steps,hence higher the number higher the accuracy
start_indian_state=0
pi=np.array([0,0])
pi[start_indian_state] = 1
prev_indian_state = start_indian_state

i=0
while i<steps:
    curr_indian_state=np.random.choice([0,1],p=T[prev_indian_state])
    pi[curr_indian_state]+=1
    prev_indian_state=curr_indian_state
    i+=1

ans=pi/steps
print("\nOverall Probabity of population migrating to Bangalore",ans[0],"\nOverall Probabity of population migrating to Chennai =",ans[1])


#                                       **********    thank you    **********




    









