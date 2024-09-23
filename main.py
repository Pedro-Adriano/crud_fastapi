import uvicorn

from fastapi import FastAPI

from app.routers import bills_router, supplier_and_customer_router, \
    supplier_and_customer_bills_router
from shared.exceptions import NotFound
from shared.exceptions_handler import not_found_exception_handler

app = FastAPI()

app.include_router(bills_router.router)
app.include_router(supplier_and_customer_router.router)
app.include_router(supplier_and_customer_bills_router.router)
app.add_exception_handler(NotFound, not_found_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0", port=9015)
