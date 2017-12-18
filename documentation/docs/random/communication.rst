Communication
=============

Monsuite will become a collection of services that may communicate with each other and with users.

Authentication and encryption will routinely be needed.

Source and destination obfuscation may also be needed.

For the approach to scale, we'll start with assuming https but will also allow for direct messaging where services are co-hosted.

To implement this we need an agreed global messaging protocol - `google protocol buffers <https://developers.google.com/protocol-buffers/>`_.