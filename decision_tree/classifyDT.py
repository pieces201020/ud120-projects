def classify(features_train, labels_train):

    ### your code goes here--should return a trained decision tree classifer
    from sklearn import tree

    clf = tree.DecisionTreeClassifier()

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print "predicting time:", round(time()-t0, 3), "s"


    from sklearn.metrics import accuracy_score
    acc = accuracy_score(pred, labels_test)
    print 'Accuracy is ', acc


    return clf
