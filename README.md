# Synthetic multi-repository security lab: identity

Deliberately vulnerable, synthetic code for authorized static-analysis testing. Do not expose or deploy this lab. No real customer data or secrets are present.

This service is called through the gateway, which supplies X-User-Id after consulting identity.

## Repository map

- [gateway](https://github.com/sainath1204/cr-multirepo-lab-gateway)
- [identity](https://github.com/sainath1204/cr-multirepo-lab-identity)
- [orders](https://github.com/sainath1204/cr-multirepo-lab-orders)
- [files](https://github.com/sainath1204/cr-multirepo-lab-files)
- [fetch](https://github.com/sainath1204/cr-multirepo-lab-fetch)
- [templates](https://github.com/sainath1204/cr-multirepo-lab-templates)
- [jobs](https://github.com/sainath1204/cr-multirepo-lab-jobs)
- [archives](https://github.com/sainath1204/cr-multirepo-lab-archives)
- [redirects](https://github.com/sainath1204/cr-multirepo-lab-redirects)
- [search](https://github.com/sainath1204/cr-multirepo-lab-search)

## Gateway contract

The [gateway](https://github.com/sainath1204/cr-multirepo-lab-gateway) calls
`POST /verify` with a JSON `token`. The response carries `user_id` and `role`;
the gateway propagates `user_id` to the other lab services through `X-User-Id`.
The endpoint only extracts unverified claims: it does not validate token
signatures. The deliberately vulnerable gateway trusts this output on every
proxied `/api/<service>/...` route; real applications must not treat it as
authenticated identity. The gateway's `compose.yaml` pins this
service to a specific source revision, so default-branch changes alone do not
change that composed fixture.
