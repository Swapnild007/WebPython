import asyncio
from concurrent.futures import ProcessPoolExecutor

def cpu_job(n): return sum(i*i for i in range(n))

async def io_job(name, delay):
    await asyncio.sleep(delay); return name

async def main():
    io_results=await asyncio.gather(io_job('A',.2),io_job('B',.1),io_job('C',.3))
    with ProcessPoolExecutor() as pool:
        loop=asyncio.get_running_loop(); cpu=await loop.run_in_executor(pool,cpu_job,100_000)
    print({'io':io_results,'cpu':cpu})

if __name__=='__main__': asyncio.run(main())
