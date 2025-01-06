import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

important_columns = ['DEPRESSIONINDEX', 'DEPEPISODE', 'MDELASTYR', 'ANYTXRXMDE', 'CATAG2', 'CATAG3', 'CATAG7', 'IRSEX', 'NEWRACE2', 'ANYINDEX', 'MJANDCOKE', 'ILLICITDRUGUSE', 'LSYRILLICIT', 'COKECRACK', 'OTHERILLICIT', 'MARJLTYR', 'MJCOKELY', 'COCCRKLY', 'MJGT12MO', 'COCGT12MO', 'ANYGT12MO', 'ALCFMFPB', 'IREDUC2', 'EDU_DUMMY', 'INCOME', 'INCOME_R', 'POVERTY', 'IRPRVHLT', 'WORKFORCE', 'EMPSTAT4', 'REVERSEPOP', 'MOVESPY2', 'CACHAR', 'CATYPE', 'CRIMEHIST', 'ANYSDRUG', 'ANYATTACK', 'ANYTHEFT', 'NUMARREST', 'HEALTH2', 'SCHDSICK', 'SCHDSKIP', 'TXLCAD', 'DSTNCALM', 'DSTTIRE', 'DSTSITST', 'DSTDEPRS', 'DSTCHEER', 'DSTNRVOS', 'IRMARIT', 'NOMARR2', 'RKIDSHH', 'MARRIED', 'CHILDRENINHOME']

def main():
    df = pd.read_csv('./data/27521-0001-Data.tsv', sep='\t')
    df_age_analysis = df[important_columns]

    corrmat = df_age_analysis.corr()
    corrmat_high = corrmat[abs(corrmat['DEPRESSIONINDEX']) > 0.7]
    f, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(corrmat_high, square=True)
    plt.show()

if __name__ == "__main__":
    main()

