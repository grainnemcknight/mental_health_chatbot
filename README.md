# mental_health_chatbot

Implements a lightweight NLU Server using RASA & FastAPI with a Streamlit Interface 

## Project Requirements

1. Install Poetry i.e. `curl -sSL https://install.python-poetry.org | python3 -
`
2. Make sure you have a compatible version of python as specified in the pyproject.toml
3. Run `poetry install` in your environment or create a poetry environment


## Running the Application

Run the following from the terminal (make sure the relevant ports aren't already in use)

` ./start.sh
`

This should open the streamlit app in a new browser window where you can interact with the Intent Detection Model


## Calling the FastAPI Endpoint from Another Service

Once the start script has been run the FastAPI app should be up and running at `http://0.0.0.0:8000` and can be called via a POST request:

``` 
curl -X POST -H "Content-Type: application/json" -d '{"text":"hello"}' http://localhost:8000/parse/
```

The response will contain the name of the detected intent, the confidence associated with the prediction and the integer value mapped to the intent:

```
{"intent":"greet","confidence":0.9999904632568359,"intent_number":6}
```


## Model Evaluation

Run `rasa test nlu --nlu train_test_split/test_data.yml` and the results should be visible in the results folder

## Changing the Model

If you have trained an alternative model you can change the model name in the `start.sh` script and restart.




