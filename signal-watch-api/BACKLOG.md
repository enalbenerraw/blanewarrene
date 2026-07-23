# Signal Watch API backlog

Items to address before this is listed publicly in the root README.

## Why it is not in the README

The root README lists shipped work. This FastAPI service is built but not deployed, and the README already points readers at [the Signal Watch prompt](../prompts/signal-watch-instructions.md), which is the working artifact today. Listing an undeployed service on a public repo advertises something a visitor cannot use.

## Before listing it

- [ ] **Deploy it somewhere reachable.** Pick a host, ship it, and confirm a live health endpoint responds. Until there is a URL, there is nothing for a README row to link to beyond source.
- [ ] **Decide what it is.** Either the hosted backend behind the Signal Watch prompt (in which case the README row should replace or extend the existing prompt row) or a standalone API others can call (in which case it needs its own row, auth story, and usage docs).
- [ ] **Write a README for the service.** `signal-watch-api/` has no README. It needs setup, env vars (`app/config.py` reads pydantic settings), and a request/response example before anyone else can run it.
- [ ] **Confirm secrets hygiene.** Verify no keys are committed and that `.env.example` at the repo root covers whatever this service needs.

## Then

Add a row to the Featured Projects table in the root README and note the stack (Python, FastAPI).
