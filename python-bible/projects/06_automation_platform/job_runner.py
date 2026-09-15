from dataclasses import dataclass, field
from datetime import datetime
from queue import Queue
from threading import Thread

@dataclass
class Job:
    name: str
    fn: object
    args: tuple=()
    kwargs: dict=field(default_factory=dict)

class JobRunner:
    def __init__(self, workers=2):
        self.q=Queue(); self.history=[]
        self.workers=[Thread(target=self._worker,daemon=True) for _ in range(workers)]
        for w in self.workers: w.start()
    def submit(self,job): self.q.put(job)
    def _worker(self):
        while True:
            job=self.q.get()
            try:
                result=job.fn(*job.args,**job.kwargs); self.history.append((job.name,'success',datetime.now().isoformat(),result))
            except Exception as e: self.history.append((job.name,'failed',datetime.now().isoformat(),repr(e)))
            finally: self.q.task_done()

if __name__=='__main__':
    r=JobRunner(); r.submit(Job('demo',lambda x:x*x,args=(7,))); r.q.join(); print(r.history)
