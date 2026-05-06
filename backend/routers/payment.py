from fastapi import APIRouter, HTTPException, Query
import stripe, os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@router.get("/checkout/")
async def create_checkout_session(email: str = Query(...), price: int = Query(...)):
    try:
        session = stripe.checkout.Session.create(
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "FastAPI Product"},
                    "unit_amount": price * 100,
                },
                "quantity": 1,
            }],
            metadata={
                "user_id": 3,
                "email": email,
                "request_id": "req_123"
            },
            mode="payment",
            success_url=os.getenv("BASE_URL") + "/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=os.getenv("BASE_URL") + "/cancel",
            customer_email=email,
        )
        return {"checkout_url": session.url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))