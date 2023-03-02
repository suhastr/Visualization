import matplotlib.pyplot as plt
import seaborn as sns
class KindsOfPlots:
    def __init__(self,dataset) -> None:
        self.data = dataset
    
    def line_scatter(self,args):
        print("args inside class ",args)
        return sns.relplot(data=self.data,x=args[2], y=args[3], hue=args[6], size=args[11], style=None, units=None, row=args[12], col=args[7], col_wrap=None, 
                           row_order=None, col_order=None, palette=None, hue_order=None, hue_norm=None, sizes=None, size_order=None, size_norm=None, markers=None, 
                           dashes=None, style_order=None, legend='auto', kind=args[1], height=int(args[9]), aspect=float(args[10]), facet_kws=None)
    
    def other_than_line_scatter(self,args):
        print("args inside class ",args)
        return sns.catplot(data=self.data,x=args[2], y=args[3], hue=args[6], row=args[12], col=args[7], col_wrap=None, estimator='mean', errorbar=('ci', 95), 
                           n_boot=1000, units=None, seed=None, order=None, hue_order=None, row_order=None, col_order=None, height=int(args[9]), aspect=float(args[10]), 
                           kind=args[1], native_scale=False, formatter=None, orient=None, color=args[8], palette=None, 
                           hue_norm=None, legend='auto', legend_out=True, sharex=True, sharey=True, margin_titles=False, facet_kws=None, ci='deprecated')
    




    
