Research
========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   australian_political_parties
   cryptocurrency/index
   hashgraph

Mind Dump
=========

Decentralized Truth
-------------------

https://medium.com/@FEhrsam/blockchain-governance-programming-our-future-c3bfe30f2d74

A hashgraph/blockchain git (is git already this) where the POT is consensual (voted??)

If this works it can implement legislation/constitution/government - issues = proposed changes.

We could then start the whole respect thing as a nomic like game to build the policy.

https://www.tezos.com/governance

An identity:
A pub key. openssh key pair.

Verifying an identity:
Send random string R to claimant, Decrypt their response using their identity and verify it equals R.

initial:
creator identity is assigned the role of super_user.
One rule:
A super_user can to anything

The super user may:
define rules
create/register members (identities)


Rules may define roles (in terms of what they can do)

Members may be assigned roles (giving them permission to do certain things)

We probably do need a verifiable (interpreted?) language for the rule implementation???? Like tezos

The 'ledger' becomes a sorta redux store plus its reducers or a sorta git where the commit could be local and the push to the POT is where things become 'agreed'

The model
---------

Our store has an immutable state and a set of reducers.
A reducer takes the state and an action and returns the new store (its redux!).

reducers are part of the store state. The initial reducer is sorta:

.. code-block:: javascript

   const reducerByType = (state={}, {type, reducer}) => {
     switch (type){
       case 'ADD_REDUCER':
         return {...state, [type]: ???}}}

If we take the view that our state is sorta immutable json we can probably use a mini language to express our reducers.
put(mapping, key, value) - new mapping with key = value
add(set, value) - new set with value included
drop(mapping, key)
remove(set, value)
push(list, value, index)
pop(list, index)

.. code-block::

   {'ADD_REDUCER': put(state, key, get(state, key, value)