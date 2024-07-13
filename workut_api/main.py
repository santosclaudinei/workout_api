from fastapi import FastAPI

from workut_api.routers import api_router
  
app = FastAPI(title='WorkutApi')
app.include_router(api_router)
