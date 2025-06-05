from fastapi import APIRouter, Request, Header, HTTPException
from .services import forward_request_to_external_api
from .config import API_KEY

router = APIRouter()

@router.post("/gateway")
async def gateway_endpoint(
    request: Request,
    x_api_key: str = Header(...)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")

    body = await request.json()

    external_url = body.get("external_url")
    payload = body.get("payload")

    if not external_url or not payload:
        raise HTTPException(status_code=400, detail="Missing external_url or payload")

    result = await forward_request_to_external_api(external_url, payload)
    return {"status": "forwarded", "result": result}
