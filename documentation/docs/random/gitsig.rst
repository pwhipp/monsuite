Gitsig
======

Validation and permission handling using signatures in git

require signatures to commit via a git hook. Used on the POT.

A signature is generated using pgp and make_signature_hash. make_signature_hash is applied using the .signature file
to generate an ordered concatenation of the specified file content.

A <name>.sigs folder contains all the sigs for the adjacent name

How do we express and retain signature requirements?


How do we present signature status (badge)?

dot signature file
-------------------------

same format as ``.gitignore``.

Describes the files and folders required for the signature.
