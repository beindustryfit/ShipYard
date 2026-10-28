"""ShipYard.

Week 1: add POST /webhooks/github.
Keep GET /. The starter test calls it.
"""
from fastapi import FastAPI

app = FastAPI(title="ShipYard")


@app.get("/")
def root():
    return {"app": "shipyard", "hint": "Week 1: add POST /webhooks/github"}
