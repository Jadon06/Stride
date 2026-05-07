from fastapi import APIRouter, HTTPException, Query, Depends, Request, status
import stripe, os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import uuid

from .. import oauth2, models
from ..database import get_db

load_dotenv()

router = APIRouter()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@router.get("/checkout/")
async def create_checkout_session(email: str = Query(...), price: int = Query(...), product_name: str = Query(...), user_id: int = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    # user = db.query(models.Users).filter(models.Users.id == user_id).first()
    try:
        session = stripe.checkout.Session.create(
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": product_name},
                    "unit_amount": price * 100,
                },
                "quantity": 1,
            }],
            metadata={
                "user_id": user_id,
                "email": email,
                "request_id": f"{uuid.uuid1()}{email}{user_id}"
            },
            mode="payment",
            success_url=os.getenv("BASE_URL") + "/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=os.getenv("BASE_URL") + "/cancel",
            customer_email=email,
        )
        return {"checkout_url": session.url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/webhook/")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    print("stripe hear")
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid signature")
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        new_payment = models.Payment(
            session_id=session["id"],
            email=session["customer_email"],
            amount=session["amount_total"],
            currency=session["currency"],
            status=session["payment_status"],
            user_id=session["metadata"].get("user_id"),
            request_id=session["metadata"].get("request_id"),
        )
        db.add(new_payment)
        db.commit()
        db.close()
    return {"status": "success"}
