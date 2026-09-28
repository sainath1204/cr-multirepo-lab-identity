# Synthetic lab source revisions

The gateway fixture's `compose.yaml` pins sibling repositories, including this
identity service, to exact source commits. A new commit on this repository's
default branch does not by itself update that composed source revision.

When testing cross-repository analysis, distinguish the selected source commit
from the current default branch. Retained citations should use the selected
full commit SHA and valid line ranges at that revision. Source references do
not establish which version is running in any deployment.

The lab is public and synthetic and is intended only for authorized analysis.
Do not deploy it with real user identities, secrets, or customer data.
