from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse
import db_helper
from db_helper import create_booking
import re

app = FastAPI()

# Define what Dialogflow sends
class DialogflowParameters(BaseModel):
    name: Optional[str]
    email: Optional[str]
    message: Optional[str]

class QueryResult(BaseModel):
    intent: dict
    parameters: DialogflowParameters

class DialogflowRequest(BaseModel):
    queryResult: QueryResult


@app.post("/webhook")
async def dialogflow_webhook(req: DialogflowRequest,request:Request):
    intent_name = req.queryResult.intent["displayName"]
    payload = await request.json()
    
    if intent_name == "consulting booking":

         # Response to Dialogflow
        
        name = req.queryResult.parameters.name
        parameters=payload['queryResult']['intent']['displayName']['parameters']
        email =  parameters['email']
        context = payload['queryResult']['outputContexts']
       
        message = req.queryResult.parameters.message
        date = req.queryResult.parameters.date
        service = req.queryResult.parameters

        # 🔥DB logic
        booking_id = create_booking(name, email,date,service)
        print(f"📥 New Consultation: {name}, {email}, {message}")
        return book_consultation(email,date,name,service)
    
def sessions_string(string):
    # get regex of output context slash session id
    pass
        
def book_consultation(email,date,name,service,budget):
    return JSONResponse(content={
            "fulfillmentText": f"Thanks {name}, your consultation has been booked. We'll email you soon."
        })
if __name__ =='__main__':
   create_booking("Thato", "Teedow@gmail.com", "2025-06-08 14:00:00",)

        
