from dataclasses import dataclass, asdict
import argparse, json
from pathlib import Path

@dataclass
class Transaction:
    kind: str
    amount: float
    category: str
    note: str = ""

class Ledger:
    def __init__(self, path="data.json"):
        self.path=Path(path); self.items=[]; self.load()
    def load(self):
        if self.path.exists(): self.items=[Transaction(**x) for x in json.loads(self.path.read_text())]
    def save(self):
        self.path.parent.mkdir(parents=True,exist_ok=True); self.path.write_text(json.dumps([asdict(x) for x in self.items],indent=2))
    def add(self, tx):
        if tx.kind not in {"income","expense"} or tx.amount<=0: raise ValueError("invalid transaction")
        self.items.append(tx); self.save()
    def balance(self): return sum(x.amount if x.kind=="income" else -x.amount for x in self.items)

def main():
    p=argparse.ArgumentParser(); p.add_argument("--add",choices=["income","expense"]); p.add_argument("--amount",type=float); p.add_argument("--category",default="General"); p.add_argument("--note",default=""); a=p.parse_args()
    l=Ledger()
    if a.add: l.add(Transaction(a.add,a.amount,a.category,a.note))
    print(f"Balance: {l.balance():.2f}")
if __name__=="__main__": main()
