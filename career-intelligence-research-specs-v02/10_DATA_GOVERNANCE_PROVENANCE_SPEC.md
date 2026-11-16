# Data governance, provenance and lineage

Treat every recommendation as a claim with provenance. Separate first-party outcome evidence, curated research, vendor claims and model inference.

## Evidence hierarchy

Observed product outcome > independently replicated research > authoritative public dataset > vendor documentation/claim > secondary reporting > model inference. Lower levels may inform but should not masquerade as verified fact.

## Lineage

source → extraction → normalization → entity resolution → inference → recommendation → outcome.

## Claim object

claim_id, statement, claim_type, evidence_refs, confidence, source_date, verification_date, reviewer, valid_from, valid_to.

## Correction

Corrections create a new version and invalidate affected projections. Never silently overwrite historical evidence.
