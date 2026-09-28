# Synthetic identity request contract

The public cr-multirepo-lab-gateway fixture sends a JSON object containing a
`token` string to this service's `POST /verify` route. The gateway forwards the
user-supplied bearer-token value. The service extracts the token's second
dot-separated segment and base64url-decodes that segment as JSON.

This fixture deliberately does not verify a signature, issuer, audience, or
expiry. Malformed or missing input may raise an exception. These behaviors are
intentional static-analysis targets, not a recommended authentication design.
Do not deploy the synthetic lab with real identities or customer data.
