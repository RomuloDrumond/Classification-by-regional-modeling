def scale_feat(X_train, X_test, scaleType='min-max'):
    if scaleType=='min-max' or scaleType=='std':
        X_tr_norm = np.copy(X_train) # fazendo cópia para deixar original disponível
        X_ts_norm = np.copy(X_test)
        scaler = MinMaxScaler() if scaleType=='min-max' else StandardScaler()
        scaler.fit(X_tr_norm)
        X_tr_norm = scaler.transform(X_tr_norm)
        X_ts_norm = scaler.transform(X_ts_norm)
        return (X_tr_norm, X_ts_norm)
    else:
        raise ValueError("Tipo de escala não definida. Use 'min-max' ou 'std'.")