Git
===

Git is excellent as a content addressed file system with full history. We could perhaps take git and integrate a voting system into its hooks with the voting backed by something flux like or hashgraph supported.

Votes might be acquired by purchasing an identity in some 'partnered' app.

https://git-scm.com/book/en/v2

This is akin to an `integration manager workflow <https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#wfdiag_b>`_ where the integration manager is a voting mechanism taking the votes of participants identified by some convention using the files in the repository.

It can extend through the peer to peer nature of git but this may require extensions to git's core functionality such that the entire git repository is not required (a significant change).

With a distributed decentralized git, a party could produce a patch based upon some subset of the whole. To be verified though, this patch would have to be applied to the whole - perhaps this latter operation can be a 'proof of work' requiring both significant storage and processing. For this to be meaningful it must be possible to patch patched subsets too.