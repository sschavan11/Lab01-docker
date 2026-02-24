from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import joblib

if __name__ == "__main__":
    # Load Wine dataset 
    wine = load_wine()
    X, y = wine.data, wine.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create pipeline: Scaling + Logistic Regression
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=5000, solver="lbfgs")
    )

    # Train model
    model.fit(X_train, y_train)

    # Save trained model
    joblib.dump(model, "wine_model.pkl")

    print("The model training was successful (Wine + Logistic Regression)")
