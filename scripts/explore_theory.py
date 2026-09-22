#!/usr/bin/env python3
"""Enumerate candidate tuples, not validated causal pathways. Standard library only."""
import argparse
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def unrank(items, order, rank):
    """Return a lexicographic combination directly, without materializing prior tuples."""
    n = len(items)
    if not 0 <= rank < math.comb(n, order):
        raise ValueError('rank outside candidate space')
    chosen, start = [], 0
    for remaining in range(order, 0, -1):
        for i in range(start, n - remaining + 1):
            block = math.comb(n - i - 1, remaining - 1)
            if rank < block:
                chosen.append(items[i]); start = i + 1; break
            rank -= block
    return tuple(chosen)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--variables', nargs='+', help='Subset of V001–V128; sorted canonically')
    p.add_argument('--order', type=int, choices=[2,3,4], default=2)
    p.add_argument('--offset', type=int, default=0, help='Zero-based lexicographic rank')
    p.add_argument('--limit', type=int, default=20, help='Maximum JSONL records to emit')
    p.add_argument('--stats', action='store_true')
    args = p.parse_args()
    data = json.loads((ROOT/'theory/data/variables.json').read_text())['variables']
    lookup = {v['id']:v for v in data}
    ids = sorted(set(args.variables or lookup))
    unknown = set(ids)-set(lookup)
    if unknown: p.error('Unknown IDs: '+', '.join(sorted(unknown)))
    if args.offset < 0 or args.limit < 0: p.error('offset and limit must be nonnegative')
    if args.stats:
        counts = {str(k):math.comb(len(ids),k) for k in [2,3,4]}
        print(json.dumps({'variables':len(ids),'unordered_candidates':counts,'total':sum(counts.values()),'status':'candidates, not causal findings'},ensure_ascii=False))
        return
    if len(ids)<args.order: p.error('Not enough distinct variables for this order')
    total=math.comb(len(ids),args.order)
    for rank in range(args.offset,min(total,args.offset+args.limit)):
        combo=unrank(ids,args.order,rank)
        print(json.dumps({'rank':rank,'variables':list(combo),'names':[lookup[x]['name'] for x in combo],'status':'unexamined candidate; specify context, direction, outcome and alternatives'},ensure_ascii=False))

if __name__=='__main__': main()
