import asyncio, httpx

async def fetch(client,url,attempts=3):
    for n in range(attempts):
        try:
            r=await client.get(url,timeout=10); r.raise_for_status(); return r.json()
        except (httpx.HTTPError,ValueError):
            if n==attempts-1: raise
            await asyncio.sleep(2**n)

async def pipeline(urls):
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(*(fetch(client,u) for u in urls))

if __name__=='__main__':
    import sys
    print(asyncio.run(pipeline(sys.argv[1:])))
