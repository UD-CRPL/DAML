import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def principal_component_analysis(dataset, labels, plot):
    X_pca = PCA().fit_transform(dataset)
    X_selected = X_pca[:,:30]
    if(plot):
        plot_pca(X_pca, labels)
    return X_selected

def plot_pca(X_pca, labels):
        plt.figure(figsize=(10,5))
        plt.title('PCA - Genetic Variant Dataset')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.scatter(X_pca[:,1],X_pca[:,2],c=labels)
        plt.legend()
        plt.show()
        return
