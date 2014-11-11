#  Python Module for import                           Date : 2014-08-08
#  vim: set fileencoding=utf-8 ff=unix tw=78 ai syn=python : per Python PEP 0263 
''' 
_______________|  yi_plot.py : essential plot functions.

References:
- Computational tools for pandas
  http://pandas.pydata.org/pandas-docs/stable/computation.html

CHANGE LOG  For latest version, see https://github.com/rsvp/fecon235
2014-08-08  Add dpi for saving image files.
2014-08-06  For boxplot, remove y_time.yymmdd_t() as fid, 
               use title instead of fid, and add grid.
2014-08-05  Revise from yip_plot.py for boxplot to handle dataframe.
'''

import matplotlib.pyplot as plt
import pandas as pd

dotsperinch = 140                 #  Resolution for plot.


#  #  Test data for boxplot:
#  import numpy as np
#  
#  np.random.seed(10)
#  
#  data = np.random.randn(30, 4)
#  labels = ['A', 'B', 'C', 'D']


def boxplot( data, title='tmp', labels=[] ):
     '''Make boxplot from data which could be a dataframe.'''
     #  - Use list of strings for labels, 
     #       since we presume data has no column names, 
     #       unless data is a dataframe.
     #
     #  - Directly entering a dataframe as data will fail, 
     #       but dataframe.values will work, so:
     lastidx = 'NA'
     #         ^for part of the plot's title...
     #  If data is a dataframe, extract some info 
     #    before conversion to values:
     if isinstance( data, pd.DataFrame ):
          lastidx = str( data.index[-1] )  
          colnames = list( data.columns )
          labels = colnames
          data = data.values

     fig, ax = plt.subplots()
     ax.boxplot( data )
     ax.set_xticklabels( labels )
     #  HACK to show points of last row as a red dot:
     ax.plot( [list(data[-1])[0]] + list(data[-1]), 'or' )
          #   ^need a dummy first point in the neighborhood
          #    for autoscale to work properly.
     ax.set_title( title + ' / last ' + lastidx )  
     plt.grid(True)
     plt.show()

     #  Now prepare the image file to save:
     title = title.replace( ' ', '_' )
     imgf = 'boxplot-' + title + '.png' 
     fig.set_size_inches(11.5, 8.5)
     fig.savefig( imgf, dpi=dotsperinch )
     print " ::  Finished: " + imgf
     return



if __name__ == "__main__":
     print "\n ::  THIS IS A MODULE for import -- not for direct execution! \n"
     raw_input('Enter something to get out: ')