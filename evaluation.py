import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import r2_score

def evaluate(y,yhat,figname='figure',visualize=True,):
    R2, RMSE = calc_score(y,yhat) 
    print (f" R2 = {R2} \n RMSE:{RMSE}")
    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(y,yhat,'.')
    ax.plot([0,y.max()],[0,y.max()],'-')
    ax.text(0.1,0.9, 'RMSE:%5.2f\nR2:%5.2f'%(RMSE,R2), transform=ax.transAxes)
    plt.xlabel('True Sale Price')
    plt.ylabel('Predicted Sale Price')

    fig.savefig(figname + '.png')
    return {'R2':R2,'RMSE':RMSE}

def calc_score(y,yhat):
    R2 = r2_score(y, yhat)
    RMSE = mean_squared_error(y,yhat,squared=False)
    return (R2,RMSE)