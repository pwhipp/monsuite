Mind Dump
=========

Social Media Visibility modelling
---------------------------------

As the number of issues and information grows, mechanisms are essential to ensure that users can keep up with the information they feel is relevant to them, ideally without creating 'bubbles'

Killing the polls
-----------------

An issue can be 'submitted' for the vote and then voted on over some 'reasonable, pre-agreed time'. During this time,
the current state of voting can be made public so the number of votes are known together with the remaining votes.

This is good for galvanizing people if it is still changeable but not so good if there is an early significant leader which might dissuade members from bothering to use their vote.

Initial delegation
------------------

When new members are added, there may be an initial defined delegation. For example, 'new_member' topic might be delegated to 'the member with the smallest number of delegations who has the "secretary" role assigned to them.

Roles are assigned by issues in the "roles" topic...

Categorization and initial issue generation
-------------------------------------------

Issues must be categorized in order to allow scaling and reasonable delegation. An issues category may be initially specified by the creator of the issue
but could be subsequently changed. How do we stop users from creating too many issues?

We could delegate 'issue creation' votes?


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

Voting history should be visible for every member including their delegation chain (which covers how they may have ended up voting a certain way).

Privacy concerns mean that no member can see another member's voting history - only their votes which caused the member to vote that way.

If Alice delegates her vote to Bob, does Bob have a right to reject it? By default Bob will have to declare himself a 'politician' making his voting history public.
A politician can 'resign' in which case votes revert to the delegee and their subsequent voting is private (unless publicised by them becoming a politician again).



Using Git
---------

I create a repo that includes 'git hooks' as part of its code such that I can permit/prevent pushes.

I can permit/control the pushes using consensus or ?hashgraph or...

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

.. code-block:: javascript

   {'ADD_REDUCER': put(state, key, get(state, key, value)

Voting
------

Where humans are voting, a large number of options are unlikely to ever be considered reasonably.
A good option is to randomly assign pairs for voting so a voter is presented with one or more pairs and simply asked which one they prefer. Perhaps allow 'equally good' (each scores 0.5) and equally bad (each scores 0).

Root
   Constitution
   Membership
   Rule

Rule
----

dRoot
   .config
      add: 90
      delete: 90
      change: 90
   dNewMember
      .config
         add: 0
         delete: 75


All actions must be signed.

new_member(details)
   details - {public_key: "xlkjlkj", fullname: "lklkj", nickname: "lklkj" email:...}



accept_member(

delegate(Membership, from_member, to_member) - requires from_member signature.
=> to_member may use the vote on changes under Membership

retract(Membership, member) - requires member signature
=> member gets their vote back

upvote(folder, patch, member, n=1) - requires member signature
downvote(folder, patch, member, n=1)

As long as the order of these commands is consistent they can reconstruct the state of the data at any time.

The data consists of objects