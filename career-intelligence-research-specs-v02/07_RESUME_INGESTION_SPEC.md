# Resume / Document Ingestion Specification

## Inputs
PDF, DOCX, TXT, LinkedIn export, portfolio, certificates, training documents, job descriptions.

## Pipeline
document → extraction → segmentation → entity recognition → normalization → evidence linking → confidence → user correction.

## Extract
titles, employers, dates, achievements, tasks, skills, tools, technologies, certifications, education, languages, industries.

## Do not state inference as fact
«Senior» from title may be ambiguous; leadership may be inferred but must be tagged inferred.

## Evidence
Every extracted claim stores source span, document ID, extraction confidence, normalized entity and evidence type.

## UX
«Найдено 42 skills. Проверьте 7 с низкой уверенностью.»

## Multi-resume
Master profile + target-role resume variants. Targeted CV must not overwrite canonical profile.

## Privacy
Consent, deletion, export, retention policy, access control, no hidden secondary use.
