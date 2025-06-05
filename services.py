import httpx

async def forward_request_to_external_api(url: str, payload: dict, headers: dict = None):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        return response.json()
