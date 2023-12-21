#Python Programming Assignment 2.1 - Submission date 09/19/2023
#Anasuya Sikdar

#Input scores from User
scoresInput = input('Please enter list of scores separated with commas: ')
#Each assignment of homework is worth 50 points
outofScore = 50

#Score variable represents each score as a string
#It is used to iterate over each element in the list using resulting from the split operatio
scoresList = [float(score) for score in scoresInput.split(', ')]

#To calculate the number of scores entered
scoresNum = len(scoresList)

#To determine the sum of all scores
scoresSum = sum(scoresList)

#To determine the lowest score
scoresLowest = min(scoresList)

if scoresNum == 1:
    #Special case when only one score is entered
    averagePercent = (scoresList[0]/50) * 100
    #Print output
    print('The average of ',scoresNum, ' scores is ',averagePercent,'%')
    print('The rounded average of ',scoresNum, ' scores is ',round(averagePercent),'%')
    print('The truncated average of ',scoresNum, ' scores is ',int(averagePercent),'%')
else:

    #To calculate the average homework percentage
    averagePercent = ((scoresSum - scoresLowest)/(scoresNum - 1))/50 * 100
    #Output of the Results
    print('The average of ',scoresNum - 1, ' scores is ',averagePercent,'%')
    print('The rounded average of ',scoresNum - 1, ' scores is ',round(averagePercent),'%')
    print('The truncated average of ',scoresNum - 1, ' scores is ',int(averagePercent),'%')





