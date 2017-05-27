import pandas as pd
import matplotlib.pyplot as plt

class PclassPlot(object):
    def __init__(self):
        self.df = pd.read_csv('./data.csv')

    def cleanData(self):
        self.df = self.df.drop(['Ticket','Cabin'], axis=1)
        self.df = self.df.dropna()

    def drawPclassSurvivors(self):
        fig = plt.figure(figsize=(18,4), dpi=120)
        alpha_level = 0.65
        ax1 = fig.add_subplot(141)
        Pclass1 = self.df.Survived[self.df.Pclass == 1].value_counts()
        Pclass1.plot(kind='bar', label='Pclass=1', color='#FA2479', alpha=alpha_level)
        ax1.set_xticklabels(["Survived", "Died"], rotation=0)
        ax1.set_xlim(-1, len(Pclass1))
        plt.title("Who Survived? with respect to Gender and Class"); plt.legend(loc='best')

        ax2 = fig.add_subplot(142, sharey=ax1)
        Pclass2 = self.df.Survived[self.df.Pclass == 2].value_counts()
        Pclass2.plot(kind='bar', label='Pclass=2', color='pink', alpha=alpha_level)
        ax2.set_xticklabels(["Died","Survived"], rotation=0)
        ax2.set_xlim(-1, len(Pclass2))
        plt.legend(loc='best')

        ax3 = fig.add_subplot(143, sharey=ax1)
        Pclass3 = self.df.Survived[self.df.Pclass == 3].value_counts()
        Pclass3.plot(kind='bar', label='Pclass=3',color='lightblue', alpha=alpha_level)
        ax3.set_xticklabels(["Died","Survived"], rotation=0)
        ax3.set_xlim(-1, len(Pclass3))
        plt.legend(loc='best')

        plt.savefig('./Pclass_result.png', dpi=120, format='png')

    def drawPclassAndSexPlot(self):
        fig = plt.figure(figsize=(12,6), dpi=120)
        alpha_level = 0.65

        ax1 = fig.add_subplot(231)
        female_3 = self.df.Survived[self.df.Sex == 'female'][self.df.Pclass == 3].value_counts()
        female_3.plot(kind='bar', label='female, Pclass=3', color='#FA2479', alpha=alpha_level)
        ax1.set_xticklabels(["Survived", "Died"], rotation=0)
        ax1.set_xlim(-1, len(female_3))
        plt.legend(loc='best')

        ax2 = fig.add_subplot(234)
        male_3 = self.df.Survived[self.df.Sex == 'male'][self.df.Pclass == 3].value_counts()
        male_3.plot(kind='bar', label='male, Pclass=3', color='steelblue', alpha=alpha_level)
        ax2.set_xticklabels(["Survived", "Died"], rotation=0)
        ax2.set_xlim(-1, len(male_3))
        plt.legend(loc='best')

        ax3 = fig.add_subplot(232)
        female_2 = self.df.Survived[self.df.Sex == 'female'][self.df.Pclass == 2].value_counts()
        female_2.plot(kind='bar', label='female, Pclass=2', color='pink', alpha=alpha_level)
        ax3.set_xticklabels(["Survived", "Died"], rotation=0)
        ax3.set_xlim(-1, len(female_2))
        plt.legend(loc='best')

        ax4 = fig.add_subplot(235)
        male_2 = self.df.Survived[self.df.Sex == 'male'][self.df.Pclass == 2].value_counts()
        male_2.plot(kind='bar', label='male, Pclass=2', color='lightblue', alpha=alpha_level)
        ax4.set_xticklabels(["Survived", "Died"], rotation=0)
        ax4.set_xlim(-1, len(male_2))
        plt.legend(loc='best')

        ax5 = fig.add_subplot(233)
        female_1 = self.df.Survived[self.df.Sex == 'female'][self.df.Pclass == 1].value_counts()
        female_1.plot(kind='bar', label='female, Pclass=1', color='red', alpha=alpha_level)
        ax5.set_xticklabels(["Survived", "Died"], rotation=0)
        ax5.set_xlim(-1, len(female_1))
        plt.legend(loc='best')

        ax6 = fig.add_subplot(236)
        male_1 = self.df.Survived[self.df.Sex == 'male'][self.df.Pclass == 1].value_counts()
        male_1.plot(kind='bar', label='male, Pclass=1', color='blue', alpha=alpha_level)
        ax6.set_xticklabels(["Survived", "Died"], rotation=0)
        ax6.set_xlim(-1, len(male_1))
        plt.legend(loc='best')

        plt.savefig('./Pclass_and_Sex_result.png', dpi=120, format='png')


if __name__ == '__main__':
    PclassDrawObj = PclassPlot()
    PclassDrawObj.cleanData()
    PclassDrawObj.drawPclassSurvivors()
    PclassDrawObj.drawPclassAndSexPlot()