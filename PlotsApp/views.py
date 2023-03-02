from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from . import generate_plot as gp

def index(request):
    if request.method=='POST':

        myfile = request.FILES['my_uploaded_file']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(myfile.name, myfile)

        return redirect('plots/?my_data={}'.format(filename))
    else:
        return render(request,'index.html')

def process_plots(request):
    filename = request.GET.get('my_data','')
    file = pd.read_csv('media/'+filename)
    return render(request,'plots.html',{
            'columns':list(file.columns),
            'typeofplot':['bar','line','scatter','box','histogram',
                          'violin','boxen','point','heatmap'],
            'filename':filename,
        })

def return_img(*args):
    dataset = pd.read_csv('media/'+args[0])
    charttype = args[1]
    x_axis = args[2]
    y_axis = args[3]
    xlabel = args[4]
    ylabel = args[5]

    plotfunc = gp.KindsOfPlots(file=dataset, x=x_axis, y=y_axis,charttype=charttype)
    plot = ''
    if charttype=='line' or charttype=='scatter':
        plot = plotfunc.line_scatter()
    else:
        plot = plotfunc.other_than_line_scatter()
    # Save the plot to a file in the media folder
    plot_path = os.path.join(settings.MEDIA_ROOT, 'my_plot.png')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plot.savefig(plot_path)

    # Construct the URL of the saved plot
    plot_url = os.path.join(settings.MEDIA_URL, 'my_plot.png')

    # Render the plot in the response
    return plot_url
    
    
    


def display_form(request):
    if request.method=='POST':
        charttype = request.POST['chart']
        x_axis = request.POST['Xaxis']
        y_axis  = request.POST['Yaxis']
        xlabel = request.POST['xlabel'] if request.POST['xlabel'] else 'X-Axis'
        ylabel = request.POST['ylabel'] if request.POST['ylabel'] else 'Y-Axis'
        filename = request.GET.get('filename','')
        img =  return_img(filename,charttype,x_axis,y_axis,xlabel,ylabel)
        return render(request, 'show_plot.html', {'plot_url': img})


    
    