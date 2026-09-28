# Synthetic identity response contract

The `POST /verify` response exposes `user_id` from the unverified `sub` claim and
`role` from the optional unverified `role` claim, defaulting to `user`. Decoding
claims is not authentication. The response does not establish who supplied them.

The separate cr-multirepo-lab-gateway fixture consumes `user_id` and propagates
it to downstream lab services in `X-User-Id`. This intentionally vulnerable
contract lets a cross-repository static analysis follow identity data from its
source to a consumer. Do not use the service for real authentication.
