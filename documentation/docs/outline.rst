Outline
=======

A small set of apps will create an ecosystem for the generation, use and exchange of credits (tokens).

MON3
----

This app is a combined wallet and miner for a blockchain technology. This will work much like a bitcoin wallet save
that:

- It runs as an active process on a device and is available to 'mine' (verify) blocks.
- mining blocks successfully will create a credit income that is added to the wallet
- the wallet can send and accept credits from other wallets. Sent & received credits are held in escrow until the
  relevant block is verified.

I'd like to avoid an ICO but am not sure how to. Perhaps we can have some credits randomly appear in the system over
time somehow or??

MONBUMP
-------

This app is connected to one or more local MON3 apps. It allows a user of the device to locally transfer credits
to another device using bump (or email or whatever).

MONSTAKE
--------

This app presents a set of questions and supports the ability to add new questions. Each question includes the list of
all possible answers. Once 'accepted' (there is a recognised way to decide the question (possibly including expiry)).

Any user may tender credits on any answer option. A tender must have a non zero ratio (default 1:(n -1) where n is the
number of possible answers.

Where there are tenders, a user may 'take' all or part of the tender.

All credits are transferred to the question accepter (the bookie). They are paid back out appropriately when the
question is resolved.