Research
========

Credits should be inflationary but the inflation should be low. It is needed to match utilization but must be low
enough for savings to retain most of their value... Perhaps all of their value if the math can balance and a user
is willing to stake all of their savings when minting.

Maybe we can use block# for mutability e.g. in block1 a user moves 1 credit into their mint. This is an 'internal'
transaction that removes their credit from possible spending in this and future blocks.

Credits in the mint are the stake used for PoS calculations and penalties in subsquent blocks.

With the blockchain ledger the entire chain is used to recalculate balances (they can be cached but they are deliberately
not part of the blockchain. I wonder if we can put the balances into the BC to limit the need for lookback.

I see how this compromises RI but perhaps this 'double accounting' is not such a bad idea. It avoids the need on most
devices for the presence of old blocks.

https://math.stackexchange.com/questions/239202/how-to-perform-a-fair-coin-toss-experiment-over-phone

https://blog.chain.com/a-letter-to-jamie-dimon-de89d417cb80

https://www.tezos.com/governance

Hmm nomic rules, TLA verification. Allow voting to add funds. As it starts with just me I can vote myself e.g. c100

Then when Alice and Bob get my app I can 'pay' them c30 each. Now there are three potential voters.

Voting more credits will devalue everyone's existing credits.
If credits holders are inactive we could 'decay' their credits (the opposite of interest).

As our POS is so cheap, we no longer need to provide income for verification.
So no inflow except voted inputs?

flux voting app
voting using distributed ledger/decentralized application - no corruption.


https://hackernoon.com/what-will-bitcoin-look-like-in-twenty-years-7e75481a798c

https://gladius.io/#product DDOS prevention - rent bandwidth to earn tokens.

https://iota.org/
https://blog.iota.org/a-primer-on-iota-with-presentation-e0a6eb2cc621

https://hashgraph.com/

Blockchain
----------

PoW, PoS?

ICO

Etherium
--------

`Etherium is attempting to switch from POW to POS <https://www.youtube.com/watch?v=aRiUG2UeUBc>`_.

'tragedy of the commons' Reward decreases over time resulting in less miners resulting in greater possibility of
a 51% acquisition and subsequent corruption.

Etherium casper algorithm
Slasher
Tendermint


Sybil attack
Chain of trust ~= #blocks with my transactions in them? No

Peercoin
--------

Questions
---------

How can we avoid the need for any individual node to maintain a full copy of the ledger?
........................................................................................

Perhaps we can supply income on the basis of blocks held (inversely proportional to #blockcopies) such that we
periodically verify the copy and the holder gets some credit on successful verification. The smaller #blockcopies
the greater the credit.

How can we avoid the need for POW?
..................................

`PoS vs PoW <http://bitfury.com/content/5-white-papers-research/pos-vs-pow-1.0.2.pdf>`_
