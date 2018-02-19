Sandbox
=======

A sandbox is a place where anyone can play, creating an isolated collection of members, issues etc. and experimenting with votes.

It should be supported by some pre-populated demos that highlight its simplicity and clarity.

This should be ultimately be a free online service allowing experimentation with all parts of Monsuite but to get going, its games in the python shell where you can invoke the functions and test behaviours.

Simple Voting
-------------

Alice, Bob and Charles have identities (they can sign things so we know they've signed them and we can encrypt things just for them).
They can propose an action (a dict fttb) with an expiry. On expiry, if the action has enough votes it is enacted.


puniverse
   monsuite
      member
         [id]
            public_key



puniverse
   hierarchical namespace of organisations

organisation
   An organization is a hierarchy of data. The implications of this data are outside the scope of the sandbox

member
   A member is an identity with a public key that

