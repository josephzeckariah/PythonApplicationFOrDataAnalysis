####################################################################################################################################################################
from numpy import number
import pandas as pd
import matplotlib.pyplot as plt
##################################################################################


pd.set_option('display.max_columns', None)

MainTable_file_path = r"C:\Users\marco\OneDrive\المستندات\Data sets\DEPI datasets\Datasets\HR\Employee.csv"
Performance_file_path = r"C:\Users\marco\OneDrive\المستندات\Data sets\DEPI datasets\Datasets\HR\PerformanceRating.csv"


MainTable = pd.read_csv(MainTable_file_path)
PerformanceTable = pd.read_csv(Performance_file_path)



finalMergedTable = pd.merge(MainTable, PerformanceTable, on='EmployeeID', how='left')
finalMergedTable['ReviewDate'] = pd.to_datetime(finalMergedTable['ReviewDate'])



#####################################################################     additional columns
def AddAgeGroupToTable():
    def age_group(age): 

        if age < 20:
            return '0-20'
        elif age < 30:
            return '20-30'
        elif age < 40:
            return '30-40'
        elif age < 50:
            return '40-50'
        elif age < 60:
            return '50-60'
        else:
            return '60+'

    for index in range(finalMergedTable.index.max()):
        finalMergedTable.loc[index, 'Age group'] = age_group( finalMergedTable.loc[index, 'Age'])


def AddSalaryClassificationColumnToTable():
    def SalaryClassification(salary): 

        if salary < 30000:
            return '0-30k'
        elif salary < 50000:
            return '30k-50k'
        elif salary < 100000:
            return '50k-100k'
        elif salary < 200000:
            return '100k-200k'
        else:
            return '200k+'

    for index in range(finalMergedTable.index.max()):
        finalMergedTable.loc[index, 'Salary group'] = SalaryClassification( finalMergedTable.loc[index, 'Salary'])

AddAgeGroupToTable()
AddSalaryClassificationColumnToTable()

################################################################################## peformance change over years

def ShowPerformanceChangeAnalysis(finalMergedTable):
    ###########################################################___________base function
    def PlotAverageVerticalColumnWithHorizontal(finalMergedTable  ,  HorizontalValueToGroupBy  ,  VerticalAverageValue):
        x=0
        while x < 5:
            print(',')
            x+=1

       
        grouped_data = finalMergedTable.groupby(HorizontalValueToGroupBy) [VerticalAverageValue].mean()

        print(VerticalAverageValue,' ','first year :' ,grouped_data.iloc[0] ,'last year :' , grouped_data.iloc[-1] , 'difference is ' , grouped_data.iloc[-1]- grouped_data.iloc[0])

        plt.figure(figsize=(10, 5))
        grouped_data.plot(kind='bar', color='skyblue')
        plt.title(VerticalAverageValue)
        plt.ylim(0, 5)
        plt.xticks(rotation=0)
     ##################################
    finalMergedTable['ReviewDate'] = finalMergedTable['ReviewDate'].dt.year


    finalMergedTable = finalMergedTable.sort_values(by='ReviewDate')
 
    

    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'ReviewDate','JobSatisfaction')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'ReviewDate','EnvironmentSatisfaction')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'ReviewDate','RelationshipSatisfaction')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'ReviewDate','WorkLifeBalance')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'ReviewDate','SelfRating')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'ReviewDate','ManagerRating')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'ReviewDate','TrainingOpportunitiesWithinYear')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'ReviewDate','TrainingOpportunitiesTaken')

    plt.show()
#ShowPerformanceChangeAnalysis(finalMergedTable)   
  
'''##################################################################################


def PlotEmployeePropertiesToPerformance(finalMergedTable):
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'Gender','JobSatisfaction')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'Gender','EnvironmentSatisfaction')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'Gender','RelationshipSatisfaction')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'Gender','WorkLifeBalance')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'Gender','SelfRating')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'Gender','ManagerRating')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'Gender','TrainingOpportunitiesWithinYear')
    PlotAverageVerticalColumnWithHorizontal(finalMergedTable,'Gender','TrainingOpportunitiesTaken')

    plt.show()

#PlotEmployeePropertiesToPerformance(finalMergedTable)'''

###################################################################################      properties relation to performance

def PlotAllPropertiesRelationValuesOneAfterAnother():
    ######################################################################################################
    def PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable  ,  HorizontalValueToGroupBy  , listOfVerticalAverageValue):
        ######################################################################################figure out layout dimensions
        def closest_factor_pair(n):
            best_pair = (1, n)  # Default pair
            min_difference = n - 1  # Start with the largest possible difference
    
            for i in range(1, int(n**0.5) + 1):  # Iterate up to sqrt(n)
                 if n % i == 0:  # Check if i is a factor
                    pair = (i, n // i)  # Factor pair
                    difference = abs(pair[0] - pair[1])  # How close they are
            
            # Update if this pair is closer in size
                    if difference < min_difference:
                        best_pair = pair
                        min_difference = difference
    
            return best_pair# helper mithods
        ################################################################
        def MakeASingleGraphAmidMultipleGraphs(PositionOfGraph,VerticalValueOfGraph):
                    grouped_data = thisyearonlyvalues.groupby(HorizontalValueToGroupBy) [VerticalValueOfGraph].mean() 
                    
                    grouped_data.plot(kind='bar', color='skyblue', ax=ax [PositionOfGraph])

                    ax[PositionOfGraph].set_title(VerticalValueOfGraph)
                    ax[PositionOfGraph].set_ylim(0, 5)
                    ax[PositionOfGraph].tick_params(axis='x', rotation=0)
                    ax[PositionOfGraph].xaxis.label.set_visible(False)
                    manager = plt.get_current_fig_manager()
                    manager.window.state('zoomed') 

        ################################################################################################################################# SupFunction end




        numberOfTables = len(listOfVerticalAverageValue)
        dimensionsOfWindow = closest_factor_pair(numberOfTables)      
        thisyearonlyvalues = finalMergedTable[finalMergedTable['ReviewDate'].dt.year == 2022]
        
        ################################################
        if (dimensionsOfWindow ==(1,1)):
           
           grouped_data = thisyearonlyvalues.groupby(HorizontalValueToGroupBy) [listOfVerticalAverageValue[0]].mean()

           plt.figure(figsize=(10, 5))
           grouped_data.plot(kind='bar', color='skyblue')
           plt.title(listOfVerticalAverageValue[0])
           plt.ylim(0, 5)
           plt.xticks(rotation=0)
           plt.show()


        ###############################################
        elif (dimensionsOfWindow[0] ==1 or dimensionsOfWindow[1] == 1):
            fig, ax = plt.subplots(dimensionsOfWindow[0], dimensionsOfWindow[1], figsize=(30, 14))

            if dimensionsOfWindow[0] == 1:
                for i in range(dimensionsOfWindow[1]): 
                    MakeASingleGraphAmidMultipleGraphs(i,listOfVerticalAverageValue[i])

                plt.tight_layout()
                plt.show()

            elif dimensionsOfWindow[1] == 1:
                for i in range(dimensionsOfWindow[0]):
                    MakeASingleGraphAmidMultipleGraphs(i,listOfVerticalAverageValue[i])

                plt.tight_layout()
                plt.show()       


        ##############################################
        else:
            fig, ax = plt.subplots(dimensionsOfWindow[0], dimensionsOfWindow[1], figsize=(30, 14))
            fig.suptitle(HorizontalValueToGroupBy+ " effect on performance", fontsize=16, fontweight="bold")

            currenttableindex =0
            for x in range(dimensionsOfWindow[0]):
                for y in range(dimensionsOfWindow[1]): 

                    MakeASingleGraphAmidMultipleGraphs((x,y),listOfVerticalAverageValue[currenttableindex])                         
                    currenttableindex +=1

            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.show()

        ##################################################################################################

    #############################################################--------------------- base function



    
    listOFRatingValues = ['JobSatisfaction','EnvironmentSatisfaction','RelationshipSatisfaction'
                      ,'WorkLifeBalance','SelfRating','ManagerRating','TrainingOpportunitiesWithinYear','TrainingOpportunitiesTaken']


    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'Gender',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'Age group',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'Salary group',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'Ethnicity',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'MaritalStatus',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'Education',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'EducationField',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'BusinessTravel',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'OverTime',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'StockOptionLevel',listOFRatingValues)
    PlotAverageVerticalColumnWithHorizontalInOneWindow(finalMergedTable,'Attrition',listOFRatingValues)

PlotAllPropertiesRelationValuesOneAfterAnother()

####################################