## CryptoCurrency Price Predictor API with FastAPI and ML models

#### This is an API that predicts the closing price of a cryptocurrency pair (e.g BTC/USD) using support vector machines.

## Intstallation
```git clone https://github.com/Tee-py/fast-crypto-predictor.git
cd fast-crypto-predictor
source env/Scripts/activate
pip install -r requirements.txt
uvicorn main:api --reload --workers 1 --host 0.0.0.0 --port 8008```