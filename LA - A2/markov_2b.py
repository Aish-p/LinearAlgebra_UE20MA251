#Vote changing pattern of Three Political parties from one election to the next.

#3 political parties - partyA , partyB , partyC
#Any one of the political parties can win the upcomming elections.
#Predicting which will be the next rulling party with each initial state being PartyA ,PartyB and PartyC
import numpy as np
import random as rm

#encoding state to numbers
state = {
    0:"partyA",
    1:"partyB",
    2:"partyC"
}
state  

#Transition Matrix
T= np.array([[0.2,0.5,0.3],[0.3,0.3,0.4],[0.4,0.5,0.1]])

#Random Walk on Markov Chains

#when start_state = 0 ,current ruling party is partyA   
#when start_state = 1 ,current ruling party is partyB     
#when start_state = 2 ,current ruling party is partyC
for  start_state in range(3):
    print("\nPrediction of rulling parties for next 5 elections when", state[start_state], "is the current rulling party:")  
    n=6            #for next 5 predictions
    print(state[start_state],"--->",end=" ")                           
    prev_state = start_state       #bcoz we have just visited start state

    while n-1:                     #continue the loop for n-1 times, as the first Election is already over
        curr_state = np.random.choice([0,1,2],p=T[prev_state])       #which state it is going next by folling the transition probability (probabilty of going to states 1,2,3 from previous state)
        
        print(state[curr_state],"--->",end=" ")
        prev_state=curr_state
        n-=1
    print("stop")

#A stationary distribution of a Markov chain is a probability distribution that remains unchanged in the Markov chain as time progresses.
steps = 10**5       #accuracy increses with number of steps,hence higher the number higher the accuracy
start_state=0
pi=np.array([0,0,0])
pi[start_state] = 1
prev_state = start_state

i=0
while i<steps:
    curr_state=np.random.choice([0,1,2],p=T[prev_state])
    pi[curr_state]+=1
    prev_state=curr_state
    i+=1

ans=pi/steps
print("\nOverall Probabity of partyA being the rulling party =",ans[0],"\nOverall Probabity of partyB being the rulling party =",ans[1],"\nOverall Probabity of partyC being the rulling party =",ans[2])


#  *******   Thank you    ********



    









