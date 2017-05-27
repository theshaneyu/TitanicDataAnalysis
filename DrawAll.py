import pandas as pd
import matplotlib.pyplot as plt

class PclassPlot(object):
    def __init__(self):
        self.df = pd.read_csv('./data.csv')

    def cleanData(self):
        print(self.df)
        self.df = self.df.drop(['Ticket','Cabin'], axis=1)
        # Remove NaN values
        self.df = self.df.dropna()

    def drawAllPlot(self):
        # specifies the parameters of our graphs
        fig = plt.figure(figsize=(18,6), dpi=1600) 
        alpha = alpha_scatterplot = 0.2 
        alpha_bar_chart = 0.55

        # lets us plot many diffrent shaped graphs together 
        ax1 = plt.subplot2grid((2,3),(0,0))
        # plots a bar graph of those who surived vs those who did not.               
        self.df.Survived.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
        # this nicely sets the margins in matplotlib to deal with a recent bug 1.3.1
        ax1.set_xlim(-1, 2)
        # puts a title on our graph
        plt.title("Distribution of Survival, (1 = Survived)")    

        plt.subplot2grid((2,3),(0,1))
        plt.scatter(self.df.Survived, self.df.Age, alpha=alpha_scatterplot)
        # sets the y axis lable
        plt.ylabel("Age")
        # formats the grid line style of our graphs                          
        plt.grid(b=True, which='major', axis='y')  
        plt.title("Survival by Age,  (1 = Survived)")

        ax3 = plt.subplot2grid((2,3),(0,2))
        self.df.Pclass.value_counts().plot(kind="barh", alpha=alpha_bar_chart)
        ax3.set_ylim(-1, len(self.df.Pclass.value_counts()))
        plt.title("Class Distribution")

        plt.subplot2grid((2,3),(1,0), colspan=2)
        # plots a kernel density estimate of the subset of the 1st class passangers's age
        self.df.Age[self.df.Pclass == 1].plot(kind='kde')    
        self.df.Age[self.df.Pclass == 2].plot(kind='kde')
        self.df.Age[self.df.Pclass == 3].plot(kind='kde')
        # plots an axis lable
        plt.xlabel("Age")    
        plt.title("Age Distribution within classes")
        # sets our legend for our graph.
        plt.legend(('1st Class', '2nd Class','3rd Class'),loc='best') 

        ax5 = plt.subplot2grid((2,3),(1,2))
        self.df.Embarked.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
        ax5.set_xlim(-1, len(self.df.Embarked.value_counts()))
        # specifies the parameters of our graphs
        plt.title("Passengers per boarding location")

        plt.savefig('./result.png', dpi=1600, format='png')

    def drawPclassSurvivors(self):
        fig = plt.figure(figsize=(18,4), dpi=1600)
        alpha_level = 0.65
        ax1 = fig.add_subplot(141)
        Pclass1 = self.df.Survived[self.df.Pclass == 1].value_counts()
        Pclass1.plot(kind='bar', label='Pclass1', color='#FA2479', alpha=alpha_level)
        ax1.set_xticklabels(["Survived", "Died"], rotation=0)
        ax1.set_xlim(-1, len(Pclass1))
        plt.title("Who Survived? with respect to Gender and Class"); plt.legend(loc='best')

        ax2 = fig.add_subplot(142, sharey=ax1)
        Pclass2 = self.df.Survived[self.df.Pclass == 2].value_counts()
        Pclass2.plot(kind='bar', label='Pclass2', color='pink', alpha=alpha_level)
        ax2.set_xticklabels(["Died","Survived"], rotation=0)
        ax2.set_xlim(-1, len(Pclass2))
        plt.legend(loc='best')

        ax3 = fig.add_subplot(143, sharey=ax1)
        Pclass3 = self.df.Survived[self.df.Pclass == 3].value_counts()
        Pclass3.plot(kind='bar', label='Pclass3',color='lightblue', alpha=alpha_level)
        ax3.set_xticklabels(["Died","Survived"], rotation=0)
        ax3.set_xlim(-1, len(Pclass3))
        plt.legend(loc='best')

        plt.savefig('./Pclass_result.png', dpi=1600, format='png')

    def drawPclassAndSexPlot(self):
        fig = plt.figure(figsize=(18,4), dpi=1600)
        alpha_level = 0.65
        ax1=fig.add_subplot(141)
        female_highclass = self.df.Survived[self.df.Sex == 'female'][self.df.Pclass != 3].value_counts()
        female_highclass.plot(kind='bar', label='female, highclass', color='#FA2479', alpha=alpha_level)
        ax1.set_xticklabels(["Survived", "Died"], rotation=0)
        ax1.set_xlim(-1, len(female_highclass))
        plt.title("Who Survived? with respect to Gender and Class"); plt.legend(loc='best')

        ax2=fig.add_subplot(142, sharey=ax1)
        female_lowclass = self.df.Survived[self.df.Sex == 'female'][self.df.Pclass == 3].value_counts()
        female_lowclass.plot(kind='bar', label='female, low class', color='pink', alpha=alpha_level)
        ax2.set_xticklabels(["Died","Survived"], rotation=0)
        ax2.set_xlim(-1, len(female_lowclass))
        plt.legend(loc='best')

        ax3=fig.add_subplot(143, sharey=ax1)
        male_lowclass = self.df.Survived[self.df.Sex == 'male'][self.df.Pclass == 3].value_counts()
        male_lowclass.plot(kind='bar', label='male, low class',color='lightblue', alpha=alpha_level)
        ax3.set_xticklabels(["Died","Survived"], rotation=0)
        ax3.set_xlim(-1, len(male_lowclass))
        plt.legend(loc='best')

        ax4=fig.add_subplot(144, sharey=ax1)
        male_highclass = self.df.Survived[self.df.Sex == 'male'][self.df.Pclass != 3].value_counts()
        male_highclass.plot(kind='bar', label='male, highclass', alpha=alpha_level, color='steelblue')
        ax4.set_xticklabels(["Died","Survived"], rotation=0)
        ax4.set_xlim(-1, len(male_highclass))
        plt.legend(loc='best')

        plt.savefig('./Pclass_and_Sex_result.png', dpi=1600, format='png')


                


if __name__ == '__main__':
    PclassDrawObj = PclassPlot()
    PclassDrawObj.cleanData()
    # PclassDrawObj.drawAllPlot()
    PclassDrawObj.drawPclassSurvivors()
    PclassDrawObj.drawPclassAndSexPlot()