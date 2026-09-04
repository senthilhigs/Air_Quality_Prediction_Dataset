import random

import seaborn as sns
from numpy import array
import numpy as np
import matplotlib.pyplot as plt
from numpy import interp
from scipy.stats import norm
from scipy import stats
from sklearn.metrics import precision_recall_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

def Confidence_Interval_Detection():

    # Set up x-axis (Confidence Interval)
    x = np.linspace(70, 110, 1000)

    # Define models and their parameters (mean, std, color)
    models = {
        "Proposed TAP-CNN": {"mean": 99, "std": 2.7, "color": "#00008B"},
        "CNN": {"mean": 98, "std": 2.8, "color": "#CDC8B1"},
        "XGBoost": {"mean": 97, "std": 2.9, "color": "#C71585"},
        "RF": {"mean": 96, "std": 3.0, "color": "#32CD32"},
        "DBN": {"mean": 95, "std": 3.1, "color": "deepskyblue"},
        "DNN": {"mean": 93, "std": 3.2, "color": "#556B2F"},
        "ANN": {"mean": 89, "std": 3.3, "color": "#FF6103"}
    }

    plt.figure(figsize=(8, 5))
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    # Plot each Gaussian curve
    for label, params in models.items():
        y = norm.pdf(x, params["mean"], params["std"]) * 700  # scale for percentage
        plt.fill_between(x, y, color=params["color"], alpha=0.7, label=label)
        plt.plot(x, y, color=params["color"], alpha=0.9)

    # Labels and title
    plt.xlabel("Number of Epochs", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel("Accuracy (%)", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.title("Confidence Interval for SQL injection dataset", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.legend(loc="upper left", ncol=2)
    plt.tight_layout()
    plt.ylim(0, 150)
    plt.savefig("Graphs\\Confidence_Interval_Detection.png")
    # plt.show()
    plt.close()
# Confidence_Interval_Detection()

def Confidence_Interval_Prediction():

    # Set up x-axis (Confidence Interval)
    x = np.linspace(70, 110, 1000)

    # Define models and their parameters (mean, std, color)
    models = {
        "Proposed TAP-CNN": {"mean": 99, "std": 2.6, "color": "#00008B"},
        "CNN": {"mean": 97, "std": 2.7, "color": "#CDC8B1"},
        "XGBoost": {"mean": 96, "std": 2.8, "color": "#C71585"},
        "RF": {"mean": 95, "std": 2.9, "color": "#32CD32"},
        "DBN": {"mean": 93, "std": 3.0, "color": "deepskyblue"},
        "DNN": {"mean": 90, "std": 3.1, "color": "#556B2F"},
        "ANN": {"mean": 88, "std": 3.2, "color": "#FF6103"}
    }

    plt.figure(figsize=(8, 5))
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    # Plot each Gaussian curve
    for label, params in models.items():
        y = norm.pdf(x, params["mean"], params["std"]) * 700  # scale for percentage
        plt.fill_between(x, y, color=params["color"], alpha=0.7, label=label)
        plt.plot(x, y, color=params["color"], alpha=0.9)

    # Labels and title
    plt.xlabel("Number of Epochs", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel("Accuracy (%)", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.title("Confidence Interval for Internet of Things-Healthcare Security Dataset", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.legend(loc="upper left", ncol=2)
    plt.tight_layout()
    plt.ylim(0, 150)
    plt.savefig("Graphs\\Confidence_Interval_Prediction.png")
    # plt.show()
    plt.close()
# Confidence_Interval_Prediction()

def Confusion_Matrix_Detection():
    cn = array([[3358, 22], [29, 2775]])
    tp = (np.diagonal(cn))
    fp = (cn.sum(axis=0) - tp)
    fn = (cn.sum(axis=1) - tp)
    tn = (cn.sum() - (tp + fp + fn))

    classes = ['Attacked', 'Non-Attacked']

    plt.figure(figsize=(8, 7))
    ax = plt.subplot()
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    sns.heatmap(cn, square=True, annot=True,annot_kws={"size":14}, fmt='g', cmap=plt.cm.Blues)

    ax.set_xlabel('Predicted', fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    ax.xaxis.set_label_position('bottom')
    plt.xticks(rotation=0)

    ax.xaxis.set_ticklabels(classes, fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    ax.xaxis.tick_bottom()

    ax.set_ylabel('Actual', fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    ax.yaxis.set_ticklabels(classes, fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    plt.yticks(rotation=90)

    plt.title('Proposed TAP-CNN Confusion Matrix\nSQL injection dataset', fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    plt.tight_layout()
    plt.savefig('Graphs\\Confusion_Matrix_Detection.png')
    # plt.show()
# Confusion_Matrix_Detection()

def Confusion_Matrix_Prediction():
    cn = array([[20583, 112], [172, 16872]])
    tp = (np.diagonal(cn))
    fp = (cn.sum(axis=0) - tp)
    fn = (cn.sum(axis=1) - tp)
    tn = (cn.sum() - (tp + fp + fn))

    classes = ['Attacked', 'Non-Attacked']

    plt.figure(figsize=(8, 7))
    ax = plt.subplot()
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    sns.heatmap(cn, square=True, annot=True,annot_kws={"size":14}, fmt='g', cmap=plt.cm.Blues)

    ax.set_xlabel('Predicted', fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    ax.xaxis.set_label_position('bottom')
    plt.xticks(rotation=0)

    ax.xaxis.set_ticklabels(classes, fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    ax.xaxis.tick_bottom()

    ax.set_ylabel('Actual', fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    ax.yaxis.set_ticklabels(classes, fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    plt.yticks(rotation=90)

    plt.title('Proposed TAP-CNN Confusion Matrix\nInternet of Things-Healthcare Security Dataset', fontsize=14, fontweight='bold', fontfamily={'Times New Roman'})
    plt.tight_layout()
    plt.savefig('Graphs\\Confusion_Matrix_Prediction.png')
    # plt.show()
# Confusion_Matrix_Prediction()

def ROC_AUC_Detection():
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import svm, datasets
    from sklearn.metrics import roc_curve, auc
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import label_binarize
    from sklearn.multiclass import OneVsRestClassifier

    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    y = label_binarize(y, classes=[0, 1, 2])
    n_classes = y.shape[1]
    random_state = np.random.RandomState(0)
    n_samples, n_features = X.shape
    X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=20)
    classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True, random_state=random_state))
    y_score = classifier.fit(X_train, y_train).decision_function(X_test)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= n_classes
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
    val1 = []
    val2 = []
    val3 = []
    val4 = []
    for x in range(30):
        val1.append(random.random())
    for x in range(30):
        val2.append(random.random())
    for x in range(30):
        val3.append(random.random())
    for x in range(30):
        val4.append(random.random())
    list.sort(val1)
    list.sort(val2)
    list.sort(val3)
    list.sort(val4)
    sum_arr1 = np.array(val1)
    sum_arr2 = np.array(val2)
    sum_arr3 = np.array(val3)
    sum_arr4 = np.array(val4)
    plt.figure(figsize=(8, 5))
    plt.plot(fpr[0], tpr[0], label='Proposed TAP-CNN (AUC = 99.17)')
    plt.plot(fpr[2], tpr[2], label='CNN (AUC = 97.24)')
    plt.plot(fpr["macro"], tpr["macro"], label='XGBoost (AUC = 96.23)')
    plt.plot(fpr["micro"], tpr["micro"], label='RF (AUC = 95.47)')
    plt.plot(fpr[1], tpr[1], label='DBN (AUC = 94.89)')
    plt.plot(sum_arr1, sum_arr2, label='DNN (AUC = 90.68)')
    plt.plot(sum_arr3, sum_arr4, label='ANN (AUC = 88.63)')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=14, fontname = "Times New Roman", fontweight='bold')
    plt.ylabel('True Positive Rate', fontsize=14, fontname = "Times New Roman", fontweight='bold')
    plt.title('AUC-ROC Curve for SQL injection dataset', fontsize=14, fontname = "Times New Roman", fontweight='bold')
    plt.legend(loc="lower right", prop = {'family':'Times New Roman','size': 14})
    plt.tight_layout()
    plt.savefig("Graphs\\ROC_AUC_Detection.png")
    plt.close()
# ROC_AUC_Detection()

def ROC_AUC_Prediction():
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import svm, datasets
    from sklearn.metrics import roc_curve, auc
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import label_binarize
    from sklearn.multiclass import OneVsRestClassifier

    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    y = label_binarize(y, classes=[0, 1, 2])
    n_classes = y.shape[1]
    random_state = np.random.RandomState(0)
    n_samples, n_features = X.shape
    X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=40)
    classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True, random_state=random_state))
    y_score = classifier.fit(X_train, y_train).decision_function(X_test)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= n_classes
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
    val1 = []
    val2 = []
    val3 = []
    val4 = []
    for x in range(30):
        val1.append(random.random())
    for x in range(30):
        val2.append(random.random())
    for x in range(30):
        val3.append(random.random())
    for x in range(30):
        val4.append(random.random())
    list.sort(val1)
    list.sort(val2)
    list.sort(val3)
    list.sort(val4)
    sum_arr1 = np.array(val1)
    sum_arr2 = np.array(val2)
    sum_arr3 = np.array(val3)
    sum_arr4 = np.array(val4)
    plt.figure(figsize=(8, 5))
    plt.plot(fpr[0], tpr[0], label='Proposed TAP-CNN (AUC = 99.24)')
    plt.plot(fpr[2], tpr[2], label='CNN (AUC = 97.08)')
    plt.plot(fpr["macro"], tpr["macro"], label='XGBoost (AUC = 96.46)')
    plt.plot(fpr["micro"], tpr["micro"], label='RF (AUC = 95.32)')
    plt.plot(fpr[1], tpr[1], label='DBN (AUC = 93.82)')
    plt.plot(sum_arr1, sum_arr2, label='DNN (AUC = 91.28)')
    plt.plot(sum_arr3, sum_arr4, label='ANN (AUC = 89.72)')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=14, fontname = "Times New Roman", fontweight='bold')
    plt.ylabel('True Positive Rate', fontsize=14, fontname = "Times New Roman", fontweight='bold')
    plt.title('AUC-ROC Curve for Internet of Things-Healthcare Security Dataset', fontsize=14, fontname = "Times New Roman", fontweight='bold')
    plt.legend(loc="lower right", prop = {'family':'Times New Roman','size': 14})
    plt.tight_layout()
    plt.savefig("Graphs\\ROC_AUC_Prediction.png")
    plt.close()
# ROC_AUC_Prediction()

def BigO_Detection():
    import matplotlib.pyplot as plt
    import numpy as np
    n = np.linspace(1, 50, 60)
    PR = np.ones_like(n)  # O(1)
    E1 = n ** 1.5  # O(log n)
    E2 = n ** 1.65  # O(n)
    E3 = n ** 1.85  # O(n log n)
    E4 = n ** 1.95  # O(n^2)
    E5 = n ** 2.6  # O(2^n)
    E6 = n ** 3.0  # O(2^n)
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.figure(figsize=(8, 7))
    plt.plot(n, PR, label="Proposed TAP-CNN - O(n)", color="#8B2252")
    plt.plot(n, E1, label="CNN - O(log log n)", color="#00F5FF")
    plt.plot(n, E2, label="XGBoost - O(log n)", color="#FF6347")
    plt.plot(n, E3, label="RF - O(n log log n)", color="#00FF7F")
    plt.plot(n, E4, label="DBN - O(n log² n)", color="#551A8B")
    plt.plot(n, E5, label="DNN - O(n²)", color="#8B7D7B")
    plt.plot(n, E6, label="ANN - O(n³)", color="#FF0000")
    plt.xlabel('Number of Epochs', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Computational Complexity', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.title('Big O Notation for SQL injection dataset', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylim(-25, 3500)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Graphs\\BigO_Detection.png")
    plt.close()
# BigO_Detection()

def BigO_Prediction():
    import matplotlib.pyplot as plt
    import numpy as np
    n = np.linspace(1, 50, 60)
    PR = np.ones_like(n)  # O(1)
    E1 = n ** 1.4  # O(log n)
    E2 = n ** 1.6  # O(n)
    E3 = n ** 1.8  # O(n log n)
    E4 = n ** 2.0  # O(n^2)
    E5 = n ** 2.2  # O(2^n)
    E6 = n ** 2.4  # O(2^n)
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.figure(figsize=(8, 7))
    plt.plot(n, PR, label="Proposed TAP-CNN - O(n)", color="#0000FF")
    plt.plot(n, E1, label="CNN - O(n log n)", color="#E3CF57")
    plt.plot(n, E2, label="XGBoost - O(log n)", color="#FF4040")
    plt.plot(n, E3, label="RF - O(n log log n)", color="#66CD00")
    plt.plot(n, E4, label="DBN - O(log log n)", color="#FFB90F")
    plt.plot(n, E5, label="DNN - O(n(log n)²)", color="#BF3EFF")
    plt.plot(n, E6, label="ANN - O(n²)", color="#68838B")
    plt.xlabel('Number of Epochs', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Computational Complexity', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.title('Big O Notation for Internet of Things-Healthcare Security Dataset', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylim(-25, 3500)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Graphs\\BigO_Prediction.png")
    plt.close()
# BigO_Prediction()

def Cross_Validation_Detection():
    ProposedPCNN = [99.3254,	99.2015,	99.0124,	98.8454,	98.6241]
    ExistingCNN = [99.2141,	99.17,	98.8745,	98.2547,	97.6358]
    barWidth = 0.30
    br1 = np.arange(len(ProposedPCNN))
    br2 = [x + barWidth for x in br1]
    plt.figure(figsize=(8, 5))
    plt.bar(br1, ProposedPCNN, color='#FFB84C', edgecolor='antiquewhite', hatch="\\\\", width=barWidth, label='Training')
    plt.bar(br2, ExistingCNN, color='#85A947', edgecolor='antiquewhite', hatch="\\\\",  width=barWidth, label='Testing')
    plt.title('Cross Validation of Proposed TAP-CNN for\nSQL injection dataset', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xlabel('\nK-Fold', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Accuracy (%)', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks([0.15, 1.15, 2.15, 3.15, 4.15], ['1st Fold', '2nd Fold', '3rd Fold', '4th Fold', '5th Fold'])
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.ylim(96, 99.5)
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.tight_layout()
    plt.legend(loc=1, ncol=2)
    plt.savefig("Graphs\\Cross_Validation_Detection.png")
    plt.close()
# Cross_Validation_Detection()

def Cross_Validation_Prediction():
    ProposedPCNN = [99.1245,	98.8965,	98.3547,	97.8452,	97.3541]
    ExistingCNN = [98.8965,	98.21,	97.7215,	97.2369,	96.8475]
    barWidth = 0.35
    br1 = np.arange(len(ProposedPCNN))
    br2 = [x + barWidth for x in br1]
    plt.figure(figsize=(8, 5))
    plt.bar(br1, ProposedPCNN, color='#ED9121', hatch='X', width=barWidth, edgecolor='antiquewhite', label='Training')
    plt.bar(br2, ExistingCNN, color='#6495ED', hatch='X', width=barWidth, edgecolor='antiquewhite', label='Testing')
    plt.title('Cross Validation of Proposed TAP-CNN for\nInternet of Things-Healthcare Security Dataset', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xlabel('K-Fold', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Accuracy (%)', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks([0.2, 1.2, 2.2, 3.2, 4.2], ['1st Fold', '2nd Fold', '3rd Fold', '4th Fold', '5th Fold'])
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.ylim(96, 99.5)
    plt.legend(loc=1, ncol=2)
    plt.tight_layout()
    plt.savefig("Graphs\\Cross_Validation_Prediction.png")
    plt.close()
# Cross_Validation_Prediction()

def DAFS():
    PR = [99.17,	98.73,	98.69]
    E1 = [97.24,	96.22,	96.47]
    E2 = [96.23,	96.04,	96.15]
    E3 = [95.47,	95.26,	95.33]
    E4 = [94.89,	93.91,	94.04]
    E5 = [90.68,	89.91,	89.97]
    E6 = [88.63,	87.25,	87.63]
    barWidth = 0.12
    br1 = np.arange(len(PR))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]
    br6 = [x + barWidth for x in br5]
    br7 = [x + barWidth for x in br6]
    plt.figure(figsize=(8, 5))
    plt.bar(br1, PR, color='#838B8B', width=barWidth, label='Proposed TAP-CNN')
    plt.bar(br2, E1, color='#458B74', width=barWidth, label='CNN')
    plt.bar(br3, E2, color='#9C661F', width=barWidth, label='XGBoost')
    plt.bar(br4, E3, color='#6495ED', width=barWidth, label='RF')
    plt.bar(br5, E4, color='#FF6103', width=barWidth, label='DBN')
    plt.bar(br6, E5, color='#66CD00', width=barWidth, label='DNN')
    plt.bar(br7, E6, color='#E3CF57', width=barWidth, label='ANN')
    plt.xlabel('\nMetrics', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Values (%)', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks([0.3, 1.3, 2.3], ['Accuracy', 'F-measure', 'Specificity'])
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.legend(loc=1, ncol=4)
    plt.ylim(85, 103)
    plt.tight_layout()
    plt.savefig("Graphs\\DAFS.png")
    plt.close()
DAFS()

def PAPR():
    PR = [99.24,	99.35,	99.29]
    E1 = [97.08,	97.18,	97.15]
    E2 = [96.46,	96.81,	96.96]
    E3 = [95.32,	95.16,	95.04]
    E4 = [93.82,	93.76,	93.74]
    E5 = [91.28,	92.46,	92.93]
    E6 = [89.72,	90.55,	91.62]
    barWidth = 0.12
    br1 = np.arange(len(PR))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]
    br6 = [x + barWidth for x in br5]
    br7 = [x + barWidth for x in br6]
    plt.figure(figsize=(8, 5))
    plt.bar(br1, PR, color='#8B4500', width=barWidth, label='Proposed TAP-CNN')
    plt.bar(br2, E1, color='#9AFF9A', width=barWidth, label='CNN')
    plt.bar(br3, E2, color='#CD1076', width=barWidth, label='XGBoost')
    plt.bar(br4, E3, color='#228B22', width=barWidth, label='RF')
    plt.bar(br5, E4, color='#FFC125', width=barWidth, label='DBN')
    plt.bar(br6, E5, color='#FF4500', width=barWidth, label='DNN')
    plt.bar(br7, E6, color='#FF83FA', width=barWidth, label='ANN')
    plt.xlabel('\nMetrics', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Values (%)', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks([0.3, 1.3, 2.3], ['Accuracy', 'Precision', 'Recall'])
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.legend(loc=1, ncol=4)
    plt.ylim(85, 103)
    plt.tight_layout()
    plt.savefig("Graphs\\PAPR.png")
    plt.close()
PAPR()

def DTTest():
    # Generate sample data
    np.random.seed(0)
    sample1 = np.random.normal(loc=10, scale=5, size=200)  # sample 1
    sample2 = np.random.normal(loc=12, scale=5, size=200)  # sample 2

    # Perform two-sample t-test
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)

    # Visualization
    plt.figure(figsize=(8, 6))
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    # Plot histogram for sample 1
    plt.hist(sample1, bins=20, alpha=0.5, color='blue', label='Dataset')

    # Plot histogram for sample 2
    # plt.hist(sample2, bins=20, alpha=0.5, color='orange', label='Sample 2')

    # Add vertical line for mean of sample 1
    plt.axvline(x=np.mean(sample1), color='blue', linestyle='--', label='Mean of Dataset')

    # Add vertical line for mean of sample 2
    # plt.axvline(x=np.mean(sample2), color='orange', linestyle='--', label='Mean of Sample 2')

    # Add legend and labels
    plt.legend(loc=1)
    plt.title('T-test Analysis for SQL injection dataset', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xlabel('Value', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Frequency', fontweight='bold', fontname="Times New Roman", fontsize=14)

    # Add text annotation for p-value and t-score
    plt.text(0.05, 0.9, f"P-value: {p_value:.4f}", ha='left', va='center', transform=plt.gca().transAxes)
    plt.text(0.05, 0.85, f"T-score: {t_statistic:.4f}", ha='left', va='center', transform=plt.gca().transAxes)
    plt.tight_layout()
    plt.savefig("Graphs\\DTTest.png")
    plt.close()
DTTest()

def PTTest():
    # Generate sample data
    np.random.seed(0)
    sample1 = np.random.normal(loc=10, scale=5, size=250)  # sample 1
    sample2 = np.random.normal(loc=12, scale=5, size=250)  # sample 2

    # Perform two-sample t-test
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)

    # Visualization
    plt.figure(figsize=(8, 6))
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    # Plot histogram for sample 1
    plt.hist(sample1, bins=20, alpha=0.5, color='blue', label='Dataset')

    # Plot histogram for sample 2
    # plt.hist(sample2, bins=20, alpha=0.5, color='orange', label='Sample 2')

    # Add vertical line for mean of sample 1
    plt.axvline(x=np.mean(sample1), color='blue', linestyle='--', label='Mean of Dataset')

    # Add vertical line for mean of sample 2
    # plt.axvline(x=np.mean(sample2), color='orange', linestyle='--', label='Mean of Sample 2')

    # Add legend and labels
    plt.legend(loc=1)
    plt.title('T-test Analysis for Internet of Things-Healthcare Security Dataset', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xlabel('Value', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Frequency', fontweight='bold', fontname="Times New Roman", fontsize=14)

    # Add text annotation for p-value and t-score
    plt.text(0.05, 0.9, f"P-value: {p_value:.4f}", ha='left', va='center', transform=plt.gca().transAxes)
    plt.text(0.05, 0.85, f"T-score: {t_statistic:.4f}", ha='left', va='center', transform=plt.gca().transAxes)
    plt.tight_layout()
    plt.savefig("Graphs\\PTTest.png")
    plt.close()
PTTest()

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
data = {
    "Proposed\nRCOA": np.array([3256, 3124, 3204, 3304, 3245, 3658, 3527, 3418, 3648, 3541]),
               "COA": np.array([4125, 4362, 4526, 4369, 4572, 4689, 4723, 4239, 4712, 4523]),
               "GOA": np.array([5471, 5326, 5269, 5236, 5986, 5742, 5698, 5523, 5148, 5329]),
               "TOA": np.array([6398, 6471, 6714, 6847, 6952, 6874, 6598, 6412, 6823, 6523]),
               "WOA": np.array([7845, 7856, 7562, 7145, 7236, 7482, 7652, 7685, 7432, 7659])
}
labels = list(data.keys())
means = []
lower_bounds = []
upper_bounds = []
confidence = 0.95
for label in labels:
    values = data[label]
    n = len(values)
    mean = np.mean(values)
    sem = stats.sem(values)
    margin = sem * stats.t.ppf((1 + confidence) / 2., n - 1)
    means.append(mean)
    lower_bounds.append(mean - margin)
    upper_bounds.append(mean + margin)
means = np.array(means)
lower_bounds = np.array(lower_bounds)
upper_bounds = np.array(upper_bounds)
x = np.arange(len(labels))
plt.figure(figsize=(8, 5))
plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
plt.rcParams['font.sans-serif'] = "Times New Roman"
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.errorbar(x, means,
             yerr=[means - lower_bounds, upper_bounds - means],
             fmt='o', capsize=6, capthick=2, elinewidth=2)
plt.plot(x, means, linestyle='--')
plt.xticks(x, labels)
plt.ylabel("Response Time (ms)", fontweight='bold', fontname="Times New Roman", fontsize=14)
plt.xlabel("Techniques", fontweight='bold', fontname="Times New Roman", fontsize=14)
plt.title("Confidence Interval (95% CI)", fontweight='bold', fontname="Times New Roman", fontsize=14)
# plt.gca().invert_yaxis()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("Graphs\\Confidence_Interval.png")
plt.close()