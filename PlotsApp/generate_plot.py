import matplotlib.pyplot as plt
import seaborn as sns
class KindsOfPlots:
    def __init__(self,x,y,charttype,file) -> None:
        self.x = x
        self.y = y
        self.file = file
        self.chart = charttype
    
    def line_scatter(self):
        return sns.relplot(data=self.file,x=self.x, y=self.y, hue=None, size=None, style=None, units=None, row=None, col=None, col_wrap=None, 
                           row_order=None, col_order=None, palette=None, hue_order=None, hue_norm=None, sizes=None, size_order=None, size_norm=None, markers=None, 
                           dashes=None, style_order=None, legend='auto', kind=self.chart, height=5, aspect=1, facet_kws=None)
    
    def other_than_line_scatter(self):
        return sns.catplot(data=self.file,x=self.x, y=self.y, hue=None, row=None, col=None, col_wrap=None, estimator='mean', errorbar=('ci', 95), 
                           n_boot=1000, units=None, seed=None, order=None, hue_order=None, row_order=None, col_order=None, height=5, aspect=1, 
                           kind=self.chart, native_scale=False, formatter=None, orient=None, color=None, palette=None, 
                           hue_norm=None, legend='auto', legend_out=True, sharex=True, sharey=True, margin_titles=False, facet_kws=None, ci='deprecated')
    




    
