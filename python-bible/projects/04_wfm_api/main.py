from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app=FastAPI(title='Python Bible WFM API',version='1.0')
class Interval(BaseModel):
    skill: str=Field(min_length=1); offered: int=Field(ge=0); handled: int=Field(ge=0); abandoned: int=Field(ge=0); aht_seconds: float=Field(gt=0)
store=[]
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/intervals')
def add(x:Interval): store.append(x); return x
@app.get('/intervals')
def list_intervals(): return store
@app.get('/summary')
def summary():
    offered=sum(x.offered for x in store); handled=sum(x.handled for x in store); abandoned=sum(x.abandoned for x in store)
    return {'offered':offered,'handled':handled,'abandoned':abandoned,'abandon_rate_pct':round(abandoned/offered*100,2) if offered else 0}
