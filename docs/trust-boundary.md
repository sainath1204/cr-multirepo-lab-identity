# Synthetic cross-repository trust boundary

The caller and identity service live in separate public fixture repositories:

- https://github.com/sainath1204/cr-multirepo-lab-gateway
- https://github.com/sainath1204/cr-multirepo-lab-identity

The gateway calls identity before forwarding `/api/<service>/...` requests.
Identity decodes attacker-supplied claims without verification; the gateway
then treats the resulting user ID as authenticated. Downstream services can
therefore receive a forged `X-User-Id`. Both sides of this boundary are required
to explain the intended synthetic multi-repository finding.

This document describes a deliberately unsafe test fixture, not a secure
reference implementation. Never expose this lab to real users or data.
